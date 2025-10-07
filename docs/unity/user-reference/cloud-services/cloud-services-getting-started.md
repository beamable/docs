---
title: "Getting Started"
slug: "getting-started"
excerpt: ""
hidden: false
createdAt: "Fri Nov 08 2024 02:43:41 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Sat Nov 09 2024 15:26:05 GMT+0000 (Coordinated Universal Time)"
---
When you need to write server authoritative code, Beamable Microservices are a good choice. 

<br />

## Setting Up

Before you can get started creating a new Microservice, you should make sure the following steps are complete.

1. Install the Beamable SDK into your Unity project. If you haven't done this yet, check the [Installing Beamable (Unity)](doc:installing-beamable). Make sure you install the SDK with version 2.0 or higher.
2. Log into a Beamable organization inside the Unity SDK. 
3. Install Docker on your system. Docker is an industry standard tool for bundling code into distributable packages. You can download DockerHub from their website, <https://www.docker.com/products/docker-desktop/>. If you forget this step, the _Beam Services_ window in the Unity SDK will prompt you to install Docker later. 
   > 📘 You do not need a Docker account
   > 
   > Docker's website and DockerHub software will to convince you to create an account with Docker. You may eventually need to create an account for other reasons, but you _do not_ need an account to get started with Beamable Microservices.

<br />

## Creating your first Microservice

To create a Microservice, open the _Beam Services_ window in Unity by clicking the _Beamable Button_ and selecting _Open Beam Services_. 

If your Unity project does not have any Microservices yet, then the _Beam Services_ window will automatically prompt you to create one. If there is already an existing service and you want to create a new one, click on the _Create_ button at the top of the window and select, _Service_. You need to enter a valid service name, and then click the _Create Service_ button. 

> 🚧 Service names must follow conventional variable naming
> 
> The name of the service will be used in various generated code and therefore must follow normal variable naming conventions. It must start with a letter, and can only contain alpha-numeric characters (plus underscores).

After the Microservice has been created, the _Beam Services_ window will focus on the service, showing the logs of the service and various buttons to interact with the service. Refer to the [Beam Services](doc:microservices-manager-overview) page for how to navigate the _Beam Services_ window.

When you open the code for the new service (using the folder icon button), you will see the standard boilerplate Beamable Microservice code snippet. 

```csharp
using Beamable.Server;

namespace Beamable.DemoService
{
	[Microservice("DemoService")]
	public partial class DemoService : Microservice
	{
		[ClientCallable]
		public int Add(int a, int b)
		{
			return a + b;
		}
	}
}
```

Before you start the service, make sure to change your Realm to a non-production realm. 

> ❗️ Be careful running local Microservices on production realms!
> 
> Beamable _Realms_ are environments for your game to use and usually there are at least three, one for development, one for staging, and one for production. If you run a local Microservice on the production realm, there is a _risk_ that the service could tamper with your production environment.  By default, Beamable will prevent the local service from receiving web traffic on a production Realm. To override this, see the [Handling Requests](doc:handling-requests)page.

Back in Unity, in the _Beam Services_ window, press the play button to start the service. You can also run the service directly from your IDE using the IDE's play or debugging buttons. Log messages will appear in the _Beam Services_ window, and eventually when the service has successfully initialized, this log message will appear. 

```
Service ready for traffic
```

<br />

Congratulations! You have a locally running Microservice!

<br />

## Testing the Microservice

As you write Microservices, you need to test the code you are writing. This is done is a few ways, through in-game testing, and by manually calling the Microservice methods from the auto generated Portal testing page. The easiest way to check your Microservice methods is to use the Portal testing page. In the _Beam Services_ window, click the globe icon in the top-right of the Microservice log section. This will open the Beamable Portal website to a section directly targeting your locally running Microservice. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/eda82702b8514572f20d3a4ec98cc122d82025d46e7ec74e154a8f20869b8f74-image.png",
        null,
        "The auto generated Portal testing page for your Microservice "
      ],
      "align": "center",
      "sizing": "50% ",
      "caption": "The auto generated Portal testing page for your Microservice "
    }
  ]
}
[/block]


You can use this UI to send sample web requests to your Microservice. To learn more about testing the Microservice from your Unity game, check out the [Calling Microservices from Unity](doc:calling-microservices-from-unity) section.
