# Content - Custom Content

Game makers may use the **Content Manager** tool window to add new content of an existing type provided by Beamable.

## Steps

### Adding Content of Existing Type

Here is the process to add a new object with **existing** content type of "Item".

| Step | Detail |
|------|--------|
| 1. Open the Content Manager Window | • Unity → Window → Beamable → Open Content Manager |
| 2. Create the "Item" content | ![Beamable Content Manager](../../../../../../../media/imgs/Beamable_Windows_Content_Manager_Create_Content_v3.jpg)<br/>• Select the content type in the list<br/>• Press the "Create" button<br/>• Populate the content name |
| 3. Open the Unity Project Window | • Unity → Window → General→ Project |
| 4. Select the "Item" asset | • Search by the name given in step #3<br/>• View the asset in the Unity Inspector Window |
| 5. Populate all data fields | ![Item Fields](../../../../../../../media/imgs/item.jpg)<br/><br/>_Note: The icons can be set to any valid Unity's [`Addressable`](https://docs.unity3d.com/Manual/com.unity.addressables.html) object._ |
| 6. Save the Unity Project | • Unity → File → Save Project<br/><br/>_Best Practice: If you are working on a team, commit to version control in this step._ |
| 7. Publish the content | • Press the "Publish" button in the Content Manager Window |

!!! tip "Try using Local Content"

    You can use [Local Content Mode](https://docs.beamable.com/docs/content-manager-overview#local-content-mode) to iterate without publishing your content.

**Code**

!!! info "Code Example"

    • See code examples at [GitHub.com/Beamable_SDK_Examples](https://www.Github.com/beamable/Beamable_SDK_Examples/)

In this snippet, the `Item` reference is resolved for use at runtime. There are 2 different methods for resolving content. Both are shown here for comparison. In production, choose whichever one method works best for the needs of the project. 

See [Content » Code (ContentLink vs ContentRef)](doc:content-code#contentlink-vs-contentref) for more info.

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

**Inspector**

![The Example in the Unity Inspector Window](../../../../../../../media/imgs/exist.jpg)

### Adding Content of Custom Type

Here is the process to add a new object with **custom** content type of "Armor".

| Step            | Detail                                                                 |
| :-------------- | :--------------------------------------------------------------------- |
| 1. Create Armor | • See the `Armor.cs` snippet below                                     |
| 2. Add Armor    | • Repeat steps 1-7 from the section above for the "Armor" content type |

**Code**

!!! info "Code Example"

    • See code examples at [GitHub.com/Beamable_SDK_Examples](https://www.Github.com/beamable/Beamable_SDK_Examples/)

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

See [Content » Code (ContentLink vs ContentRef)](doc:content-code#contentlink-vs-contentref) for more info.

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

**Inspector**

![The Example in the Unity Inspector Window](../../../../../../../media/imgs/custom.jpg)

## Advanced

See [Content » Code (Advanced)](doc:content-code#advanced) for more info.

### Content Validation

Beamable supports optional validation for each field of a `ContentObject` subclass. This allows game makers to easily build tooling to facilitate team members with their content administration tasks.

See [Content - Validation](doc:content-validation) for more info.

### Inheritance Hierarchies

There might be cases where you want to have some hierarchy chain of `ContentObject` but have one of the types in the chain not be an actual `ContentType`; for example, to share code between different child `ContentTypes` but in a parent class that can never be created directly as a piece of Beamable content. You can do that by making the class abstract and **not** marking it as a `ContentType`.

The snippet below demonstrate what that would look like.

```csharp
// BaseCustomContent.cs
[ContentType("BaseCustomContent")]
[System.Serializable]
public class BaseCustomContent : ContentObject { /** (...) */ }

// AbstractCustomContent.cs
// This type is not a Beamable ContentType, but it'll share its members and functions with it's children.
[System.Serializable]
public abstract class AbstractCustomContent : BaseCustomContent { /** (...) */ }

// Leaf1CustomContent.cs
[ContentType("leaf1")]
[System.Serializable]
public class Leaf1CustomContent : AbstractCustomContent { /** (...) */ }

// Leaf2CustomContent.cs
[ContentType("leaf2")]
[System.Serializable]
public class Leaf2CustomContent : AbstractCustomContent { /** (...) */ }
```
