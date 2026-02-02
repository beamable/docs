# Microstorages

Beamable Microstorages are MongoDB databases that integrate seamlessly with Beamable Microservices to provide powerful custom state management solutions. Microstorages have a C# project written in dotnet that _represents_ the storage database. This C# project is used as identity, and can be a place to put data related code, such as model types. Beamable Microservices can access storage objects through the `Storages` accessor.

## Getting Started

The gist of a common example Microstorage and Microservice is below.

**UserDataStorage**

A custom child of `MongoStorageObject` is defined to wrap the database. The `UserMessage` is added as the high-level object to be stored in the database.

UserDataStorage.cs
```csharp 
using Beamable.Server;
using MongoDB.Bson;

namespace Beamable.Server
{
    [StorageObject("UserDataStorage")]
    public class UserDataStorage : MongoStorageObject
    {

    }

    public class UserMessage
    {
        public ObjectId Id;
        public string Message;
        public int X;
        public int Y;
    }
}
```

**UserDataService**

The Beamable Microservice `UserDataService` is created to wrap all calls to the database.

See [Microservices](doc:microservices-feature-overview) for more info.

UserDataService.cs
```csharp 
using System;
using System.Collections.Generic;
using System.Linq;
using MongoDB.Driver;
using UnityEngine;

namespace Beamable.Server
{
   [Microservice("UserDataService")]
   public class UserDataService : Microservice
   {
      [ClientCallable]
      public async Promise<bool> SaveMessage(string message, int x, int y)
      {
         bool isSuccess = false;

         try
         {
            var db = await Storage.GetDatabase<UserDataStorage>();
            var collection = db.GetCollection<UserMessage>("messages");
            collection.InsertOne( new UserMessage()
            {
               Message = message,
               X = x,
               Y = y
            });
            
            isSuccess = true;
         }
         catch (Exception e)
         {
            Debug.LogError(e.Message);
         }

         return isSuccess;
      }
      
      [ClientCallable]
      public async Promise<List<string>> GetMessage(int x, int y)
      {
         var db = await Storage.GetDatabase<UserDataStorage>();
         var collection = db.GetCollection<UserMessage>("messages");
         var messages = collection
            .Find(document => document.X == x && document.Y == y)
            .ToList();

         return messages.Select(m => m.Message).ToList();
      }
   }
}
```

**UserDataMicroServiceExample**

UserDataMicroServiceExample.cs
```csharp 
using System.Collections.Generic;
using UnityEngine;
using Beamable.Server.Clients;

namespace Beamable.Examples.Features.Microservices.UserDataMicroServiceExample
{
    /// <summary>
    /// Demonstrates <see cref="Microservices"/>.
    /// </summary>
public class UserDataMicroServiceExample : MonoBehaviour
{
    //  Properties  -----------------------------------
        
    //  Fields  ---------------------------------------
    private UserDataServiceClient _userDataServiceClient = null;
        
    //  Unity Methods  --------------------------------

    protected void Start()
    {
        Debug.Log("Start() Instructions...\n" + 
        "* Complete docker setup per https://docs.beamable.com/docs/microservices-feature-overview\n" +
        "* Start the server per https://docs.beamable.com/docs/microservices-feature-overview\n" +
        "* Play This Scene\n" + 
        "* View the Unity Console output\n" + 
        "* Enjoy!\n\n\n");
            
        SetupBeamable();
    }
        
        //  Methods  --------------------------------------
        private async void SetupBeamable()
        {
            var beamContext = BeamContext.Default;
            await beamContext.OnReady;

            Debug.Log($"beamContext.PlayerId = {beamContext.PlayerId}");
            
            _userDataServiceClient = new UserDataServiceClient();
            
            // #1 - Call Microservice
            bool isSuccess = await _userDataServiceClient.SaveMessage("Hello World!", 0, 0);
                
            // #2 - Result = true
            Debug.Log ($"SaveMessage() isSuccess = {isSuccess}");
            
            // #3 - Call Microservice
            List<string> messages = await _userDataServiceClient.GetMessage(0, 0);
                
            // #4 - Result = true
            Debug.Log ($"GetMessage() messages.Count = {messages.Count}, messages[0] = {messages[0]}");
        }
    }
}
```

## MongoCrudExtensions API

To make interactions with mongo storage feature easier and more affordable we've introduced `MongoCrudExtensions` class that contains following methods:

- Get 
- Create
- Update
- Delete

In the example, there is a `TestDocument` storage document as described below.

TestDocument.cs
```csharp 
namespace Beamable.Server
{
	public class TestDocument : StorageDocument
	{
		public int IntValue;
		public string StringValue;
	}
}
```

The example targets the `TestStorage` StorageObject class.

TestStorage.cs
```csharp 
using Beamable.Common;
using MongoDB.Driver;

namespace Beamable.Server
{
	[StorageObject("TestStorage")]
	public class TestStorage : MongoStorageObject
	{
	}
}
```

Then, in a Microservice, the `TestDocument` can be created, read, updated, and deleted as shown below.

TestMicroservice.cs
```csharp 
using Beamable.Mongo;
using Beamable.Server;
using MongoDB.Driver;
using System.Collections.Generic;

namespace Beamable.Microservices
{
	[Microservice("TestMicroservice")]
	public class TestMicroservice : Microservice
	{
		[ClientCallable]
		public async void Get(string id)
		{
			TestDocument document = await Storage.Get<TestStorage, TestDocument>(id);
		}

		[ClientCallable]
		public async void Create(int intValue, string stringValue)
		{
			await Storage.Create<TestStorage, TestDocument>(new TestDocument
			{
				IntValue = intValue, StringValue = stringValue,
			});
		}

		[ClientCallable]
		public async void Update(string id, int intValue, string stringValue)
		{
			await Storage.Update<TestStorage, TestDocument>(id, new TestDocument
			{
				IntValue = intValue,
				StringValue = stringValue
			});
		}

		[ClientCallable]
		public async void Delete(string id)
		{
			await Storage.Delete<TestStorage, TestDocument>(id);
		}
	}
}
```

!!! info "The Collection Name is the Class Name"

    When you use these helper methods, the Mongo Collection for the `TestDocument` class will be called `"TestDocument"`.
