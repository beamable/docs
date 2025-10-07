# Content - Code

## Code

!!! info "Code Example"

    • See code examples at [GitHub.com/Beamable_SDK_Examples](https://www.Github.com/beamable/Beamable_SDK_Examples/)

API highlights for [ContentService](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Content_1_1ContentService.html#details).

### Subscribe

```csharp
private async void SetupBeamable()
{ 
    var beamContext = BeamContext.Default;
    await beamContext.OnReady;
      
    // Fetch All  
    beamContext.Api.ContentService.Subscribe(clientManifest =>
    {
        Debug.Log($"#1. ContentService, all object count = {clientManifest.entries.Count}");
    });

    // Fetch Filtered 
    beamContext.Api.ContentService.Subscribe("items", clientManifest =>
    {
        Debug.Log($"#2. ContentService, filtered 'items' object count = {clientManifest.entries.Count}");
    });
}
```

### Content Subscription vs ContentLink/ContentRef

Beamable supports subscriptions to Content as well as direct references to certain pieces of content. Both of these will allow you to download content from the server, depending on the Game Maker's needs.

Subscriptions use a PlatformSubscription to dynamically read the data on the server, and fire a callback when the data is changed. However, ContentLink and ContentRef are both resolved manually when the data is needed:

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

!!! info "Best Practice"

    If the content that your game is using is known ahead of time (e.g. there will only be subtle differences in existing pieces of content), a content reference (such as ContentLink or ContentRef) should be used.
    
    However, if the content in your game needs to be more dynamic (e.g. the Game Maker will be pushing entirely new pieces of content, unknown to the game client), a content subscription should be used.

### GetContent Method

Beamable's ContentService has another method that can pull content: GetContent. Since this method will attempt to pull several pieces of content at once, it is often inefficient, however it may be useful depending on the scope of your project.

```csharp
private string contentIdToLoad;

private async void GetContent()
{
    var rawContent = await _beamContext.Api.ContentService.GetContent(contentIdToLoad); //Returns as IContentObject
    var content = rawContent as ItemContent;
    //content can now be used as ItemContent
}
```

## Advanced

### ContentLink vs ContentRef

Beamable supports 2 methodologies for referencing a content object; [`ContentLink`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1ContentLink.html) and [`ContentRef`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1ContentRef.html). While they are both very similar syntactically and need to be resolved before using, they perform differently and have different use-cases.

- `ContentLink` - Beamable will perform a first frame load to resolve the reference. `ContentLink`s must be present and resolvable (that is, they cannot be `null`)
- `ContentRef` - Beamable will perform a lazy load to resolve the reference. As such, it is okay for a `ContentRef` to be `null` as long as it is never resolved

See [Content » Guide (Steps)](doc:content-guide#step) for more info.

!!! info "Best Practice"

    - DO: Use `ContentLink` in any member variable in your _custom_ content type which references another content type. ContentLink is useful for data that needs to be loaded quickly at runtime, since it is preloaded in very early stages of the application's lifecycle.
    - DON'T: Use `ContentRef` by default _everywhere_ in your project. This is supported but is considered overkill. ContentRef is useful for data that the application can afford to load on-demand (especially data that might not get loaded at all).

### Content Caching

Content is cached by the client and stored both in memory and persisted to disk. When content is updated on our backend, Beamable updates a client manifest and push it to all clients to invalidate and update the cache. 

See source code of `Runtime/DisruptorEngine/Content/ContentCache.cs` for more info.

### Content ID

The content ID is assigned at creation, and is composed of content `type` and content `id`. A content ID always starts with the content type.

For example, a currency content for dollars would be `currency.dollars`.

**Nesting**

Content may be nested too, and the resulting hierarchy will be baked in to the name. 

For example, to group "weekend" events under a common folder -- the content ID would be `events.weekend.<user-defined-id>`. 

### Content Serialization

Unity's built-in features use [Unity's serialization](https://docs.unity3d.com/Manual/script-Serialization.html). 

However, Beamable's custom content types rely instead on Beamable's custom serialization. This serialization is strict and has limitations.

| Supported Types | Unsupported Types |
|-----------------|-------------------|
| • Unity's [`AssetReference`](https://docs.unity3d.com/Packages/com.unity.addressables@0.3/api/UnityEngine.AddressableAssets.AssetReference.html)<br/>• Unity's [`Color`](https://docs.unity3d.com/ScriptReference/Color.html)<br/>• `bool`<br/>• `double`<br/>• `enum`<br/>• `float`<br/>• `int`<br/>• `List`<br/>• `long`<br/>• `string`<br/>• `System.Object` (and child types)<br/>• [`ContentRef`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1ContentRef.html)<br/>• [`ContentLink`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Common_1_1Content_1_1ContentLink.html) | • Unity's [`MonoBehaviour`](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html)<br/>• Unity's [`ScriptableObject`](https://docs.unity3d.com/ScriptReference/ScriptableObject.html)<br/>• Etc... |

**Excluding Fields from Serialization**

The `[IgnoreContentFieldAttribute]` can be applied to any field that you wish to exclude from the Content Serialization process.

MyCustomContent.cs
```csharp
[Agnostic]
[ContentType("MyCustomContent")]
public class MyCustomContent : ContentObject 
{
     public string Name;
     public AssetReferenceSprite Icon;

     [IgnoreContentFieldAttribute]
     public Dictionary<string, int> KeyValuePair;

}
```

### Content Validation

Beamable supports optional validation for each field of a `ContentObject` subclass. This allows game makers to easily build tooling to facilitate team members with their content administration tasks.

See [Content - Validation](doc:content-validation) for more info.

### Storage Location of Content Types

Each content object derives from Unity's [`ScriptableObject`](https://docs.unity3d.com/Manual/class-ScriptableObject.html), is an asset file written to disk, and is therefore persistent between sessions.

While all content objects must go in this location, game makers may choose to create custom subfolders within. 

**Development (Unity Editor)**

```csharp
/Assets/Beamable/Editor/content/
```

**Deployment (On-device)**  
The development location is not included in the built game project. Instead, when the player loads the game, a fresh copy of all content is retrieved from the Beamable back-end and stored on-device. This allows Beamable to serve _dynamic_ content to the game project. By default, this is a lazy loading operation. Each of Beamable's feature prefabs show a loading progress indicator UI automatically.

Content is stored on-device in a within Unity's [`Application.persistentDataPath`](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html).

```csharp
 Application.persistentDataPath + $"/content/{contentId}.json";
```

### Game Content Designer

Config data, or "Content" as it is called within Beamable, is realm-scoped and can be deployed from either...

- **Unity** -  Via Unity's [`ScriptableObject`](https://docs.unity3d.com/Manual/class-ScriptableObject.html)
- **Google Sheets** -  Via Beamable's [Game Content Designer](doc:game-content-designer)

Within the context of a CI/CD pipeline, game makers can create jobs that invoke the Content deployment function against data it pulled from source control, and pass in arguments for which realm this Content should go to. This is not theoretical, this is what game makers do today in production. 

### Content with Microservices

This 'MyCustomContent.cs' snippet includes the  `[Agnostic]` attribute. To make content classes available to your microservices, add the attribute to your content classes.

See [Microservices](doc:microservices-feature-overview) for more info.

MyCustomContent.cs
```csharp
[Agnostic]
[ContentType("MyCustomContent")]
public class MyCustomContent : ContentObject { ... }
```

### Content Namespaces

!!! warning "Global Namespace"

    Beamable APIs that use content under the hood can _only_ look to the global namespace.

```csharp
public class Tester : MonoBehaviour
{
    public CurrencyRef currency;

    async void Start()
    {
        var ctx = BeamContext.Default;

        ctx.Content.GetContent(content.Id, "tuna");

        var service = (ContentService)ctx.Content;
        service.SwitchDefaultManifestID("tuna");
        var content = await currency.Resolve();
    }
}
```
