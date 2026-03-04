# Mail - Overview

The Beamable **Mail** feature allows game makers to create and manage in-game mail messaging systems for players.

The purpose of this feature is to allow players to manage in-game mail messages. Let's say your users have an inbox in their player profile, and they can receive messages whenever something significant happens. This is a good fit for Mail.

Mail provides a robust messaging system that enables players to send and receive persistent messages with attachments and rewards, creating engagement through communication and item distribution.

Unlike many Beamable features, Mail does not have a dedicated feature prefab. The main usages of this feature are listed below.

| Function | Definition |
|----------|------------|
| Send Messages | Send a message to another player's inbox.<br/><br/>_Note: This requires **Admin** privileges._ |
| Receive Messages | Fetches the mail messages from the user's inbox. |

## Using Microservices
If you would like to allow players to send messages without granting players Admin privileges, consider using [Microservices](../../cloud-services/microservices/microservice-framework.md). Sending a message via a microservice allows the game maker to validate the message's contents before the final sendoff.

## Mobile Notifications
Mobile Notifications are a native part of mobile platforms including iOS and Android. These messages show up as a banner of text, regardless of whether or not your game is running. See [Notifications](notifications-overview.md) for more info.

## Mail API

Unlike many Beamable features, Mail does not require a specific Beamable feature prefab to be used. The main entry point to this feature is C# programming. The main API component is [`MailService`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Api_1_1Mail_1_1MailService.html).

The following chart describes the main **functionality** related to mail messages.

| Method Name | Detail |
|-------------|--------|
| GetCurrent | Fetches the count of unread `MailMessage` objects |
| GetMail | Fetches a list of `MailMessage` objects |
| SearchMail | Fetches a list of filtered `MailMessage` objects |
| SendMail | Sends a list of `MailMessage` objects<br/><br/>_Note: This requires **Admin** privileges_ |
| Update | Updates an existing `MailMessage` object<br/><br/>_Note: Uses the [`MailUpdate`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Api_1_1Mail_1_1MailUpdate.html) to define the operation_ |

The main data structure is [`MailMessage`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Api_1_1Mail_1_1MailMessage.html).

The following chart describes the core **structure** of mail messages.

| Parameter Name | Detail |
|----------------|--------|
| id | The unique ID of the mail message |
| sent | The timestamp when sent<br/><br/>_Note: This value is formatted as `2019-03-28T00:00:00Z`_ |
| receiverGamerTag | Receiver PlayerId |
| senderGamerTag | Sender PlayerId |
| category | Arbitrary category string |
| subject | The subject of the mail |
| body | The main content (in text) of the mail |
| state | "unread", "read", or "deleted" |
| expires | The timestamp when expires<br/><br/>_Note: This value is formatted as `2019-03-28T00:00:00Z`_ |

### Sample Code

Below are code examples demonstrating common mail operations. In this `MailServiceExample` snippet, sending mail from the client and receiving mail through subscription is shown.

MailServiceExample.cs
```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Beamable.Common.Api;
using Beamable.Common.Api.Mail;
using Beamable.Examples.Shared;
using UnityEngine;
using UnityEngine.Events;

namespace Beamable.Examples.Services.MailService
{
   /// <summary>
   /// Holds data for use in the <see cref="MailServiceExampleUI"/>.
   /// </summary>
   [System.Serializable]
   public class MailServiceExampleData
   {
      public long Dbid = 0;
      public int UnreadMailCount = 0;
      
      // UI messages that indicate mail exists or not
      public List<string> UnreadMailLogs = new List<string>();
      public List<string> UpdateMailLogs = new List<string>();
      public List<string> SendMailMessageLogs = new List<string>();
      public List<string> MailMessageLogs = new List<string>();
      public bool IsBeamableSetup = false;
   }
   
   [System.Serializable]
   public class RefreshedUnityEvent : UnityEvent<MailServiceExampleData> { }
   
   /// <summary>
   /// Demonstrates <see cref="MailService"/>.
   /// </summary>
   public class MailServiceExample : MonoBehaviour
   {
      //  Events  ---------------------------------------
      [HideInInspector]
      public RefreshedUnityEvent OnRefreshed = new RefreshedUnityEvent();
      
      
      //  Fields  ---------------------------------------
      private BeamContext _beamContext;
      private const string MailCategory = "";
      private MailServiceExampleData _data = new MailServiceExampleData();

      
      //  Unity Methods  --------------------------------
      protected void Start()
      {
         string startLog = $"Start() Instructions..\n" +
                           $"\n * Play Scene" +
                           $"\n * Check for mail using UI. Probably none" +
                           $"\n * Stop Scene" +
                           $"\n * Unity → Window → Beamable → Examples → MailService → Send Test Mail To 
                               Active User" +
                           $"\n * Play Scene" +
                           $"\n * Check for mail using UI. Probably some\n\n";
         
         Debug.Log(startLog);
         
         SetupBeamable();
         Refresh();
      }


      //  Methods  --------------------------------------
      private async void SetupBeamable()
      { 
         _beamContext = BeamContext.Default;
         await _beamContext.OnReady;

         _data.Dbid = _beamContext.UserId;
         Debug.Log($"beamContext.PlayerId = {_data.Dbid}");

         // Fetch All Mail
         _beamContext.Api.MailService.Subscribe(async mailQueryResponse =>
         {
            _data.UnreadMailLogs.Clear();
            _data.UnreadMailCount = mailQueryResponse.unreadCount;
            string unreadMailLog = $"unreadCount = {_data.UnreadMailCount}";
            _data.UnreadMailLogs.Add(unreadMailLog);

            await GetMail();
            Refresh();
         });

         Refresh();
         
         _data.IsBeamableSetup = _beamContext != null;
      }

      
      private async Task<EmptyResponse> GetMail()
      {
         _data.MailMessageLogs.Clear();
         var listMailResponse = await _beamContext.Api.MailService.GetMail(MailCategory);
         foreach (var mailMessage in listMailResponse.result)
         {
            string mailMessageLog = $"MailMessage" +
                                    $"\n\tname = {mailMessage.senderGamerTag}" +
                                    $"\n\tname = {mailMessage.receiverGamerTag}" +
                                    $"\n\tname = {mailMessage.subject}" +
                                    $"\n\tname = {mailMessage.body}" +
                                    $"\n";
            _data.MailMessageLogs.Add(mailMessageLog);
         }
         
         Refresh();

         return new EmptyResponse();
      }

      
      public async void UpdateMail()
      {
         _data.UpdateMailLogs.Clear();
         var mailUpdateRequest = new MailUpdateRequest();
         
         // Arbitrary Example - Toggle "read" to "unread"
         var listMailResponse = await _beamContext.Api.MailService.GetMail(MailCategory);
         foreach (var mailMessage in listMailResponse.result)
         {
            MailState newMailState = MailState.Read;
            if (mailMessage.MailState == MailState.Read)
            {
               newMailState = MailState.Unread;
            }
            mailUpdateRequest.Add(mailMessage.id, newMailState, true, mailMessage.expires);
         }
    
         await _beamContext.Api.MailService.Update(mailUpdateRequest);
         
         string updateMailLog = $"updateMailRequests = {mailUpdateRequest.updateMailRequests.Count}";
         _data.UpdateMailLogs.Add(updateMailLog);
         
         Refresh();
      }
      
      
      public void Refresh()
      {
         if (_data.IsBeamableSetup)
         {
            string refreshLog = $"Refresh() ...\n" +
                                $"\n * UnreadMailCount.Count = {_data.UnreadMailCount}" +
                                $"\n * UnreadMailLogs.Count = {_data.UnreadMailLogs.Count}" +
                                $"\n * MainLogs.Count = {_data.SendMailMessageLogs.Count}" +
                                $"\n * MatchmakingLogs.Count = {_data.MailMessageLogs.Count}\n\n";

            //Debug.Log(refreshLog);
         }

         // Send relevant data to the UI for rendering
         OnRefreshed?.Invoke(_data);
      }
      
      
      /// <summary>
      /// NOTE: This must be called from a user with
      /// admin privileges or from a microservice
      /// </summary>
      public static async void SendMailMessage()
      {
         var beamContext = BeamContext.Default;
         await beamContext.OnReady;
         long playerId = beamContext.UserId;
      
         // Arbitrary Example - Send mail from ME to ME 
         var mailSendRequest = new MailSendRequest();
         var mailSendEntry = new MailSendEntry();
         mailSendEntry.category = MailCategory;
         mailSendEntry.senderGamerTag = playerId;
         mailSendEntry.receiverGamerTag = playerId;
         mailSendEntry.body = $"Test Mail Body From {playerId}.";
         mailSendEntry.subject = $"Test Mail Subject From {playerId}.";
         mailSendRequest.Add(mailSendEntry);

         // Call may fail if sender lacks permissions
         bool isSuccess = true;
         try
         {
            Debug.Log($"beamContext.UserId = {playerId}");
            
            var emptyResponse = await beamContext.Api.MailService.SendMail(mailSendRequest);
         }
         catch (Exception e)
         {
            Debug.LogError(e.Message + "\n\n");
            Debug.LogWarning($"Solution To Error: Add the beamContext.UserId of {playerId} with the role 
                of 'Admin' via Portal → Teams and retry this operation.\n\n");
            isSuccess = false;
         }

         if (isSuccess)
         {
            Debug.Log ($"SendMailMessage() Success!");
         }
      }
   }
}
```
