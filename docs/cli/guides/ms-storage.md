# Microservice storage

Add database storage to Beamable Standalone Microservices

## Dependencies

Before you can use Beamable Storage Objects, you need to complete the [Getting-Started Guide](getting-started.md). That means having [.NET 10](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) installed, and getting the [Beam CLI](https://www.nuget.org/packages/Beamable.Tools).

You can confirm you have everything installed checking the versions of the tools.
```shell
dotnet --version
dotnet beam version # dotnet beam --version also works.
```

In order to use a Storage Object, you also need to have a local `.beamable/` workspace with a Beamable Standalone Microservice. As a reminder, you can create one quickly using the commands below.
```shell
beam init MyProject
cd MyProject
dotnet beam project new service HelloWorld
```

## Storage objects

A Storage Object is a MongoDB database. Beamable will host and manage a database on your behalf when you deploy your project. Locally, the Beam CLI creates a local mongo database inside a Docker container. Beamable never installs mongo directly on your host machine.

To create a Storage Object, use the [project new storage](ms-workflow.md#creating-new-projects) command.

```shell
dotnet beam project new storage
```

This creates a new `.csproj` in your existing `.sln`. You will also be prompted to assign a reference between the Storage Object and some Microservices. A Storage Object cannot exist independently of a Microservice. When you specify a dependency between a Storage Object and a Microservice, Beamable knows to pass the connection credentials to the Microservice.

When developing locally, anytime a Microservice that depends on a Storage Object starts, it will make sure the Docker container for the Storage Object is running. If there is no running container, it will start a container. This can take several seconds and it may appear the service is failing to start.

The code documentation explains how to interact with a Storage Object.

## Storage objects and Common Libraries

!!! warning "Keep storage types out of Common Libraries"
    Storage object types (`MongoStorageObject` subclasses) and the MongoDB-serialized document types they persist (types using `[BsonElement]`, `[BsonId]`, and other `MongoDB.Bson` attributes) must live in your microservice or storage project, not in a shared Common Library (`dotnet beam project new common-lib`). A Common Library references only `Beamable.Common` — it has no MongoDB dependency, so these types will not compile there. Adding a `MongoDB` package reference to the Common Library is not a fix: the library is copied into every linked Unity project, and Unity has no MongoDB driver (only a small set of mock Bson attributes), so the build breaks. Share plain data contracts (DTOs, enums) through the Common Library; keep storage objects and their documents server-side.

A data transfer object (DTO) is a plain contract you share with the client through the Common Library. It references nothing beyond `Beamable.Common`, so it compiles both server-side and in Unity:

```csharp
[Serializable]
public class PlayerLoadout
{
    public string WeaponId;
    public int[] PerkIds;
}
```

A data storage object (DSO) is the record you persist. It derives from `StorageDocument` and can carry `MongoDB.Bson` attributes and server-only fields, so it stays in the microservice or storage project:

```csharp
public class PlayerRecord : StorageDocument
{
    [BsonElement("loadout")]
    public PlayerLoadout Loadout { get; set; }

    [BsonElement("bannedUntil")]
    public long BannedUntilTicks { get; set; }
}
```

There is no shared base class between the two. Every type you store is constrained to `StorageDocument`, so a DSO must derive from it; because C# permits a single base class, a DSO cannot also inherit a DTO, and a DTO cannot derive from `StorageDocument` without pulling `MongoDB.Bson` into the Common Library. Prefer composition: give the DSO a field of the DTO type — as `PlayerRecord.Loadout` does above — keeping the shared shape in the Common Library and the storage concerns server-side.
