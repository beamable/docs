# Unity Editor Login

## Overview

The Beamable Login tool window provides a user interface for managing authentication and account access within the Unity editor environment.

The purpose of this Tool Window is to allow front-end administration of the game maker account.

## The User Interface

Here is the user interface of the Beamable "Login" tool window.

| New User | Existing User                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------|
| ![New User Login](../../../../media/imgs/Beamable_Windows_Login_New_User.jpg){width="300px"} | ![Existing User Login](../../../../media/imgs/Beamable_Windows_Login_Existing_User.jpg){width="300px"} |

To open the panel, select "Log in" from the Beamable Button if you are not logged in, or select your email address if you are logged in.

![Beamable Login Button](../../../../media/imgs/499d63afc4444bf449ce78b29fdd5d7948a080c50f968fa4c4c10a2c68fb7d09-image.png){width="300px"}

![Beamable Login Button](../../../../media/imgs/1aeb1cdb745e27cfe00a335c8684677c8a7e3812ef84f8dcee6ad3366837e036-image.png){width="300px"}


## Login Information

When you log into Beamable in the Unity editor, the log-in information is kept in the `.beamable` workspace folder in your Unity project's root folder. You can run terminal commands from that folder with the same authentication. If you log out from either the CLI or the Unity editor, the log-in information will be removed.

## Changing Beamable Environment

By default, Beamable packages are configured to use Beamable's production server environment, at `https://api.beamable.com`. If you want to target a different Beamable server environment, or a Private Cloud environment, you need to configure that when you log into Beamable within the Unity Editor.

![Beamable Environment Configuration](../../../../media/imgs/13b21da60da00575bde5e785017e19baa5f284be3d30c9a46bbe265f199b360a-image.png){width="300px"}
