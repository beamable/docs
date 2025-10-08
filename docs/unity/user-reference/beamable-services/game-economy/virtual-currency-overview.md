# Virtual Currency - Overview

The Beamable **Currency** feature allows game makers to manage in-game currencies for purchasing and economic systems. Virtual Currencies provide a flexible economic foundation for your game, enabling players to earn, spend, and manage various types of in-game money. The Virtual Currency system in Beamable is built on top of the [Content  System](../profile-storage/content/content-overview.md). Currencies exist out of the box in the Beamable SDK as a content type.

![virtual-currency-experience.png](../../../../../media/imgs/virtual-currency-experience.png){: style="height:auto;width:500px"}

## Managing Currencies

Currencies can be configured from the [Content Manager Editor](../profile-storage/content/content-unity.md#content-manager-editor), with optional parameters for Starting Amount for new players, and "Write Self" under Client Permissions (meaning the client can modify their own currencies). Here is an example of a currency as seen in the inspector:

![Gem Currency Inspector](../../../../../media/imgs/gem-currency-inspector.png){: style="height:auto;width:500px"}

The currencies for a given player can be managed in several ways, depending on your use case.

**Client-Authoritative (Unity code):** If your game does not include networked multiplayer and can tolerate cheating, allowing the client to read/write their own currencies is the simplest option. Examples of this can be seen in the bellow. Note that your currency must have "Write Self" enabled.

**Server-Authoritative (Microservice):** A much more secure way to handle currency modifications is via a Microservice. In this scenario, the client is not able to modify their currencies directly, it is handled on the server. You can check the [Microservices](../../cloud-services/microservices/microservice-framework.md) section for more information.

**Portal (Development):** Player currencies can also be modified through the Portal; Note that this should only be used during development or to make corrections to a player account.

## API

The Beamable API provides helper functions to subscribe to changes in the currency, and modify the currency (if the client can write itself). The basis for the Currency system is built on the InventoryService, which is built on the Content service. If you're not familiar with how Content operations work, you can read about them in the [Content](../profile-storage/content/content-overview.md) section.

The main API components are [`InventoryUpdateBuilder`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Api_1_1Inventory_1_1InventoryUpdateBuilder.html#details) which builds a list of one or more currency operations to execute, and [`InventoryService`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Api_1_1Inventory_1_1InventoryService.html#details) which executes the currency operations.

_Note: This Beamable system handles player inventory **and also** player currency._

### Adding Currency

```csharp
public async void AddCurrency()
{
   // Resolve Reference
   var currencyContentPrimary =  await _currencyRefPrimary.Resolve();
   
   // List the operations
   InventoryUpdateBuilder inventoryUpdateBuilder = new InventoryUpdateBuilder();
   inventoryUpdateBuilder.CurrencyChange(currencyContentPrimary.Id, +1);

   // Execute the operations
   await _beamContext.Inventory.Update(inventoryUpdateBuilder).Then(obj =>
   {
      Debug.Log($"AddCurrency() success.");
   });
}
```

### Removing Currency

```csharp
public async void RemoveCurrency()
{
   // Resolve Reference
   var currencyContentPrimary =  await _currencyRefPrimary.Resolve();
   
   // List the operations
   InventoryUpdateBuilder inventoryUpdateBuilder = new InventoryUpdateBuilder();
   inventoryUpdateBuilder.CurrencyChange(currencyContentPrimary.Id, -1);

   // Execute the operations
   await _beamContext.Inventory.Update(inventoryUpdateBuilder).Then(obj =>
   {
      Debug.Log($"RemoveCurrency() success.");
   });
}
```

### Sample Code
This sample code will subscribe to changes in the available currencies, and the player's owned currencies. It also provides methods to add, remove, and trade between two currencies.

InventoryCurrencyExample.cs
```csharp
using System.Collections.Generic;
using System.Linq;
using Beamable.Common.Api.Inventory;
using Beamable.Common.Content;
using Beamable.Common.Inventory;
using Beamable.Examples.Shared;
using UnityEngine;
using UnityEngine.Events;

namespace Beamable.Examples.Services.InventoryService.InventoryCurrencyExample
{
   [System.Serializable]
   public class InventoryCurrencyExampleEvent : UnityEvent<InventoryCurrencyExampleData> { }

   /// <summary>
   /// Demonstrates <see cref="InventoryService"/>.
   /// </summary>
   public class InventoryCurrencyExample : MonoBehaviour
   {
      //  Events  ---------------------------------------
      [HideInInspector]
      public InventoryCurrencyExampleEvent OnRefreshed = new InventoryCurrencyExampleEvent();
      
      //  Fields  ---------------------------------------
      [SerializeField] private CurrencyRef _currencyRefPrimary = null;
      [SerializeField] private CurrencyRef _currencyRefSecondary = null;

      private BeamContext _beamContext;
      private const int CurrencyDeltaPerClick = 1;
      private const string ContentType = "currency";
      private readonly InventoryCurrencyExampleData _inventoryCurrencyExampleData = new 
          InventoryCurrencyExampleData();
         
      //  Unity Methods  --------------------------------
      protected void Start()
      {
         Debug.Log($"Start()");

         SetupBeamable();
      }

      
      //  Methods  --------------------------------------
      private async void SetupBeamable()
      { 
   
         _beamContext = await BeamContext.Default.Instance;

         Debug.Log($"_beamContext.PlayerId = {_beamContext.PlayerId}");

         _inventoryCurrencyExampleData.CurrencyContentPrimary = 
            await _currencyRefPrimary.Resolve();
         
         _inventoryCurrencyExampleData.CurrencyContentSecondary = 
            await _currencyRefSecondary.Resolve();

         // All currencies (Available in game)
         _beamContext.Api.ContentService.Subscribe(ContentService_OnChanged);
         
         // Filtered currencies (Owned by current player)
         _beamContext.Api.InventoryService.Subscribe(ContentType, InventoryService_OnChanged);

      }

      
      public void Refresh()
      {
         string refreshLog = $"Refresh() ...\n" +
                             $"\n * ContentType = {ContentType}" +
                             $"\n * ContentCurrencyNames.Count = 
                             {_inventoryCurrencyExampleData.ContentCurrencyNames.Count}" +
                             $"\n * InventoryCurrencyNames.Count = 
                             {_inventoryCurrencyExampleData.InventoryCurrencyNames.Count}\n\n";
            
         //Debug.Log(refreshLog);

         OnRefreshed?.Invoke(_inventoryCurrencyExampleData);
      }
      

      public async void AddPrimaryCurrency()
      {
         InventoryUpdateBuilder inventoryUpdateBuilder = new InventoryUpdateBuilder();
         inventoryUpdateBuilder.CurrencyChange(_inventoryCurrencyExampleData.CurrencyContentPrimary.Id, 
            CurrencyDeltaPerClick);

         // Add
         await _beamContext.Api.InventoryService.Update(inventoryUpdateBuilder).Then(obj =>
         {
            Debug.Log($"#1. PLAYER AddPrimaryCurrency2() success.");
                     
         });
      }

      
      public async void RemovePrimaryCurrency()
      {
         InventoryUpdateBuilder inventoryUpdateBuilder = new InventoryUpdateBuilder();
         
         // Remove
         inventoryUpdateBuilder.CurrencyChange(_inventoryCurrencyExampleData.CurrencyContentPrimary.Id, 
            -CurrencyDeltaPerClick);

         await _beamContext.Api.InventoryService.Update(inventoryUpdateBuilder).Then(obj =>
         {
            Debug.Log($"#2. PLAYER RemovePrimaryCurrency() success.");
                     
         });
      }

      
      public async void TradePrimaryToSecondary()
      {
         InventoryUpdateBuilder inventoryUpdateBuilder = new InventoryUpdateBuilder();
         
         // Remove Primary
         inventoryUpdateBuilder.CurrencyChange(_inventoryCurrencyExampleData.CurrencyContentPrimary.Id, 
            -CurrencyDeltaPerClick);
         
         // Add Secondary
         inventoryUpdateBuilder.CurrencyChange(_inventoryCurrencyExampleData.CurrencyContentSecondary.Id, 
            CurrencyDeltaPerClick);

         await _beamContext.Api.InventoryService.Update(inventoryUpdateBuilder).Then(obj =>
         {
            Debug.Log($"#3. PLAYER TradePrimaryToSecondary() success.");
                     
         });
      }
      
      
      public async void TradeSecondaryToPrimary()
      {
         InventoryUpdateBuilder inventoryUpdateBuilder = new InventoryUpdateBuilder();
         
         // Remove Secondary
         inventoryUpdateBuilder.CurrencyChange(_inventoryCurrencyExampleData.CurrencyContentSecondary.Id, 
            -CurrencyDeltaPerClick);
         
         // Add Primary
         inventoryUpdateBuilder.CurrencyChange(_inventoryCurrencyExampleData.CurrencyContentPrimary.Id, 
            CurrencyDeltaPerClick);

         await _beamContext.Api.InventoryService.Update(inventoryUpdateBuilder).Then(obj =>
         {
            Debug.Log($"#4. PLAYER TradeSecondaryToPrimary() success.");
                     
         });
      }
      
      
      //  Event Handlers  -------------------------------
      private void ContentService_OnChanged(ClientManifest clientManifest)
      {
         _inventoryCurrencyExampleData.IsChangedContentService = true;
         
         // Filter to ONLY CurrencyContent
         List<ClientContentInfo> clientContentInfos =  clientManifest.entries.Where((clientContentInfo, i) 
               => 
               ExampleProjectHelper.IsMatchingClientContentInfo(clientContentInfo, ContentType)).ToList();
         
         Debug.Log($"GAME - ContentService_OnChanged, " +
                   $"currencies.Count = {clientContentInfos.Count}");
         
         _inventoryCurrencyExampleData.ContentCurrencyNames.Clear();
         foreach (ClientContentInfo clientContentInfo in clientContentInfos)
         {
            string currencyName = 
                ExampleProjectHelper.GetDisplayNameFromContentId(clientContentInfo.contentId);
            string currencyNameFormatted = $"{currencyName}";
            _inventoryCurrencyExampleData.ContentCurrencyNames.Add(currencyNameFormatted);
         }
         
         // Alphabetize
         _inventoryCurrencyExampleData.ContentCurrencyNames.Sort();
         
         Refresh();
      }
      
      
      private void InventoryService_OnChanged(InventoryView inventoryView)
      {
         _inventoryCurrencyExampleData.IsChangedInventoryService = true;
         
         Debug.Log($"PLAYER - InventoryService_OnChanged, " +
                   $"currencies.Count = {inventoryView.currencies.Count}");

         _inventoryCurrencyExampleData.InventoryCurrencyNames.Clear();
         foreach (KeyValuePair<string, long> kvp in inventoryView.currencies)
         {
            string currencyName = ExampleProjectHelper.GetDisplayNameFromContentId(kvp.Key);
            string currencyNameFormatted = $"{currencyName} x {kvp.Value}";
            _inventoryCurrencyExampleData.InventoryCurrencyNames.Add(currencyNameFormatted);
         }
         
         // Alphabetize
         _inventoryCurrencyExampleData.InventoryCurrencyNames.Sort();
         
         Refresh();
      }
   }
}
```