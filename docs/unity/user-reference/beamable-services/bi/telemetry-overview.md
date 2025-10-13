# Telemetry

Telemetry is a critical piece needed to write analytic data about your game. Beamable provides you with API's that allow you to write data about what is taking place in your game that can be queried and reported on.

If you wanted to know how many players use a specific weapon in your game in comparison to other weapons, how would you accomplish this? The answer is to write bits of data whenever each weapon is used in order to understand which weapon is used more. This is what we call Telemetry Data.

Telemetry Data by definition are measurements and data that are collected at remote or inaccessible points.

When defining what you want to know about your game, you ultimately want to ask questions about your players and their behaviors. Essentially, you want to ask the underlying questions of **What** and **Why** something happens, does, or is.

Telemetry data can also be used to measure the success of your game. There are three primary outlets of measurement that are common in the gaming industry:

- **Engagement** - Are my players having fun in my game and want to play more and for longer duration?
- **Retention** - Do my players want to come back and play the game day after day? How often do they come back to play?
- **Monetization** - Do players spend money in my game? When do they spend money? How often do they spend money? What is preventing them from spending money?

You can learn more about these concepts in the [Analytics - Overview](analytics-overview.md) where we further discuss Analytics and reporting for your game.

Another use case for Telemetry is to react to what your players are doing in your game. You may want to create groups of players that you can identify according to a behavior pattern. We call these groups **Segments**, and while there are multiple ways to create Segments in Beamable, one of them is to write specific telemetry data about your players' behaviors so you can group them into a Segment for all players with the same behavior.

Segments are great because once your players are segmented, you can run A/B Tests on them. You can learn more about A/B Testing on the [A/B Testing - Overview](ab-testing-overview.md) doc where we explain how to run experiments using Segments.

## Telemetry API

Writing Telemetry data is very easy using the Beamable SDK. But under the hood, it is a simple rest API call. When writing Telemetry, we use the `AnalyticsTracker` and the `TrackEvent` API.

The following example example shows how to write custom telemetry data into the Beamable service. You can query this data later.

!!! info "How to query your custom telemetry data"

    See the [Analytics - Guide](analytics-overview.md) to learn more about how to query your custom telemetry data.

Start off by creating a custom event data structure. This holds the **payload** for your event which you will send to Beamable.

```csharp
public class MyExampleEvent : CoreEvent 
    {
        public MyExampleEvent(string foo, string bar) : base (
            "example",  
            "my_example_event", 
            new Dictionary<string, object>
            {
                ["foo"] = foo,
                ["bar"] = bar,
                ["hello_world"] = "Hello World."
            })
        {
        }
    }
```

Now that you have defined what data you want to send, you can then send that event using the `AnalyticsTracker.TrackEvent()` API. This takes your `CoreEvent` and a flag for whether you want to send it immediately or queued, which we'll talk about in the next section.

```csharp
var beamContext = BeamContext.Default;
await beamContext.OnReady;

//Create an instance of the data you want to send
var foo = "lorem ipsum 1";
var bar = "lorem ipsum 2";
var myExampleEvent = new MyExampleEvent(foo, bar);
            
//Send Immediately
var sendImmediately = true;
//Send the event to Beamable's Analytics Database (Athena)
beamContext.Api.AnalyticsTracker.TrackEvent(myExampleEvent, sendImmediately);
```

The API supports batching together multiple analytics calls (default max limit is 100) within a single client-server communication as an optimization. You will especially want to use the batching feature when you need to write high volumes of data during gameplay. The only difference here is the second parameter of TrackEvent: `sendImmediately`.

```csharp
var beamContext = BeamContext.Default;

var eventOne = new MyExampleEvent("foo1", "bar1");
var eventTwo = new MyExampleEvent("foo2", "bar2");
var eventThree = new MyExampleEvent("foo3", "bar3");

//Tracking them batch-style, passing sendImmediately as false
beamContext.Api.AnalyticsTracker.TrackEvent(eventOne, false);
beamContext.Api.AnalyticsTracker.TrackEvent(eventTwo, false);
beamContext.Api.AnalyticsTracker.TrackEvent(eventThree, false);
```

Analytics event requests will be batched together into a list, then sent off as one API call either when a certain amount of requests has been reached, or after a certain amount of time passes. These values are configurable through the BatchSettings, which can be updated with `UpdateBatchSettings`. The default settings are a 1 second heartbeat, 60 second timeout, and 100 event batch size.

```csharp
var beamContext = BeamContext.Default;

beamContext.Api.AnalyticsTracker.UpdateBatchSettings(
    new BatchSettings
    {
        HeartbeatInterval = 1,
        MaxSize = 100,
        TimeoutSeconds = 60
    });
```
