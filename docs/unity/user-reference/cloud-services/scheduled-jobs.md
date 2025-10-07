# Scheduled Jobs

A scheduled job is a networking event that happens in the future. Scheduled jobs can be microservice `Callable` invocations, HTTP calls, or generalized Beamable message bus events. Today, scheduled jobs are available directly via the Beamable API (see the [Open API swagger](https://dev.api.beamable.com/api/platform/docs) doc), or through an SDK accessible in Microservices using Beamable 1.16.0 or later.

Every scheduled job has 4 main components, 

- Metadata
- A single action
- A list of triggers
- A retry policy

## Job Metadata

The metadata for a job includes a `name`, a `source`, and after it is saved, an `id`. The `name` and `source` can both be used to search for existing jobs. The `id` is unique for each job. 

Commonly, the `source` represents the entity or process that creates a job. By default, the `source` will be the Microservice's name that schedules the job. 

The `name` can be anything, but should be used to uniquely describe the job. For example, before creating a job to award bonus currency to a player, your system can check for the existence of a job with the name, `$"award-{Context.UserId}"`, and only if the job does _not_ exist, will you create it.

## Job Actions

A job must execute a single action. That action can be a privileged call to a Microservice, an HTTP call, or an internal Beamable message bus call. In the SDK, only Microservice and HTTP calls are supported. 

### Microservice Action

A scheduled job executing a Microservice should use the `.Schedule().Microservice()` utility function.  

```csharp
var job = await Services.Scheduler.Schedule()
	.Microservice<ExampleService>()
	.Run(n => n.ExampleMethod)
	.OnCron(c => c.Daily())
	.Save("example");
```

The `.Microservice<ExampleService>()` method allows the developer to use the `Run()` method, which will require the developer to provide an expression mapping to a callable method. The input parameter to `Run()` should map an instance of the desired service to the _method group_ that will be run when the job executes. The lack of parenthesis on `n => n.ExampleMethod` indicates it is a method group. If the desired method takes input arguments,  the values should be passed as additional arguments to the `.Run()` method.

The target method group must return a `Task` or `Promise`. It is invalid to schedule a call to a function that itself returns any value. The target method should be marked with the `[ServerCallable]` attribute. When Beamable executes the job and calls the method, it will not provide any `playerId`, so the `[ClientCallable]` attribute will be invalid. However, to protect and secure endpoints, they should require the admin `"*"` scope. The `[ServerCallable]` attribute ensures that the method invocation has the admin scope, but does not need a `playerId`. 

The `.Microservice<T>()` method takes an optional parameter called `useLocal`. When Beamable executes the job, it can send a request to a locally running Microservice, or to the deployed Microservice on the realm. When `useLocal` is set to `true`, the request will be sent to whatever address scheduled the job. For local testing, this means that if you schedule a Microservice action from a locally running Microservice, your locally running Microservice will be expected to handle the method call later. If the remote service is used to schedule the job, then the remote service will be sent the invocation. If `useLocal` is set to `false`, then all requests will always be sent to the remote, even if they were scheduled from a locally running service.  
By default, `useLocal` is set as `true`. 

### HTTP Action

A scheduled job executing a HTTP request should use the `.Schedule().Http()` utility function.

```csharp
var job = await Services.Scheduler.Schedule()
	.Http()
	.Run(Method.GET, "https://webhook.site/2e7e3ca0-a771-4515-8570-e925c69f2059")
	.OnCron(c => c.Daily())
	.Save("sample");
```

The `.Http()` method allows the developer to use the `.Run()` function which creates a HTTP action for the job. Optionally, a third parameter can be given as the body for the HTTP request. By default, the HTTP action will use JSON to serialize any request payload. There are overloads of the method available that allow a developer to specify a custom body, accept header, and custom headers.  

## Job Triggers

A job must have at least 1 trigger, but may have many. A trigger is some schedule that defines when the job should execute the action. There are two types of triggers, a cron trigger, and a time trigger. 

### Time Triggers

A time trigger specifies an exact time for a job to execute. There are a few utility methods to assist in creating time triggers.

In this example, the `OnExactDate` method is used to schedule the job to execute once on the 1st of April, 2024.

```csharp
var job = await Services.Scheduler.Schedule()
	.Http()
	.Run(Method.GET, "https://example.com")
	.OnExactDate(new DateTime(2024, 4, 1))
	.Save("sample");
```

In this example, the `After` method is used to schedule the job to execute once thirty seconds after `.Save()` called.

```csharp
var job = await Services.Scheduler.Schedule()
	.Http()
	.Run(Method.GET, "https://example.com")
	.After(TimeSpan.FromSeconds(30))
	.Save("sample");
```

### Cron Triggers

A cron trigger specifies an [NCronTab](https://github.com/atifaziz/NCrontab) expression that dictates a series of times when the job should execute. Cron expressions are unbounded, and have no end date. The cron expression must be a 6 term expression, in this format

```text
* * * * * *
- - - - - -
| | | | | |
| | | | | +--- day of week (0 - 6) (Sunday=0)
| | | | +----- month (1 - 12)
| | | +------- day of month (1 - 31)
| | +--------- hour (0 - 23)
| +----------- min (0 - 59)
+------------- sec (0 - 59)
```

Creating cron strings by hand is allowed, but is tricky for the uninitiated. As an alternative, there is a cron builder utility function. 

```csharp
var job = await Services.Scheduler.Schedule()
	.Http()
	.Run(Method.GET, "https://example.com")
	.OnCron(c => c
		.AtSecond(0)
		.AtMinute(0)
		.AtHour(0)
		.OnDayOfMonth(1)
		.InApril()
	)
	.Save("sample");
```

The cron builder must specify all components of the cron string. Each time unit has an `At` method that specifies an exact value for the time. Each time unit also has an `Every` variant that puts a `*` in the place of that time value. Each time unit also has an `EveryNth` that places a `n/*` value in the cron string. `Between` and `Complex` can also be provided. 

!!! warning "Don't forget about Cron Triggers!"

    It is easy to create a scheduled job using a cron trigger, and then forget it exists! Make sure keep track of your cron jobs. The API and SDK can search for active jobs, but it is always a good idea to have a sense of the jobs running in your realm.

For common schedule types (daily, weekly, monthly, twiceMonthly), short cuts exist.  
This table shows common schedule patterns that may be helpful.

| Code                                                                                                       | Description                                                                     |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `.OnCron(c => c.Weekly(day: 1, hour:12)`                                                                   | Every week on Monday at Noon (UTC)                                              |
| `.OnCron(c => c.Daily())`                                                                                  | Every day at midnight                                                           |
| `.OnCron(c => c.Monthly(day: 15))`                                                                         | Every month on the 15th day                                                     |
| `.OnCron(c => c 	.AtSecond(0) 	.EveryNthMinute(30) 	.EveryHour() 	.EveryDayOfTheWeek() 	.EveryMonth() )`   | On the first second, every 30 minutes, all the time                             |
| `.OnCron(c => c   		.AtSecond(0)   		.AtMinute(0)   		.EveryNthHour(2)   		.OnFriday()   		.InJuly()   	)` | On the first second, of the first minute, every other hour, on Fridays in July. |

## Job Retry Policy

Every job has a retry policy. Each time a job executes, if the action fails, the execution has failed. When an execution fails, the retry policy determines what happens next. If the policy allows, the action is retried until it either succeeds, or the policy is exhausted. 

The default retry policy allows for 1 retry, after 10 seconds.  
In this sample, the policy is set to allow for 2 retries, half a second apart.

```csharp
var job = await Services.Scheduler.Schedule()
	.Http()
	.Run(Method.GET, "https://example.com")
	.OnCron(c => c.Daily())
	.WithRetryPolicy(maxRetryCount: 2, retryDelayMs:500)
	.Save("sample");
```

## Job Executions

A job may execute many times depending on the job's triggers. It may be useful to know about past executions, and upcoming executions. 

### Upcoming Job Executions

This code sample will acquire the upcoming job executions for a job with the given id.

```csharp
var api = Provider.GetService<BeamScheduler>();
var upcoming = await api.GetJobUpcomingExecutions(jobId);
```

Upcoming job executions are `DateTime` structures. If the job has a cron trigger, then this will return the first 1000 execution times. An optional `limit` parameter may be passed to get less or more executions. 

### Past and Current Executions

This code sample will acquire past and ongoing job executions for a job with the given id.

```csharp
var api = Provider.GetService<BeamScheduler>();
var executions = await api.GetJobActivity(jobId);
```

Each execution will have a list of events that describe the execution's current state. This table shows the various execution states.

| State      | Description                                                                        |
| :--------- | :--------------------------------------------------------------------------------- |
| ENQUEUED   | The job has been accepted into the Beamable system.                                |
| DISPATCHED | The job will attempt to execute at the next scheduled execution time.              |
| RUNNING    | The job has started running.                                                       |
| DONE       | The job has completed without error.                                               |
| CANCELED   | The job has been stopped.                                                          |
| ERROR      | The job has failed. The `message` field of the event should have an error message. |

## Managing Jobs

After a job has been created, it can be left to execute, modified, or canceled. Canceling or modifying a job will take effect on the next execution of the job. These operations identify jobs by their identifier, the `id` field of the `Job` data structure. If you need to find a job by name, the `GetJobs` method allows searching by name.

### Canceling a Job

A Job may be canceled at any time. However, if there is an ongoing execution of the Job, it will not be cut short. Instead, the next scheduled execution of the Job will be canceled, as well as all following scheduled executions.

```csharp
await Services.Scheduler.CancelJob(job.id);
```

When a Job is canceled, the actions are left alone, but all Job Triggers are removed from the job.

### Modifying a Job

A Job may be modified to have different triggers, actions, or metadata. The code below shows how this is possible. If there is an ongoing execution of the Job, it will not use the modified data. Instead, the modification will take effect for all future scheduled executions of the Job.

```csharp
var job = await Services.Scheduler.GetJob(job.id);
job.triggers.Add(new ExactTimeEvent(DateTime.UtcNow + TimeSpan.FromHours(1)));
await Services.Scheduler.SaveJob(job);
```

## Getting Started

The code below demonstrates how to create a simple scheduled job that will award a player 10 gems, one minute after the job is scheduled.

```csharp
[Microservice("example")]
public class ExampleService : Microservice
{
	[ClientCallable]
	public async Promise<Job> ScheduleAward()
	{
		var job = await Services.Scheduler
      .Schedule() 
			.Microservice<ExampleService>() // execute a type safe method on the ExampleService
			.Run(t => t.AwardBonus, Context.UserId) // Run AwardBonus, with the current player id.
			.After(TimeSpan.FromMinutes(1)) // Trigger the method in 1 minute
			.Save($"awarding-{Context.UserId}"); // save the job

		return job;
	}

	[ServerCallable]
	public async Task AwardBonus(long userId)
	{
		Debug.Log($"awarding a bonus to player {userId}");
    // Note that ServerCallable has no user ID in its context implicitly,
    // so we must use AssumeNewUser to do anything player-oriented.
    var assumed = AssumeNewUser(userId, requireAdminUser: false);
		await assumed.Services.Inventory.AddCurrency("currency.gems", 10);
	}
}	
```