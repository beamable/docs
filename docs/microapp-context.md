# Working with the context

Every MicroView receives an `ExtensionContext`. It is your MicroView's connection to the Console: identity, the Beam SDK, routing, portal settings, storage, and more. You get the same object no matter how you built the MicroView:

- In the [React template](./microapp-react.md), it arrives as the `context` prop on your `App`
- With the [raw contract](./microapp-contract.md), it is the second argument to `onMount`

This page is the reference for what is on the context and how to use each part. Examples are framework-neutral; where the React toolkit offers a shortcut (such as `useBeam`), that is called out.

```ts
import { type ExtensionContext } from '@beamable/portal-toolkit'
```

## Identity

- `realm`: the selected realm (its `pid`)
- `cid`: the organization (customer) id

Both are plain strings, available synchronously. Use them for display, logging, or to scope your own data. Anything that needs authenticated calls goes through the [Beam SDK](#the-beam-sdk).

## The Beam SDK

`context.beam` is a promise that resolves to an authenticated Beam SDK client for the current realm. Await it once:

```ts
const beam = await context.beam
```

In React, prefer the `useBeam` hook. It returns `null` until the client resolves, then re-renders with it:

```tsx
import { useBeam, BeamSpinner } from '@beamable/portal-toolkit/react'

function Widget({ context }: { context: ExtensionContext }) {
  const beam = useBeam(context)
  if (!beam) return <BeamSpinner />
  return <span>Realm {beam.pid}</span>
}
```

The client gives you two ways to reach the backend:

- **Convenience getters** on `beam.player` (a read-only `PlayerService`): `beam.player.id`, `beam.player.stats`, and similar. Good for a quick read. You cannot write through them
- **Generated API functions** in `@beamable/sdk/api`, one per backend endpoint. Each takes `beam.requester` as its first argument. This is how you write, and how you read anything the getters do not expose

Reading and writing a player's stats, for example:

```ts
import { playersGetStatsByPlayerId, playersPostStatsByPlayerId } from '@beamable/sdk/api'

const beam = await context.beam
const playerId = beam.player.id

// read the current player's client/public stats
const resp = await playersGetStatsByPlayerId(beam.requester, playerId, 'client', undefined, 'Public')
const stats = (resp.body as { stats?: Record<string, unknown> }).stats ?? {}

// write one back
await playersPostStatsByPlayerId(beam.requester, playerId, { set: { level: '7' } }, 'client', 'Public')
```

The trailing `domain` and `visibility` arguments pick which stat bucket you touch. `domain` is `client` (player-writable) or `game` (server-authoritative); `visibility` is `Public` or `Private`. Player-facing reads and writes are usually `client` and `Public`.

!!! info "The SDK comes with the toolkit"

    You can import from `@beamable/sdk` and `@beamable/sdk/api` directly. The SDK installs automatically as a peer dependency of `@beamable/portal-toolkit`, so you do not add it to your `package.json`.

### Which player?

The Console is an operator tool, so "the player" depends on the situation:

- `beam.player` is the **signed-in operator's** player in the current realm. `beam.player.id` is their realm-scoped id (gamertag)
- a page that inspects **another** player takes that player from a route param, for example a mount at `players/list/:playerId` read as `context.params.playerId`. That value is usually an **account id**, which is stable across realms
- stats and most per-player data are keyed by the **realm-scoped gamertag**, not the account id. When you start from an account id, resolve the gamertag first (with `accountsGetFindBasic`) before calling player-scoped endpoints

To call your own microservice's endpoints (not just the built-in APIs), see [Calling your microservice](#calling-your-microservice).

## Calling your microservice

The examples above use Beamable's built-in APIs. To call your own microservice's `[ClientCallable]` endpoints, you generate a typed client, register it, and call it. The service must be running for the calls to resolve.

### 1. Generate a client

From your workspace, add the microservice as a dependency of your MicroView:

```sh
beam portal extension add-microservice MyView MyService
```

This does two things:

- adds `MyService`'s BeamId to your MicroView's `microserviceDependencies` (see [the manifest](./microapp-contract.md#the-manifest))
- generates a typed client into `MyView/beamable/clients/`, one method per `[ClientCallable]` endpoint

The microservice must already exist in your workspace and have been built at least once, so the CLI can read its endpoints. Re-run the command to regenerate after you change endpoints; do not hand-edit the generated file.

### 2. Register and call it

The generated client is named `<ServiceName>Client` (for example `MyServiceClient`). Register it on the resolved `beam` with `use`, then call it through `beam.<serviceName>Client` (the class name, camel-cased):

```ts
import { MyServiceClient } from '../beamable/clients/MyServiceClient'

const beam = await context.beam
beam.use(MyServiceClient)

const score = await beam.myServiceClient.getPlayerScore()
await beam.myServiceClient.submitScore({ score: 42 })
```

Each method takes the endpoint's request body as its only argument (when it has one) and resolves to the response, already deserialized.

### 3. Run the microservice

Calls resolve only when the service is running, either locally with `beam project run --ids MyService` or deployed to your realm. While developing, run the MicroView and its microservice together.

!!! info "What the generated client looks like"

    Each endpoint becomes an async method that forwards to the host. You import and call it; you do not write or edit it.

    ```ts
    // MyView/beamable/clients/MyServiceClient (generated)
    import { BeamMicroServiceClient } from '@beamable/sdk'

    export class MyServiceClient extends BeamMicroServiceClient {
      get serviceName() { return 'MyService' }

      async getPlayerScore() {
        return this.request({ endpoint: 'GetPlayerScore', withAuth: true })
      }
      async submitScore(params) {
        return this.request({ endpoint: 'SubmitScore', payload: params, withAuth: true })
      }
    }
    ```

## Mount and args

`context.mount` is the manifest entry that triggered this mount: its `page`, `selector`, nav fields, and `args`. Read it to branch when one bundle serves several mounts.

`context.mount.args` is an arbitrary object you set on the mount entry in the manifest. It is static, declared by the author, and handed straight back at runtime. Use it to render the same bundle differently at different mount points.

```jsonc
// package.json: two mounts of one bundle, distinguished by args
"mounts": [
  { "page": "orders", "selector": "#extension-page", "args": { "mode": "list" } },
  { "page": "orders/archive", "selector": "#extension-page", "args": { "mode": "archive" } }
]
```

```ts
const mode = context.mount.args?.mode   // 'list' or 'archive'
```

`args` is fixed by the manifest. For data passed in at runtime by a parent MicroView, see [Site data](#site-data).

## Routing

- `params`: route parameters matched from the mount's `page` pattern. A mount at `players/:playerId` viewing `.../players/abc` gives `context.params.playerId` of `abc`. A trailing `*` wildcard lands on `context.params['*']`
- `location`: a read-only snapshot of the URL at mount time (`pathname`, `search`, `hash`). It does not update after mount; read `window.location` or listen for `popstate` if you need live URL changes
- `navigate(path, opts?)`: move the Console to another route. A path with no leading `/` is realm-relative; a leading `/` is absolute to the domain

The realm-relative vs absolute rule (and the full realm URL prefix) is covered in [Routes: realm-relative and absolute](./microapp-react.md#routes-realm-relative-and-absolute).

## Portal config

`context.config` exposes portal-wide settings as read-only observables. Each has `.get()` for the current value and `.subscribe(handler)` to react to changes; `.subscribe` returns its unsubscribe function.

- `dateRange`: the active range from the top bar
- `timezone`: the user's IANA zone, or the literal `local`
- `theme`: `dark` or `light`
- `account`: the signed-in identity (`{ id, email, role }`), or `null`

```ts
const range = context.config.dateRange.get()
const unsubscribe = context.config.dateRange.subscribe((next) => {
  // react to the new range
})
```

Subscribing keeps your MicroView in step with the rest of the Console. Extensions never write back through `config`; it is read-only.

## Site data

When a MicroView is mounted inside another through a [mount site](./microapp-react.md#composition-and-tabs), the parent can hand it data. The child reads it from `context.siteData`.

`siteData` is a snapshot taken at mount time. Mutating the parent's value afterward does not update an already-mounted child; a remount picks up the new value. For a child that stays in sync with live changes, the parent passes a store (a handle with `get()` and `subscribe()`) and the child subscribes to it.

`context.siteData` is typed as `unknown`, because a mount site is a generic slot and the type system cannot know a given site's contract. Validate it at the receiving end with a companion type, a schema, or a defensive cast.

Use `args` for values fixed by your own manifest, and `siteData` for values a parent supplies at runtime.

## Storage

`context.storage` gives each MicroView persistent key/value storage. Every value is isolated to this MicroView and the signed-in account, so you never collide with another MicroView or another user.

A value's location has three parts. You pick the **tier** explicitly; the **scope** and **mount** default unless you override them:

- **tier** (`session` or `local`): `session` clears when the tab or session ends; `local` stays on the device and survives reloads
- **scope** (`pid` or `cid`): `pid` (default) keeps the value to the current realm; `cid` shares it across every realm in the org
- **mount** (`all` or `instance`): `all` (default) shares one value across every mount of the MicroView; `instance` keeps a separate value per mount site

Each tier is itself a store. Calling `get` / `set` / the rest on it directly uses the default location, `scope: 'pid'` and `mount: 'all'`. To use a different scope or mount, call `.scope({ scope, mount })`, which returns a store bound to that location. These two writes are identical:

```ts
context.storage.local.set('k', v)
context.storage.local.scope({ scope: 'pid', mount: 'all' }).set('k', v)  // same location
```

That is why the examples below can call `.set()` straight on a tier: they are writing to the default `pid` + `all` location. Reach for `.scope()` only to deviate. Every method is asynchronous:

```ts
// session tier, default location (pid + all): this realm, shared across mounts, TTL 30s
await context.storage.session.set('token', value, { ttl: 30_000 })

// local tier, default location: per-realm, this device, survives reloads
await context.storage.local.set('lastFilter', filter)
const filter = await context.storage.local.get<Filter>('lastFilter')

// local tier, org-wide: one value shared across every realm (scope override)
await context.storage.local.scope({ scope: 'cid' }).set('compact', true)
```

`get` returns `null` when a key is absent or its TTL has elapsed. The other methods are `set`, `remove`, `keys`, `clear`, and `subscribe(key, handler)`. A TTL is evaluated lazily: an entry is dropped on the first read after it expires.

## Badges

`context.updateBadge` sets the MicroView's sidebar badge while it is mounted. Pass a value to set it, or `null` to clear it:

```ts
context.updateBadge({ value: unread, tone: 'warning' })
context.updateBadge(null)
```

A badge is a count or a short label in one of four tones (`info`, `warning`, `error`, `accent`). To show a badge before the page is ever opened, supply a `getBadge` callback at registration instead; see [Badges](./microapp-react.md#badges).

## Discovering mount-site candidates

If your MicroView exposes a [mount site](./microapp-react.md#composition-and-tabs) for others to fill, `context.getMountSiteCandidates(selector)` returns a reactive list of the MicroViews that could mount there, each with its `beamId`, matched `mount` entry, toolkit version, and whether it is running locally. Subscribe to react as candidates deploy, enable, or disable. Use it to build UI such as a "which view" picker, or to compute which children to render.
