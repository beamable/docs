
# Unity Beamable SDK 1.x is End Of Life

The 1.x version of the Unity Beamable SDK will not be officially supported as of **December 15th, 2025**. If you have a project using the 1.x version, then you must take action immediately. 

The preferred approach is to upgrade your projects to later versions of the Beamable Unity SDK. To update your project, please see our [upgrade documentation](../whatsnew/2.0.md). 

!!! warning
    Please remember that if you are updating from a 1.x version, you must update to 2.x _before_ you can update beyond 2.0. 

However, if you cannot update the SDK version number, you can apply a small code change to your project to enable continued longevity. 

1. You must add [this file](https://gist.github.com/cdhanna/19cf0c4b0eaaf36b1eabc898224c1d4c) to your `/Assets` folder.
2. You must verify that your realm configuration settings in the Beamable portal do not have a `notification/publisher` value set to `pubnub`. If you do have this setting enabled, then remove it, or change the value to `beamable`. 

Once these two steps are taken, please validate that your game continues to function. Once you have validated your game is working, release the new build to your players. 

!!! danger
    If you are unable to update your project, your game may cease to function. Please [contact us.](https://beamable.com/support) 