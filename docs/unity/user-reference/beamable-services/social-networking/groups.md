# Groups

The **Groups** feature allows players to play together in-game.

The purpose of this feature is to allow players to play together in-game.

Players can create groups and interact in real-time. Interactions include donating currency between group members for spending on in-game items. Depending on the game design, group members may have shared goals where interaction and collaboration are a key part of success.
Here are some common use cases for the Groups feature:

• **Collaboration** - Group members may share resources to progress on common goals (such as quests)
• **Competition** - All groups in the game community compete directly and indirectly for rewards
• **Communication** - Groups functionality integrates with text chat. See [Chat](chat.md) for more info

Here is the glossary of group-related terms.

| Name              | Detail                                                                                       |
| :---------------- | :------------------------------------------------------------------------------------------- |
| Group             | A collection of game players (e.g. a guild)                                                  |
| Group Member      | A game player within the group                                                               |
| Group Member Role | Players within a group may have distinct roles to dictate gameplay limits and responsibilities |

## Groups API

Unlike many Beamable Features, Groups do not require a specific Beamable Feature Prefab to be used. The main entry point to this feature is C# programming.

!!! info "Learning Fundamentals"

    Before using this feature, it's recommended to understand Beamable's fundamental concepts.
    
    • See [Beamable: Asynchronous Programming](https://docs.beamable.com/docs/guides-overview#asynchronous-programming) for more info

The main API highlights include [`GroupsService`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Api_1_1Groups_1_1GroupsService.html).

| Method Name | Detail |
| :---------- | :----- |
| Subscribe | Callback to observe changes |
| CreateGroup | Create a new group |
| GetCurrent | Get list of all current groups |
| JoinGroup | Join a group |
| LeaveGroup | Leave the current group |
| MakeDonationRequest | Request a currency donation from group |
| Donate | Send a currency donation to group member |
| SetGroupProps | Sets the [`GroupUpdateProperties`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Api_1_1Groups_1_1GroupUpdateProperties.html) including...<br>• `Name` - Group name<br>• `Slogan` - External-facing group slogan<br>• `Motd` - Internal-facing message for members<br>• `Tag` - Optional 3 letter shorthand for group<br>• `EnrollmentType` - restricted / open / closed<br><br>- Restricted - By invitation or application only<br>- Closed - By invitation only<br>- Open - Anybody can join |

### Creating Groups

> NOTE: The group tag must be 3 characters or less. Group tags that longer than this will throw an InvalidTag exception.

```csharp
var groupCreateRequest= new GroupCreateRequest ("MyGroupName", "tag", "open", 0, 50);
await _beamContext.Api.GroupsService.CreateGroup (groupCreateRequest);
```

### Requesting Group Donation

```csharp
_beamContext.Api.GroupsService.MakeDonationRequest (groupId, currency);
```

### Make Group Donation

```csharp
_beamContext.Api.GroupsService.Donate (groupId, memberId, 10);
```
### Sample Code

In this example, the player can create a group and interact.

GroupsServiceExample.cs
```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Beamable.Common.Api;
using Beamable.Common.Api.Groups;
using UnityEngine;
using Beamable.Experimental.Api.Chat;
using UnityEngine.Events;

namespace Beamable.Examples.Services.GroupsService
{
    /// <summary>
    /// Holds data for use in the <see cref="GroupsServiceExampleUI"/>.
    /// </summary>
    [System.Serializable]
    public class GroupsServiceExampleData
    {
        public List<string> GroupNames = new List<string>();
        public List<string> GroupPlayerNames = new List<string>();
        public List<string> RoomNames = new List<string>();
        public List<string> RoomPlayerNames = new List<string>();
        public List<string> RoomMessages = new List<string>();
        public string GroupToCreateName = "";
        public bool IsInGroup = false;
        public bool IsInRoom = false;
        public string MessageToSend = "";
      
    }
   
    [System.Serializable]
    public class RefreshedUnityEvent : UnityEvent<GroupsServiceExampleData> { }
    
    /// <summary>
    /// Demonstrates <see cref="GroupsService"/>.
    /// </summary>
    public class GroupsServiceExample : MonoBehaviour
    {
        //  Events  ---------------------------------------
        [HideInInspector]
        public RefreshedUnityEvent OnRefreshed = new RefreshedUnityEvent();
        
        //  Fields  ---------------------------------------
        private ChatView _chatView = null;
        private GroupsView _groupsView = null;
        private BeamContext _beamContext;
        private ChatService _chatService;
        private GroupsServiceExampleData _data = new GroupsServiceExampleData();
    
        //  Unity Methods  --------------------------------
        private async void Start()
        {
            Debug.Log("Start()");

            await SetupBeamable();
        }
        
        //  Methods  --------------------------------------
        private async Task SetupBeamable()
        {
            _beamContext = await BeamContext.Default.Instance;
            _chatService = _beamContext.ServiceProvider.GetService<ChatService>();

            Debug.Log($"beamContext.UserId = {_beamContext.UserId}");

            // Observe GroupsService Changes
            _beamContext.Api.GroupsService.Subscribe(async groupsView =>
            {
                _groupsView = groupsView;
                _data.IsInGroup = _groupsView.Groups.Count > 0;
                
                Debug.Log("GroupsService.Subscribe 1: " + _groupsView.Groups.Count);
                
                _data.GroupNames.Clear();
                _data.GroupPlayerNames.Clear();
                foreach(var groupView in groupsView.Groups)
                {
                    string groupName = $"Name = {groupView.Group.name}, Players = {groupView.Group.members.Count}";
                    _data.GroupNames.Add(groupName);

                    foreach (var member in groupView.Group.members)
                    {
                        string groupPlayerName = $"Name = {member.gamerTag}";
                        _data.GroupPlayerNames.Add(groupPlayerName);
                    }

                    // Create a new chat room for the group
                    string roomName = $"Room For {groupView.Group.name}";
                    await _chatService.CreateRoom(roomName, false,
                        new List<long> {_beamContext.PlayerId});
                    
                }
                Refresh();
            });
            
            // Observe ChatService Changes
            _chatService.Subscribe(chatView =>
            {
                _chatView = chatView;

                int roomsWithPlayers = 0;
                _data.RoomNames.Clear();
                _data.RoomPlayerNames.Clear();
                foreach(RoomHandle room in chatView.roomHandles)
                {
                    // Optional: Only setup non-empty rooms
                    if (room.Players.Count > 0)
                    {
                        roomsWithPlayers++;
                        
                        string roomName = $"Name = {room.Name}, Players = {room.Players.Count}";
                        _data.RoomNames.Add(roomName);

                        foreach (var roomPlayerDbid in room.Players)
                        {
                            string roomPlayerName = $"Player = {roomPlayerDbid}";
                            _data.RoomPlayerNames.Add(roomPlayerName);
                        }

                        room.Subscribe().Then(_ =>
                        {
                            _data.RoomMessages.Clear();
                            foreach (var message in room.Messages)
                            {
                                string roomMessage = $"{message.gamerTag}: {message.content}";
                                _data.RoomMessages.Add(roomMessage);
                            }

                            room.OnMessageReceived += RoomHandle_OnMessageReceived;
                            Refresh();
                        });
                    }
                }

                _data.IsInRoom = roomsWithPlayers > 0;
                Debug.Log("ChatService.Subscribe 1: " + roomsWithPlayers);
                
                Refresh();
            });
        }
        
        public async Task<EmptyResponse> SendGroupMessage()
        {
            foreach(RoomHandle room in _chatView.roomHandles)
            {
                await room.SendMessage(_data.MessageToSend);
            }
            return new EmptyResponse();
        }
        
        public async Task<EmptyResponse> CreateGroup ()
        {
            // Leave any existing group
            await LeaveGroups();
            
            string groupName = _data.GroupToCreateName;
            string groupTag = "t01";
            string enrollmentType = "open";

            // Search existing group
            var groupSearchResponse = await _beamContext.Api.GroupsService.Search(groupName, 
                new List<string> {enrollmentType});
            
            // Join or Create new group
            if (groupSearchResponse.groups.Count > 0)
            {
                foreach (var group in groupSearchResponse.groups)
                {
                    var groupMembershipResponse = await _beamContext.Api.GroupsService.JoinGroup(group.id);
                }
            }
            else
            {
                var groupCreateRequest = new GroupCreateRequest(groupName, groupTag, enrollmentType, 0, 50);
                await _beamContext.Api.GroupsService.CreateGroup(groupCreateRequest);
            }

            // HACK: Force refresh here (0.10.1)
            // Wait (arbitrary milliseconds) for refresh to complete 
            _beamContext.Api.GroupsService.Subscribable.ForceRefresh();
            await Task.Delay(300); 
            
            Refresh();

            return new EmptyResponse();
        }
        
        public async Task<EmptyResponse> LeaveGroups()
        {
            // Leave any existing room
            await LeaveRooms();
            
            // Leave any existing groups
            foreach(var group in _groupsView.Groups)
            {
                var result = await _beamContext.Api.GroupsService.LeaveGroup(group.Group.id);
            }
            
            // HACK: Force refresh here (0.10.1)
            // Wait (arbitrary milliseconds) for refresh to complete 
            _beamContext.Api.GroupsService.Subscribable.ForceRefresh();
            await Task.Delay(300); 
            
            Refresh();
            
            return new EmptyResponse();
        }
        
        public async Task<EmptyResponse> LeaveRooms()
        {
            
            Debug.Log("_chatView 1: " + _chatView.roomHandles.Count);
            foreach(var room in _chatView.roomHandles)
            {
                var result = await _chatService.LeaveRoom(room.Id);
            }
            
            Debug.Log("_chatView 2: " + _chatView.roomHandles.Count);
            
            _data.RoomMessages.Clear();
            Refresh();
            return new EmptyResponse();
        }
        
        public void Refresh()
        {
            // Create new mock message 
            int messageIndex = _data.RoomMessages.Count + 1;
            _data.MessageToSend = $"Hello {messageIndex:000}!";
            
            // Create new mock group name
            int groupIndex = _data.GroupNames.Count + 1;
            _data.GroupToCreateName = $"Group{groupIndex:000}";

            string refreshLog = $"Refresh() ...\n" +
                                $"\n * GroupNames.Count = {_data.GroupNames.Count}" +
                                $"\n * GroupPlayerNames.Count = {_data.GroupPlayerNames.Count}" +
                                $"\n * RoomNames.Count = {_data.RoomNames.Count}" +
                                $"\n * RoomUserNames.Count = {_data.RoomPlayerNames.Count}" +
                                $"\n * IsInGroup = {_data.IsInGroup}" +
                                $"\n * IsInRoom = {_data.IsInRoom}\n\n";
            //Debug.Log(refreshLog);
          
            // Send relevant data to the UI for rendering
            OnRefreshed?.Invoke(_data);
        }
        
        //  Event Handlers  -------------------------------
        private void RoomHandle_OnMessageReceived(Message message)
        {
            string roomMessage = $"{message.gamerTag}: {message.content}";
            _data.RoomMessages.Add(roomMessage);
            Refresh();
        }
    }
}
```

## Adding Group Chat

The chat feature includes full functionality for groups. Players can send chat messages within their group. Players can also send chat messages globally, within rooms, and directly to a specific player. See [Chat](chat.md) for more info.

## Adding Group Events
The events feature includes full functionality for groups. Players can collaborate with group members and get group rewards. See [Events](../live-ops/live-ops.md) for more info.
