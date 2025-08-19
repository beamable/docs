# PIE Settings

The new Beamable PIE Settings provide a flexible way to configure your game for Play In Editor (PIE). With this system, you can create, capture, and save player profiles for use at runtime, as well as define custom play presets directly within your Unreal projects.

This enables you to test your game across multiple configurations and entry points without repeatedly changing project settings. You can even simulate custom lobbies inside gameplay scenes by overriding both per-player and global settings.

!!! warning "PIE Settings are Experimental"
    PIE Settings are currently marked as Experimental under Project Settings > Beam Core Settings and are disabled by default.
    To enable them, go to the Beamable Core section in the Unreal Engine editor settings. Once enabled, the PIE Settings UI will be available.. ![pie-enable.png](../../../media/imgs/pie-enable.png)

# Player Manager
The Player Manager lets you manage player profiles and settings for your game. It provides an easy-to-use interface to create, capture (from play), and save player profiles that can be used at runtime.

Profiles with a name become available in Play Presets, making it simple to switch between different players during development and testing.

![pie-user.png](../../../media/imgs/pie-user.png)

## Capturing and Saving Players
Whenever you run the game in the editor, the Player Manager records any logged-in players. This creates a new profile in the list, which can be inspected using the Open Portal button.

Player profiles can then be saved as either Local or Template, making them reusable in Play Presets:

* **Local (Green)**: Saved locally in your .beamable folder. Useful for personal testing and development.
* **Template (Orange)**: Saved in your Saved folder and can be committed to version control. Intended as shared templates so the whole team can start from the same baseline.

Profiles marked Grey are Captured Players. These are unsaved, temporary profiles and should be considered disposable.

!!! warning "Player Profile Names and Descriptions"
    Always give saved player profiles a name, as only named profiles will appear in Play Presets.
    You can also add descriptions and tags to profiles to provide extra context for testing scenarios.

# Play Presets
Play Presets let you define how your game should run in PIE. You can create, edit, and delete presets from the Play Presets section of the PIE Settings. This allows you to test different scenarios and entry points without modifying global project settings. Each preset can specify:

* Which maps it applies to
* Whether it should simulate fake lobbies
* Which players will be logged into the session

![pie-settings.png](../../../media/imgs/pie-settings.png)

## Creating and Using Play Presets
To create a new Play Preset, click the **Create New Preset** button. You can then configure the preset with the desired settings. Once created, you can select a preset from tuhe dropdown men in the Main Toolbar UI to apply it to the current map.

![pie-use-preset.png](../../../media/imgs/pie-use-preset.png)

## Map Settings
Play Presets can be configured to apply to specific maps or a list of maps which fill the name rule requirement. This allows you to have different presets for different levels or game modes. You can specify the maps in the **Available Maps** list of the preset editor and/or add a name rule in the Map Name Pattern.

![pie-map-settings.png](../../../media/imgs/pie-map-settings.png)

## Fake Lobbies
Play Presets can simulate artificial lobbies, allowing you to test multiplayer scenarios without requiring real players. This is especially useful when testing games that use the Gameplay scene as the entry point, since it ensures a fully simulated initialization of Beamable systems and lobby setup. Normally, this initialization would occur in earlier scenes, such as the Main Menu or Matchmaking Lobby.  

!!! warning "Integration with Beamable Realtime Multiplayer Systems"
    Notice that the Play Presets Editor is tightly integrated with the Beamable Runtime Multiplayer Systems, having some requirements in your scenes to work properly. For more information, check the [Realtime Multiplayer Overview](../realtime-multiplayer/realtime-multiplayer-overview.md) page.

In the Fake Lobby Settings you can configure:

- **Enable/Disable**: The Checkbox in the header enables or disables the fake lobby simulation for this preset.
- **Server Map Override**: The map that will be used as the server map for the fake lobby. This overrides the default server map defined in the Unreal Project Settings.
- **Game Type**: The Beamable's Game Type that will be used for the fake lobby Scene.
- **Lobby Global Data**: Custom Global Key-Value pairs that will be used to initialize the fake lobby. This data is available in the Gameplay Scene and can be used to simulate different scenarios.

![pie-fake-lobby.png](../../../media/imgs/pie-fake-lobby.png)

## User Settings
The User Settings section allows you to configure per-player settings that will be pre-logged in this session. This is useful for testing different player profiles and configurations without modifying the global project settings.

When Fake Lobbies are enabled, the Add Lobby Data will be available to add custom Key-Value pairs that will be used to initialize the player in the fake lobby. This data is accessible in the Gameplay Scene and can be used to simulate various scenarios such as the selection of a custom skin by the player.

![pie_play_users.png](../../../media/imgs/pie_play_users.png)

!!! warning "Player Profiles"
    Notice that only named profiles will appear in Play Presets to be selected.
