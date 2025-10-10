# Parties

The Beamable **Parties** feature allows players to form parties for short-lived multiplayer sessions.

## Parties API

These examples cover common use cases for Parties. The `_beamContext` variable used below is an instance of the `BeamContext` class may be obtained by `BeamContext.Default`:

### Creating a Party

The `Create` method will fill the state of a current party which can be accessed through `_beamContext.Party.State`.  
The `Create` method has a number of optional parameters:

- `maxSize` determines maximum allowed number of players in the party. 0 means default value which is currently defined by the backend and is equal to 25.
- callbacks for party related events which can be provided later through subscriptions.
- `PartyRestriction` has 2 possible values:
  - `Unrestricted` means the party can be joined by any player who knows the `partyId`
  - `InviteOnly` allows only invited players to join the party

```csharp
await _beamContext.Party.Create(PartyRestriction.Unrestricted);
```

### Listening for Party Updates

The following events are available

```csharp
public Action<PartyInviteNotification> OnPlayerInvited;
public Action<PlayerJoinedNotification> OnPlayerJoined;
public Action<PlayerLeftNotification> OnPlayerLeft;
public Action<PartyUpdatedNotification> OnPartyUpdated;
public Action<PlayerPromotedNotification> OnPlayerPromoted;
public Action<PlayerKickedNotification> OnPlayerKicked;
```

### Joining Party

```csharp
await _beamContext.Party.Join(partyId);
```

### Leaving a Party

```csharp
await _beamContext.Party.Leave();
```

### Getting Party Invites

There is an observable list of available party invites.

```csharp
party.ReceivedPartyInvites.OnElementsAdded += invites =>
{
	// accept the first invite
	invites.First().Accept();
};
```

Additionally, this method returns a `InvitesResponse` object which contains pending party invitations as `List<PartyInvite>`. Each `PartyInvite` contains a `invitedBy` player ID and a `partyId` which can be passed to `Party.Join` method to join the party.

```csharp
var invites = await _beamContext.Party.GetInvites();
```

### Party Leader Methods

Methods below can be called only by a party leader.

#### Updating Party

This method allows to change settings of an already created party. Again `maxSize` parameter is optional. The `State` property is altered by this method.

```csharp
await _beamContext.Party.Update(PartyRestriction.Unrestricted, 5);
```

#### Inviting Player

```csharp
// acquire a playerId from the player social sdk
await _beamContext.Party.Invite(playerId);
```

### Party Member Actions

There is an observable structure, `PartyMembers` that contains the list of party members. If the current player is the leader, they can promote or kick players from this list.

```csharp
party.PartyMembers.OnElementsAdded += members =>
{
	foreach (var member in members)
	{
		Debug.Log($"{member.playerId} joined the party");
	}
};

party.PartyMembers.OnElementRemoved += members =>
{
	foreach (var member in members)
	{
		Debug.Log($"{member.playerId} left the party");
	}
};
```

The `PartyMember` structure has `Promote` and `Kick` methods, but player actions can also be taken with the `Party` accessor directly.

```csharp
// promote the player to party leader
await _beamContext.Party.Promote(playerId);

// remove the player from the party
await _beamContext.Party.Kick(playerId);
```

## FAQ

> Is there a party storage? Similar to `clientData` in `GroupService` that we can utilize?

There is no such storage. All the data related to parties is stored in `_beamContext.Party.State`. The only properties you can change are `restriction` which is either `PartyRestriction.Unrestricted` or `PartyRestriction.InviteOnly` and `maxSize`. To alter them you need to call `Update` method as a party leader.

> Is there any method / way to disband the party?

The party is disbanded automatically when all of the members leave. When a leader leaves the party a new one is chosen automatically.

> What is the difference between `Party.State` vs `Party.Value` ?

Both properties point to the same object. However `Party.Value` is obsolete.

> Is `Party.State` / `Party.Value` automatically updated if there is a change in party data? (new member join, owner change, etc). I found that we can also get Party data directly from `Party`, ex: `Party.Id`, `Party.Members`, `Party.Leader`.  
  Members data is `List<string>`. Are those string values userIds? Why string not long? What is the difference between userId (long) vs playerId (string)?

Yes, party data gets updated automatically based on notifications. Properties like `Party.Id` are just a shorthand for `Party.State.Id`. Use the `PartyMember` observable list to get access to the list of party members instead of the obsolete `Member` list. `PartyMember` instances have `long` userId types instead of `string`.
