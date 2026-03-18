# BeamFarm Demo

This demo showcases how you can use the **Beamable Unreal SDK** in a mobile game project. Particularly it focuses on the Mobile Link Account Flows in Multiple providers like Google and Apple.

## Introduction

Aside from our `BeamableCore` Plugin, here's what the sample contains:

- **`BEAMPROJ_BeamFarm` Unreal Plugin.**: Contains the UE implementation for the sample's client. The core code is inside `LiveOpsDemoMainMenu.h` and part of the implementation is done through BPs inside the folder `UI_BPs` folder of the `BEAMPROJ_Beamfarm` project.
- **`Microservice/BeamfarmMs` Microservice**: Microservice containing code that's used by the sample for various matchmaking and stats stuff.

To set up this sample you'll need a Beamable Account and a Realm. To configure the repo for the sample run `dotnet beam unreal select-sample BEAMPROJ_Beamfarm`.

## Setting up the Project
To set up an organization and realm to run this sample, follow the steps below.

1. Go to the Beamable Portal and create a new Beamable realm called `Beamfarm`
2. Compile and open the `BeamableUnreal` editor project.
3. Sign into your Beamable account and go to the `Beamfarm` realm.
    1. Optionally you can hit `Apply to Build` after the realm change is done.

## Running the Sample in Editor

Leveraging the new Beamable PIE Settings, you can run the sample in editor through two entry points: The Main Menu or the Gameplay scene.

## Running the Sample
1. Open the Unreal editor.
2. Open the `L_Beamfarm_MainScreen` Level if it's not opened yet.
    1. You can find it inside the `BEAMPROJ_Beamfarm Content`  folder.
    2. If you can't see plugin content in your content browser, you can change the settings of the UE `Content Browser` to display it.
3. Go to the `Beamable -> Microservice` window.
    1. You should see the `BeamfarmMS` service there. Select it.
    2. Click `Run` and wait until you see the `Service ready for traffic` log line (and the running icon in the Microservice's card to change).
    3. After you're done with the sample, don't forget to come here and stop the service.
4. You don't need to select any Play Preset, as the `Beamfarm_MainScreen` level is the common entry point for the sample. So leave the Play Preset selector to `None`.
5. Play the `L_Beamfarm_MainScreen` in the Editor.

## Can I use it as a Template?

This sample is not meant to be used as a template directly; however, its components are free for you to copy and use in your own project. Here's what these are:

- The `BeamfarmMS` Microservice : located inside Microservice/BeamfarmMS
- Beamable code and blueprints inside BEAMPROJ_Beamfarm plugin