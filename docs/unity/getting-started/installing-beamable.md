# Setup Unity SDK (Unity)

Welcome to Beamable! This guide will walk you through the steps required to install the Beamable SDK into a Unity project.

!!! info "Compatibility"

    • Beamable supports Unity versions 2021.3 to 6000.3 and is compatible with all template types
    • Beamable supports Windows, Mac, iOS, Android, and WebGL platforms

## Setting Up an Account in the Beamable Portal

To start using Beamable in your project, you need to have a valid Beamable account. Please create an account via our [Portal](https://portal.beamable.com/signup/registration). Please remember your **Alias** as it'll be used to log into the SDK in your editor or via the Beamable CLI.

## Downloading and Installing the Beamable SDK

You can download the Beamable SDK Installer Package [Here](https://packages.beamable.com/com.beamable/Beamable_SDK_Installer.unitypackage).

Once downloaded, follow these steps to install the Beamable SDK into your Unity project.

| Step | Detail |
|------|--------|
| 1. Import the **Beamable SDK Installer Package** | ![Import Package](../../media/imgs/step-1-import-package.png)<br>• Unity → Assets → Import Package → Custom Package |
| 2. Verify the import | ![Verify Import](../../media/imgs/step-2-verify-import.png)<br>• Press the "Import" button |
| 3. Install the **Beamable SDK** | ![Install SDK](./installation-01.png)<br>• Click to continue |
| 4. Remove the **Beamable SDK Installer Package** | • Now that the installation process is complete, the installer package is no longer needed. You can remove it. |
| 5. **Install Dotnet (if required)** | Starting with the Unity 5.0.0 SDK, Beamable requires that you have dotnet 10.0.100 or 8.0.302 installed on your machine. If you don't, the Beamable SDK will offer a download option for you, and once you've finished installing it, you can continue through the dialog. |

Congratulations, the Beamable SDK is now installed!

!!! Note
    If you need to install a Release Candidate version of Beamable, use the _Search for specific version_ drop-down under the main _Install Beamable SDK_ button. You can also find nightly builds here. 

## Log into Beamable

Open the Beamable Login Window by clicking the Beamable button in the Unity toolbar.  Now see the Beamable Login Window prompts for user account credentials. Enter the Organization Alias, Email, and Password with which you signed up for Beamable.

![Beamable Login Window](./login.png){: style="max-width: 400px;" }

Now you're ready to start your first Beamable project!

## Say _Hello_ to Beamable!
To confirm that you have a working Beamable setup, we will pull in the default Beamable runtime console prefab and make sure we can access a player account. 

Navigate to the _Beam Library_ by finding it from the Beamable Button in the top-right of the Unity editor. 

In the _Beam Library_, find the _Admin Console_ card and click the _Add Prefab_ button to add the prefab to an empty scene.
![Beamable Admin Console](./library-admin-console.png){: style="max-width: 700px;"}

Enter play-mode, and hit the `~` character (the same key as `` ` ``). This should open up the _Admin Console_. You can type in a bunch of commands like `help`, or `dbid`. 

!!! Note
    The `dbid` command will print out the current player's id. Learn more in the [frictionless auth section](./../user-reference/beamable-services/identity/frictionless.md).

<try-it-out git-fragment="Assets/Minis/Basics/SetupConsole/Logic.cs" title="Console Access" args="scene=setup_console"/>

## Beam CLI Dependency

The Beamable plugin will automatically install the Beam CLI into your Unity project. The Beam CLI is a developer tool for managing Beamable resources like Microservices, Content, and more. The Beamable Unity plugin relies on the CLI for interacting with Beamable. Your Unity project is a valid Beamable CLI project, which means you can also use the CLI directly if required.

You should expect to see a `.beamable` folder and a `.config`folder in your Unity project's file structure. The `.beamable` folder contains Beamable-specific information about your project, and the `.config` folder is a special `dotnet` folder that defines the version of the Beam CLI. If you are using source-control, you should include both of these folders in source control.

The `.config` folder has a file called `dotnet-tools.json` which specifies the version of the Beam CLI being used by the Beamable Unity SDK. By default, the Beamable SDK will maintain this number, and you should not edit it by hand.

New versions of the Beamable SDK may depend on different versions of the Beam CLI. This table shows which versions of the Beamable SDK depend on what CLI versions. 

| SDK Version | CLI Version |
| :---------- | :---------- |
| 5.0.0       | 7.0.0 |
| 4.0.4       | 6.2.2 |
| 4.0.3       | 6.2.2 |
| 4.0.2       | 6.2.1 |
| 4.0.1       | 6.2.0 |
| 4.0.0       | 6.2.0 |
| 3.1.7       | 5.4.3 |
| 3.1.6       | 5.4.2 |
| 3.1.5       | 5.4.2 |
| 3.1.4       | 5.4.2 |
| 3.1.3       | 5.4.2 |
| 3.1.2       | 5.4.2 |
| 3.1.1       | 5.4.1 |
| 3.1.0       | 5.4.0 |
| 3.0.0       | 5.3.0 |
| 2.4.3       | 4.3.4 |



!!! danger "User Beware: Changing the CLI version may cause issues."

    Starting in SDK 3.0, you _may_ disable the SDK's explicit control of the `dotnet-tools.json` by enabling the `Beamable/Editor/AdvancedCli/Disable Version Requirement` setting in Unity's Project Settings window. If you do this, please understand that the Beamable SDK may stop functioning, as it would then be trying to use an unplanned version.
