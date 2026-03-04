# Web Access Sample

The project linked from this page is an example of how to use Beamable APIs in a webpage context: HTML and Javascript.

## Quick Start

The example code in <https://github.com/beamable/BeamWebAccess-example> is pointed at the `BeamWebAccess-prod` realm, as described below. You can start testing with it without making any changes. You can read more on [GitHub](https://github.com/beamable/BeamWebAccess-example)

1. Clone the `BeamWebAccess-example` repository
2. Point a web browser at `web/index.html`
3. Use the Guest Login button to create a guest account
4. Try out the forms below the login area

The "Display Name" and "Avatar" portion of things uses `client.public` stats, which can be written and read by anyone who has a valid access token. The "Dice" portion of the page uses a Beamable C# Microservice to interact with `game.private` stats, which are only readable and writable by admins and privileged processes. C# Microservices are a good way to mediate access to privileged resources, using logic that you define when writing the C#MS.

## Testing your own realms

As shipped in this repository, the example code is hardcoded to use a Beamable staff CID and PID (1418422019508250 and DE_1719820960373762, respectively). You may freely try out the code in this realm, but if you want to make significant changes, such as modifying the C# microservice, you should switch to a realm that you control. The CID and PID are encoded in two places; you should change them in both.

- In `Assets/Beamable/Resources/config-defaults.txt` you should modify three fields: `"cid"`, `"alias"`, and `"pid"`. You can find the proper values for these in the config-defaults.txt of any other Beamable project that you have created on your own.
- In `web/index.html` you should modify the constants `beam_cid` and `beam_pid` to match your own realm.

!!! info "BeamWebAccess Unity project is a Stub"

    Because the primary purpose of this repo is to demonstrate web-based interaction with Beamable, the Unity project in the `Assets/` directory is just there to serve as a reminder that `config-defaults.txt` exists and as a jumping off point for Unity-based testing if needed.
