# Zoned microservices

A **zone** groups realms under a customer. Each realm can be bound to one zone (its `zoneId`), and a zone sits *above* those realms. A **zoned microservice** (zone-scoped microservice) runs once per `(cid, zid)`, for the whole zone, instead of once per realm like a standard [Microservice](microservices.md).

Reach for a zoned microservice when the logic belongs to the customer or spans realms, and is not tied to a single realm or player: cross-realm orchestration, customer-directory operations, and back-office or tooling logic that should exist once above your realms rather than being copied into each one.

## What a zone microservice is

- **Zone-scoped.** It is addressed as `cid.zid`, and one deployment serves the entire zone, across every realm bound to it
- **A different base class.** It inherits `ZoneMicroservice` instead of `Microservice`. The two are analogous, but the zone version deliberately omits the realm SDK
- **Above realms.** It has no realm and no player context. It can, on demand, step *into* a specific realm to use the full realm SDK (see [Working inside a realm](#working-inside-a-realm-with-assumerealm))
- **A separate manifest.** Zone services live in the zone manifest (`cid.zid`), deployed independently from your realm services (see [Deploy](#deploy))

## What a zone microservice is not

- **Not realm-scoped.** The realm accessors a `Microservice` exposes are intentionally absent: no `Services` (the realm SDK), no realm `Context` (there is no `Pid` or `UserId`), no `Requester`, `Storage`, `SignedRequester`, or on-behalf-of-a-player helpers. The base class is marked `[ZoneScoped]`, so registering it into a realm-scoped container is rejected, and reaching for a realm member through the interface throws
- **Not client-callable.** Game clients cannot call a zone service directly. A browser or game client cannot authenticate "as a zone", so endpoints are server-to-server. Use `[ServerCallable]`, not `[ClientCallable]`
- **Not per-realm.** It does not run once per realm. There is a single instance per zone
- **Not a replacement for realm microservices.** Player- and realm-scoped logic (inventory, stats, player data) still belongs in a standard [Microservice](microservices.md)

## Create a zone microservice

From inside a `.beamable/` workspace, pass `--zone` to the [project new service](ms-workflow.md#creating-new-projects) command:

```shell
dotnet beam project new service MyZoneService --zone
```

This uses the zone template: the project inherits `ZoneMicroservice` and its `.csproj` sets `<BeamServiceScope>zone</BeamServiceScope>`, which marks the service as zone-scoped in the manifest. The CLI reads that scope and boots the project as a zone service when you run or deploy it.

The scaffolded service looks like this:

```csharp
using Beamable.Server;

namespace Beamable.MyZoneService
{
    // A zone-scoped service runs once per (cid, zid), above realms. It has no player or
    // realm context, so it inherits ZoneMicroservice (not Microservice) and exposes no
    // realm SDK. Clients cannot call it directly, so use [ServerCallable] entry points.
    public partial class MyZoneService : ZoneMicroservice
    {
        [ServerCallable]
        public int Add(int a, int b)
        {
            return a + b;
        }
    }
}
```

## What you can use inside a zone service

A `ZoneMicroservice` exposes a small, zone-appropriate surface:

- **`Provider`**: the dependency provider for the request scope. Register your own services with the `[ConfigureServices]` attribute, exactly as you would in a realm `Microservice`
- **`Context`**: a `ZonedRequestContext`, the zone analog of the realm request context. It identifies the zone (`cid.zid`) and has no `Pid` or `UserId`
- **`Services.Customer`**: a read-only directory of the customer this zone belongs to:
    - `GetRealms()` lists every realm, including each realm's `zoneId` binding
    - `GetZones()` lists every zone
- **`AssumeRealm(pid, gamerTag = 0)`**: enter a realm and get the full realm SDK (see below)

```csharp
[ServerCallable]
public async Task<int> CountRealms()
{
    var realms = await Services.Customer.GetRealms();
    return realms.Count;
}
```

## Scoped dependency injection

A service's dependency container is built with a scope, `Realm` or `Zone`, taken from the `<BeamServiceScope>` in its `.csproj`. Two attributes declare where a service is allowed to live:

- `[RealmScoped]`: valid only in a realm (`cid.pid`) container
- `[ZoneScoped]`: valid only in a zone (`cid.zid`) container

A type with neither attribute is scope-neutral and may be registered in either scope. `ZoneMicroservice` is `[ZoneScoped]`, and the realm SDK services are realm-scoped, which is what keeps the two apart.

Enforcement is a fail-fast, boot-time guard. When the container is built, it scans every registration, and if any service's declared scope does not match the container's, it throws a single error listing every offender at once. A zone service that pulls in a realm-scoped service (or a realm service that pulls in a zone-scoped one) fails immediately at startup with a clear message, instead of surfacing as a null reference deep inside a request.

The realm accessors are not part of the `ZoneMicroservice` surface at all, so `Services`, `Context`, `Requester`, `Storage`, and the rest do not compile against a zone service. If code reaches one through the shared interface anyway, it throws for the same reason.

Services you register with `[ConfigureServices]` are scope-neutral by default and work in either scope. Annotate one with `[RealmScoped]` or `[ZoneScoped]` only when it genuinely belongs to a single scope, and the same boot-time guard enforces it.

## Working inside a realm with AssumeRealm

A zone service has no realm SDK of its own, but it can step into any realm in the customer and get the same dependency scope a realm `Microservice` would have. `AssumeRealm` is the zone-to-realm bridge.

```csharp
[ServerCallable]
public async Task DoWorkInRealm(string pid)
{
    // The handle owns its own realm-scoped child scope and is disposable.
    using var realm = AssumeRealm(pid);

    // realm.Services, realm.Requester, and realm.Provider are the realm-scoped SDK,
    // exactly what a realm Microservice would have for this pid.
}
```

- Pass the realm's `pid`. Optionally pass a `gamerTag` to act on behalf of a specific player; when it is `0` (the default), the scope acts with the service's own server identity
- The returned handle is **disposable** and owns a child scope, so wrap it in a `using` and let it dispose when the work is done

## Run it locally

Run a zone service the same way as any other, with [project run](ms-workflow.md):

```shell
dotnet beam project run --ids MyZoneService
```

The effective zone is resolved from your workspace. When a realm is selected, that realm's zone binding wins; when no realm is selected, the local zone id from your `.beamable/` [configuration](configuration.md) is used. A realm bound to no zone resolves to no zone.

## How the zid is derived

A zone service runs as `cid.zid`, so the CLI has to decide which zone your workspace is acting as. That resolution is centralized, so `beam config`, `project generate-env`, and the deploy path all agree:

1. **When a realm is selected**, the realm's zone binding is authoritative. The CLI reads the realm's `zoneId` from the platform, and it wins over any local value. A realm bound to no zone resolves to no zone, even if a local `zid` is set
2. **When no realm is selected**, the CLI uses the `zid` stored in your `.beamable` config

This is why a realm workspace stores no `zid` of its own (its zone follows the realm binding), while a pure zone workspace, which has no realm, carries a `zid` as its scope.

Check the resolved value with `beam config`. When the CLI builds the run environment for a zone service, it injects the resolved id as `ZID` and signs with the zone secret. If it cannot resolve one (no realm selected and no local `zid`, or the selected realm is bound to no zone), it stops and asks you to bind the realm to a zone or set a `zid` in the `.beamable` config.

## Deploy

Zone services are published to the zone manifest (`cid.zid`), which is separate from the realm manifest (`cid.pid`). The [deploy](ms-deployment.md) commands take a `--scope` option to choose which manifest to operate against:

```shell
# Plan and release the zone manifest (zone services only)
dotnet beam deploy plan --scope zone
dotnet beam deploy release --scope zone
```

`--scope realm` is the default and ignores zone-scoped services; `--scope zone` ignores all realm-scoped services and targets the zone manifest. Because the two scopes are separate manifests, you deploy realm services and zone services independently.

## How zone services are invoked

Zone services are a server-side surface. There are two ways to reach one:

- **Server-to-server**, through a service's `[ServerCallable]` endpoints
- **From operator tooling**, such as a Portal extension, which authenticates with an operator (customer-scoped) token rather than as a game client

If you need player- or client-facing endpoints, put them on a realm [Microservice](microservices.md) instead, and let that service (or your tooling) call into the zone service server-to-server.
