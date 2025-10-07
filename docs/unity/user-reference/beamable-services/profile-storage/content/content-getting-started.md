# Content - Getting Started
Beamable's ContentService allows game makers to create, manage, and distribute game content. Content can be created in the Beamable Content Manager window in the Unity Editor, and then published to Beamable's servers. Once published, content can be pulled into a game at runtime via the ContentService API.

## Creating Custom Content Types

In this snippet, the custom `Armor` item type is created. Note that, as a subclass of `ItemContent`, whose content type is already `"items"`, Armor's resulting content type will be `"items.armor"`. In the Content Manager in Unity, this will appear as a nested category under the `items` type.

Armor.cs
```csharp
using Beamable.Common.Content;
using Beamable.Common.Inventory;

namespace Beamable.Examples.Services.ContentService
{
    [ContentType("armor")]
    public class Armor : ItemContent
    {
        public string Name = "";
        public int Defense = 0;
    }
}
```

In this snippet, the `Armor` reference is resolved for use at runtime. There are 2 different methods for resolving content. Both are shown here for comparison. In production, choose whichever one method works best for the needs of the project.

See session [ContentLink vs ContentRef](content-overview.md#contentlink-and-contentref) in the Content Overview for more info.

ContentServiceCustomExample.cs
```csharp
using Beamable.Examples.Shared;
using UnityEngine;

namespace Beamable.Examples.Services.ContentService
{
    /// <summary>
    /// Demonstrates <see cref="ContentService"/>.
    /// </summary>
    public class ContentServiceCustomExample : MonoBehaviour
    {
        //  Fields  ---------------------------------------
        [SerializeField] private ArmorLink _armorLink;
        [SerializeField] private ArmorRef _armorRef;

        private Armor _armorFromLink = null;
        private Armor _armorFromRef = null;
        
        //  Unity Methods  --------------------------------
        protected void Start()
        {
            Debug.Log($"Start()");
            
            SetupBeamable();
        }

        //  Methods  --------------------------------------
        private async void SetupBeamable()
        {
            var beamContext = BeamContext.Default;
            await beamContext.OnReady;
      
            Debug.Log($"beamContext.PlayerId = {beamContext.PlayerId}");
            
            await _armorLink.Resolve()
                .Then(content =>
                {
                    _armorFromLink = content; 
                    Debug.Log($"_armorFromLink.Resolve() Success! " +
                              $"Id = {_armorFromLink.Id}");
                })
                .Error(ex =>
                {
                    Debug.LogError($"_armorFromLink.Resolve() Error!"); 
                });
            
            await _armorRef.Resolve()
                .Then(content =>
                {
                    _armorFromRef = content; 
                    Debug.Log($"_armorFromRef.Resolve() Success! " +
                              $"Id = {_armorFromRef.Id}");
                    
                }).Error(ex =>
                {
                    Debug.LogError($"_armorFromRef.Resolve() Error!"); 
                });
            

        }
    }
}
```

## Creating New Content

Game makers may create new content of _existing_ content types or new content of _custom_ content types. For the purposes of this guide, we will be using the existing "Item" type.

| Step | Detail                                                                                                                                                                                                                       |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Open the Content Manager Window | • Unity → Window → Beamable → Open Content Manager                                                                                                                                                                           |
| 2. Create the "Item" content | ![Beamable Content Manager](../../../../../../media/imgs/Beamable_Windows_Content_Manager_Create_Content_v3.jpg)<br/>• Select the content type in the list<br/>• Press the "Create" button<br/>• Populate the content name |
| 3. Open the Unity Project Window | • Unity → Window → General→ Project                                                                                                                                                                                          |
| 4. Select the "Item" asset | • Search by the name given in step #3<br/>• View the asset in the Unity Inspector Window                                                                                                                                     |
| 5. Populate all data fields | ![Item Fields](../../../../../../media/imgs/content-item.jpg)<br/><br/>_Note: The icons can be set to any valid Unity's [`Addressable`](https://docs.unity3d.com/Manual/com.unity.addressables.html) object._             |
| 6. Save the Unity Project | • Unity → File → Save Project<br/><br/>_Best Practice: If you are working on a team, commit to version control in this step._                                                                                                |
| 7. Publish the content | • Press the "Publish" button in the Content Manager Window                                                                                                                                                                   |

## Downloading Content

Content that has been published to the server can be pulled from Beamable's ContentService via a ContentLink or ContentRef. Both are shown in this example.

ContentServiceExistingExample.cs
```csharp
using System;
using Beamable.Common.Content;
using Beamable.Common.Inventory;
using UnityEngine;

namespace Beamable.Examples.Services.ContentService
{
    [Serializable]
    public class ItemLink : ContentLink<ItemContent> {}
    
    /// <summary>
    /// Demonstrates <see cref="ContentService"/>.
    /// </summary>
    public class ContentServiceExistingExample : MonoBehaviour
    {
        //  Fields  ---------------------------------------
        [SerializeField] private ItemLink _itemLink;
        [SerializeField] private ItemRef _itemRef;

        private ItemContent _itemContentFromLink = null;
        private ItemContent _itemContentFromRef = null;
        
        //  Unity Methods  --------------------------------
        protected void Start()
        {
            Debug.Log($"Start()");
            
            SetupBeamable();
        }

        //  Methods  --------------------------------------
        private async void SetupBeamable()
        {
            var beamContext = BeamContext.Default;
            await beamContext.OnReady;
      
            Debug.Log($"beamContext.PlayerId = {beamContext.PlayerId}");
            
            await _itemLink.Resolve()
                .Then(content =>
                {
                    _itemContentFromLink = content; 
                    Debug.Log($"_itemContentFromLink.Resolve() Success! " +
                              $"Id = {_itemContentFromLink.Id}");
                })
                .Error(ex =>
                {
                    Debug.LogError($"_itemContentFromLink.Resolve() Error!"); 
                });
            
            await _itemRef.Resolve()
                .Then(content =>
                {
                    _itemContentFromRef = content; 
                    Debug.Log($"_itemContentFromRef.Resolve() Success! " +
                              $"Id = {_itemContentFromRef.Id}");
                    
                }).Error(ex =>
                {
                    Debug.LogError($"_itemContentFromRef.Resolve() Error!"); 
                });
        }
    }
}
```

After being added to a GameObject, the Inspector will display a drop-down of all valid content entries.

![Content Service Example](../../../../../../media/imgs/ContentServiceExample.png)

Click Play in the Editor and inspect the console to see that the Item content was pulled successfully.

![Content Service Logs](../../../../../../media/imgs/ContentServiceLogs.png)