# Content - Guide

The purpose of this feature is to allow game maker to store project-specific data objects. In this guide, we will create and publish a content entry, then pull the content from the server within an instance of Unity's [`MonoBehaviour`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html) script.

## Adding Content

Game makers may create new content of _existing_ content types or new content of _custom_ content types. For the purposes of this guide, we will be using the existing "Item" type.

| Step | Detail |
|------|--------|
| 1. Open the Content Manager Window | • Unity → Window → Beamable → Open Content Manager |
| 2. Create the "Item" content | There are two methods of creating new content:<br/><br/>1. Right Click<br/>   • Right-click the content type name;<br/>      • Select the option "Create \<type_name> Content";<br/>      • Populate the content name.<br/>2. Using the create button<br/>     • Select the content type in the list;<br/>     • Press the "Create" button;<br/>     • Populate the content name.<br/>   ![Item Creation](../../../../../../../media/imgs/BeamContent_ItemCreation.png) |
| 3. Select the "Item" asset | • In the Content Window editor, find the created item (you can use the search bar to find it if necessary);<br/>• Left-click it to select it;<br/>• View the asset in the Unity Inspector Window. |
| 4. Populate all data fields | ![Item Fields](../../../../../../../media/imgs/item.jpg)<br/><br/>_Note: The icons can be set to any valid Unity's [`Addressable`](https://docs.unity3d.com/Manual/com.unity.addressables.html) object._ |
| 5. Publish the content | • Press the "Publish" button in the Content Manager Window |

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

!!! info "Learning Fundamentals"

    The above code sample uses C# async methods. However, the same code can be written using the Promise library.
    
    • See [Beamable: Asynchronous Programming](https://docs.beamable.com/docs/guides-overview#asynchronous-programming) for more info

### Inspector

After being added to a GameObject, the Inspector will display a drop-down of all valid content entries.

![Content Service Example](../../../../../../../media/imgs/ContentServiceExample.png)

### Output

Click Play in the Editor and inspect the console to see that the Item content was pulled successfully.

![Content Service Logs](../../../../../../../media/imgs/ContentServiceLogs.png)
