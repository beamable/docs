# Parties

Beamable's Party system provides a comprehensive set of tools for managing player groups in your game. Whether you're
developing a cooperative game, competitive multiplayer, or social gaming features, the Party system offers flexible
options for player collaboration and team organization.

The Beamable **Parties** feature supports various party management operations, including:

- Create
- Join
- Decline Invites

Party Leaders can:

- Invite a player
- Kick a player
- Promote a player to leader
- Cancel the invite

## Getting Started

This section will bring a simple case for a party system and show how to implement it using the Beamable's party subsystem.

To use the party system, first you need to set up your environment with PIE mode, allowing you to play with multiple instances so that you can follow along with this guide.

With the multiplayer instances set we can start creating a Blueprint (BP) function that will do the basic Party operations.

### Creating a Party

1. Open your Level Blueprint (or some other BP)
2. Call `Operation - Party - CreateParty`. It will create a party and put the user slot that called it inside the party.
3. Get the state of the current party that the user is party of.

![party-create](../../../media/imgs/party-create.png)

???+ Warning "Unrestrict/InviteOnly Party Types"
    **Unrestrict**: Allows anyone to join the party without an invite.<br>
    **InviteOnly**: Only invited players can join the party.

### Joining a Party

1. Open your Level Blueprint (or some other BP)
2. Call `TryGetUserPartyState` from the `BeamPartySubsystem`. 
    - If the player is already in a party, it will return true.
    - A player must be removed from their current party before joining another. Trying to join without doing so will return an error.
3. After verifying and removing the player from their existing party if necessary, call the operation: `Operation - Party - JoinPlayerParty`.

![party-join](../../../media/imgs/party-join.png)

???+ Warning "Join Unrestricted Party"
    If the party type is `unrestrict` it's possible to join without receiving an invite from another player.

### Inviting Players (Leader Only)

1. Open your Level Blueprint (or some other BP)
2. Call `Operation - Party - InvitePlayerToMyParty`. It will send an invite to a given FBeamGamerTag.

???+ Warning "Friends"
    It is **NOT** required to be a friend to receive/send a party invite.

![party-send-invite](../../../media/imgs/party-send-invite.png)

### Declining Invites

1. Open your Level Blueprint (or some other BP)
2. Call `Operation - Party - DeclinePlayerInvite`. It will remove the received invite from the invite list of the player.

![party-decline](../../../media/imgs/party-decline.png)

### Canceling Invite (Leader Only)

1. Open your Level Blueprint (or some other BP)
2. Call `Operation - Party - CancelPlayerPartyInvite`. It will cancel the invite sent to another player.

![party-promote-leader](../../../media/imgs/party-promote-leader.png)

### Kicking a Player (Leader Only)

1. Open your Level Blueprint (or some other BP)
2. Call `Operation - Party - Kick Player From My Party`. It will remove a player from the party.

![party-party-kick](../../../media/imgs/party-kick.png)

### Promoting Player to Leader (Leader Only)

1. Open your Level Blueprint (or some other BP)
2. Call `Operation - Party - Promote Player As My Party Leader`. It will promote another player as the party leader.

???+ Warning "Leader Leaving Party"
    When the leader leaves the party, another player will automatically be selected as the party leader.

![party-promote-leader](../../../media/imgs/party-promote-leader.png)

## Events

Events in the party will be used to react to actions like received an invite, join a party, etc.

### Invite Events

Invite events will be used mostly to handle updates to the invite list, like show a popup of a invite or update the friend list with a new party invite.

![party-bind-invite-events](../../../media/imgs/party-bind-invite-events.png)

### Party Events

Party Events are used to handle updates to the party, like updating visuals when players leave/join, for example.

![party-bind-party-events](../../../media/imgs/party-bind-party-events.png)

### Party State Usage

In this case, we are iterating over the player states within the party. This can be used to populate the UI with the party's details.

![party-get-state](../../../media/imgs/party-get-state.png)