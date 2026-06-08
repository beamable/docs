# Microservice analytics

Emit custom analytics events from a Beamable Standalone Microservice.

## Dependencies

This guide assumes you have an existing Microservice. You need to complete the
[Getting-Started Guide](getting-started.md). That means having [.NET 10](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) installed, and getting the [Beam CLI](https://www.nuget.org/packages/Beamable.Tools).

You can confirm you have everything installed by checking the versions of the tools.
```sh
dotnet --version
dotnet beam version # dotnet beam --version also works.
```

In order to emit analytics events, you also need to have a local `.beamable/` workspace with a Beamable Standalone Microservice. As a reminder, you can create one quickly using the commands below.
```sh
beam init MyProject
cd MyProject
dotnet beam project new service HelloWorld
```

## Emitting events

Microservices can emit custom analytics events using the `Services.Analytics` API.

Define a subclass of `CoreEvent` to describe your event. The constructor takes a category string, a snake_case event name, and a flat payload dictionary.

```csharp
using System.Collections.Generic;
using Beamable.Api.Analytics;

public class MatchResultEvent : CoreEvent
{
    public MatchResultEvent(string outcome, int score)
        : base("gameplay", "match_result", new Dictionary<string, object>
        {
            ["outcome"] = outcome,
            ["score"] = score,
        })
    {
    }
}
```

Keep the number of distinct categories small - a handful such as `"gameplay"`, `"funnel"`, and `"monetization"` is typical. Event names within a category can be more numerous; a single `"gameplay"` category might contain many sibling event types beyond just `"match_result"`.

Then build and send the event from a callable method using `Services.Analytics`:

```csharp
[ClientCallable]
public async Task<string> RecordMatchResult(string outcome, int score)
{
    var evt = new MatchResultEvent(outcome, score);
    var request = Services.Analytics.BuildRequest(evt);
    Services.Analytics.SendAnalyticsEvent(request);
    return "OK";
}
```

### Source domain

The Microservice analytics API uses the same channel as client-side telemetry. Events emitted from a Microservice therefore appear as **client** records in Athena, not as a separate server or game source.

The Athena table name follows the pattern `client_{category}_{event_name}`. For the example above, the table is `client_gameplay_match_result`.

### Verifying events

After invoking your Microservice method, the event should appear in Athena within a few minutes. You can confirm it with a query like:

```sql
SELECT * FROM client_gameplay_match_result LIMIT 10;
```

Individual player analytics events are also visible on the player profile page in the Beamable Portal.
