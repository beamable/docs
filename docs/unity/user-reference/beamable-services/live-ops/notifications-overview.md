# Notifications - Overview

The Beamable **Notifications** feature allows game makers to message players, regardless if the game is running.

Notifications provide a robust messaging system that enables communication between different parts of your game through a publish/subscribe pattern. Objects can listen for updates (subscribe) with a certain tag. Other objects can then notify the subscribers (publish) with some context-relevant data.

The Notification feature's functionality is actually used by many other features, providing a foundation for a publish/subscribe pattern. For example, `Inventory.Subscribe()` uses the NotificationService's `Subscribe()` function under the hood.

Through the Notification API, the game maker can use this same messaging system for other parts of their game. This means that the purpose of the Notification feature is to expose a feature that Beamable already uses internally in the SDK.

There are two main types of notifications:

- **Local Notifications** - Received on the **client-side** while the game is running.
- **Push Notifications** - Scheduled at any time from the **server-side**, regardless if the game is running. Typically it is received moments after it is scheduled.

Push Notifications are a native part of mobile platforms including iOS and Android. These messages show up as a banner of text, regardless if your game is running. A common use-case is notifying the user when a time-sensitive event is about to occur.

| Name | Beamable Supports | Beamable Requires Firebase | App Must Be Running (To Send) | App Must Be Running (To Receive) |
|------|-------------------|----------------------------|-------------------------------|----------------------------------|
| Push Notifications | ✔️ | ✔️ | ❌ | ✔️ |
| Local Notifications | ✔️ | ❌ | ✔️ | ✔️ |

Beamable offers multiple messaging capabilities to communicate with your player community:

- **1. Mail** - Send persistent messages with attachments and rewards to players. See [Mail](doc:mail-feature-overview) for more info
- **2. Announcements** - Broadcast important news and updates to all players. See [Announcements](doc:announcements-feature-overview) for more info
- **3. Notifications** - Real-time messaging system using publish/subscribe pattern. Continue reading below for more info

!!! warning "Work in Progress"

    This feature is currently under active development with additional capabilities being added.

## Notifications API

The Notifications feature can be accessed via the NotificationsService from the Beamable API. Notifications primarily function using a [Publish-subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern), where objects that should react to incoming messages (the "subscribers") listen for messages being sent out by another object (the "publishers"). Following this pattern, the API is quite simple.

#### Callback Function

When a subscribed object receives a message, the message carries some data with it that can provide extra content about the event that occurred. For the purposes of this document, this function will be used:

```csharp
void CallbackAction(object callbackObject)
{
    //Some code that uses the callback object
}
```

#### Subscribe/Unsubscribe

Subscriptions are PlayerId based, so an event published by the server (e.g., a microservice) must specify your PlayerId in order for your client to receive the event.

```csharp
var beamable = BeamContext.Default;

//Start listening to events published with the specified message name
beamable.Api.NotificationService.Subscribe("messageName", CallbackAction );

//Stop listening for events with the specified message name
beamable.Api.NotificationService.Unsubscribe("messageName", CallbackAction );
```

#### Publish (from Microservice)

```csharp
public async Task SendNotificationFromMicroservice(List<long> playerIds, string context, object payload)
{
    var json = JsonUtility.ToJson(payload);
    await Services.Notifications.NotifyPlayer(playerIds, context, json);
}
```
