# LightBeam Overview

The _Beam Library_ window in the Unity Editor has a list of Lightbeams. Lightbeams are Unity Package Samples designed to teach you various parts of the Beamable SDK. The Lightbeams share a common architectural design pattern. Unity Package Samples are copied into your `/Assets` folder and you have complete control over their source code. This means you can fork these samples into your project, or just delete them when you're done. The Lightbeams are versioned with each release of the Beamable SDK, which means you can have multiple versions of the Lightbeam installed in your `/Assets` folder. 

Most of the Lightbeams are full `.unity`scene files that offer a greybox UI to explore a feature-set. 


## Common Sample Structure

When you open a Lightbeam scene, there may be additional configuration to perform before entering Playmode. Check the documentation for each Lightbeam. 

Almost all of the Lightbeam samples follow a similar structure and layout. 

```shell
/Sample
  SampleConfig.cs         # scriptable object config
  SampleConfig.asset
  SampleManager.cs        # entry point
  Lightbeam.Sample.asmdef
  Lightbeam_Sample.unity  # scene file
  /Prefabs
    /ExamplePrefab
       Example.prefab
       Example.cs
```

The main entry point of the Lightbeam is the class in the root folder that ends with `Manager`. These scripts should roughly all have a `Start()` method that calls the `beamContext.CreateLightBeam()` function, and then the `lightBeam.Scope.Start<HomePage>()`function. 

To start learning about the code in each Lightbeam, jump into the `HomePage` class and start exploring the code. Most of the samples will have an entry point method in the `HomePage` class that looks like this... 

```csharp
public async Promise OnInstantiated(LightBeam ctx)
```



## Lightbeam Framework

Most of the Lightbeam samples use a common framework that builds on top of Beamable's [Dependency Injection](doc:beam-sdk-di). The Lightbeam framework is trying to solve the age-old "UI data binding" problem in a way that feels natural to the Beamable SDK. A `LightBeam` is a dependency scope built with a `BeamContext`, plus whatever `GameObjects` and UI related prefabs that exist to power the greybox UI. The `LightBeam` type is used to instantiate UI prefabs and offer a chance to bind data to those prefab instances directly from the dependency injection scope.  

All Lightbeams require a `BeamContext`, and most of the samples have a `Manager`class with this fragment, 

```csharp
var beamContext = BeamContext.Default;
var lightBeam = await beamContext.CreateLightBeam(root, loadingBlocker, builder => {
  // add extra UI dependencies... 
});
```

The `CreateLightBeam` function takes 3 parameters. The first 2 are UI related. The `root` is a `GameObject` reference where the LightBeam will spawn all future UI panels. The `loadingBlocker` is a `CanvasGroup` that the LightBeam uses to fade transition between panels. Finally, the last parameter is the `builder`, which is a `IDependencyBuilder` object. This instance can be used to add UI prefab types into the dependency scope. 


### Light Components

The Lightbeam framework adds a special extension method to the `IDependencyBuilder`, called `AddLightComponent()`. This method injects a sub-type of `ILightComponent`. These types are UI elements that can be spawned in using the Dependency Injection system. For example, in the Account Lightbeam, it is possible to have several Accounts loaded at once, and each one needs to instantiate a prefab instance as a UI element. The Lightbeam is created with this line in the `CreateLightBeam`'s dependency configuration, 

```csharp
builder.AddLightComponent<AccountDisplayBehaviour, PlayerAccount>(config.accountDisplayTemplate);
```

The class `AccountDisplayBehaviour` has this signature, 

```csharp
public class AccountDisplayBehaviour : MonoBehaviour, ILightComponent<PlayerAccount>
```

The  `ILightComponent<PlayerAcount>` declaration represents that the type is a LightBeam UI component, and the generic argument declares the component needs a `PlayerAccount` instance as an instance level data model. The `ILightComponent<T>`interface only requires one method, the `OnInstantiated` method.

```csharp
	public interface ILightComponent<in T> : ILightRoot
	{
		Promise OnInstantiated(LightBeam beam, T model);
	}
```

 The `OnInstantiated` method receives 2 parameters; the full `LightBeam` context, and an instance of the generic data model. 

The `AccountDisplayBehaviour`'s implementation of this method is abbreviated below, 

```csharp

public Promise OnInstantiated(LightBeam ctx, PlayerAccount model)
{
	playerIdLabel.text = model.GamerTag.ToString();
	aliasLabel.text = model.Alias ?? "Anonymous";
	emailLabel.text = model.Email ?? "";
	avatarImage.sprite = ctx.Scope.GetService<AvatarConfiguration>().GetAvatarSprite(model.Avatar);

	return Promise.Success;
}
```

The purpose of this method is to bind the data from the `PlayerAccount` into the instance of the UI component `AccountDisplayBehaviour` instance. 

Finally, these `AccountDisplayBehaviour` instances are created via the `LightBeam` context like so, 

```csharp
var instance = await lightBeam.Instantiate<AccountDisplayBehaviour, PlayerAccount>(playerAccountContainer, account);
```

The `lightBeam.Instantiate()` method fetches the requested type from the `IDependencyProvider`, instantiates the type as a `GameObject`and attaches the newly spawned `Transform` to the given `playerAccountContainer` transform. Then the `AccountDisplayBehaviour.OnInstantiated`method is invoked on the new instance, and the data argument is forwarded. 

In addition to the `Instantiate` method, the `LightBeam` context has a `GotoPage` method. This method is used to change the top-level UI object under the given `root` GameObject used to create the `LightBeam`. All this method does is use the `CanvasGroup` to fade transition between two `ILightComponent` instances.


### Custom Parameters

Most Lightbeams have a `Manager` class that configures the sample, and in the `Start()` method of these classes, there is a line similar to the following, 

```csharp
await lightBeam.Scope.Start<HomePage>();
```


This line of code bootstraps the `LightBeam` and builds a `IDependencyProvider` . It will open the UI to the `ILightComponent` specified by the generic parameter. However, the function will check for custom parameters, including a custom start page. Lightbeams are designed to be shared via webGL builds, and as such, they can accept these custom parameters through query args in the url. The custom url query arg, `pageType` can be used to specify the class name of the class that should be instantiated first when the Lightbeam initializes. If the given initial page requires a data model, then additional query args can be passed using a custom format that configure the fields in the model type. 

For example, if the model type had a field called `tuna`, then a query arg of `d_tuna` would set the field on the instance passed to the instantiated UI.


### Utility Functions

Although the Lightbeam framework is intended to be minimal, there are a few helper functions that you should know about. The functions exist in the `LightBeamUtilExtensions` class. 


#### Clear

The `Clear()` method is an extension on `Transform` that will destroy all child objects. A common pattern in the Lightbeams is to hold references to `Transforms` that act as containers for other data UI elements. As new data becomes available, the container is cleared of all its child UI elements, and then new UI elements are instantiated under the container transform. Consider using object pooling if you intend to use these Lightbeams in high load scenarios. 

#### EnableObjects and DisableObjects

The `EnableObjects()` and `DisableObjects()` methods are extensions on the `ILightComponent` that will take a parameter list of components and enable or disable the associated `GameObject`s. 

#### HandleClicked

The `HandleClicked()` method is an extension on the `Button` type that attaches a callback to the button click event. This will clear any existing handlers. The method can either run the callback immediately, or if the callback is a long running action (such as a network call), then the button will be transformed into a loading icon while the callback executes. 

#### ShowLoading

The `ShowLoading()` method is an extension of a variety of types, and it acts as a way to show a loading visualization to the user while a `Promise` executes in the background. A `Promise` is a representation of asynchronous work, similar to the dotnet `Task` type.
