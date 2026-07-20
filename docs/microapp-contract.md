# The MicroView extension contract

A MicroView is a JavaScript bundle that the Console loads and mounts. The [React template](./microapp-react.md) is one way to produce that bundle, but nothing about the contract requires React. This page describes the contract itself, so you can build a MicroView with any framework or none, and understand what the React toolkit does under the hood.

## Requirements

Every MicroView must satisfy four requirements:

1. An npm project whose `package.json` has a `beam-build` script. Running it must emit an [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) bundle at `assets/index.js` and a stylesheet at `assets/style.css`
2. A `beamable` block in `package.json` (the manifest) that marks the project as a MicroView and declares where it mounts (see [The manifest](#the-manifest))
3. A dependency on [`@beamable/portal-toolkit`](https://www.npmjs.com/package/@beamable/portal-toolkit). It brings in `@beamable/sdk` as a peer dependency, so backend calls need no extra dependency (see [The Beam SDK](./microapp-context.md#the-beam-sdk))
4. An entry module that registers the MicroView with `Portal.registerExtension` (see [Registering](#registering))

!!! info "Build tools are your choice"

    Beamable's template uses [Vite](https://vite.dev) to satisfy the `beam-build` contract, and `@beamable/portal-toolkit/vite` wraps the config. Vite is not required. The requirement is the output: an IIFE `assets/index.js` and an `assets/style.css`.

## The manifest

The `beamable` block in `package.json` tells the Console the MicroView exists and where it belongs:

```jsonc
{
  "beamable": {
    "version": "1.0.0",
    "portalExtension": true,        // marks this project as a MicroView
    "serviceGroups": ["my-hub"],    // optional: groups related MicroViews (usually the hub)
    "microserviceDependencies": [], // BeamIds of microservices this view calls
    "mounts": [
      {
        "page": "my-hub/my-page",   // realm-relative URL pattern; supports :params
        "selector": "#extension-page",
        "args": {},                 // arbitrary data passed to the mount on context.mount
        "navGroup": "My Hub",       // sidebar group label
        "navLabel": "My Page",      // sidebar item label
        "navIcon": "robot",
        "navLabelOrder": 1
      }
    ]
  }
}
```

Each entry in `mounts` is matched independently against the current URL. The mount fields:

- `page`: the URL pattern, matched after the realm prefix. Supports route params like `players/:playerId`
- `selector`: the DOM slot to render into. `#extension-page` is the full-page slot; a `#<name>` that matches another MicroView's site nests this one inside it
- `args`: arbitrary data handed back on `context.mount.args`, so one bundle can render differently per mount
- `navLabel`, `navGroup`, `navIcon`, `navDescription`, `navColor`, `navLabelOrder`, `navGroupOrder`: optional sidebar presentation. A single-segment `page` with these fields declares a hub

Alongside `mounts`, the top-level `serviceGroups` (optional) tags the MicroView as part of one or more named groups of related MicroViews, typically the hub it belongs to (for example `players`).

`microserviceDependencies` lists the BeamIds of the microservices this MicroView calls. Do not edit it by hand: run `beam portal extension add-microservice <view> <service>`, which adds the entry and generates a typed client for that service. See [Calling your microservice](./microapp-context.md#calling-your-microservice).

Like a microservice, a MicroView is tracked in your workspace's service manifest and ships with `beam deploy` (see [Deploying](./microapp-react.md#deploying)). The built `assets/` output is a build artifact, not source: the CLI regenerates it, so you do not commit it.

## Registering

The entry module registers the MicroView by calling `Portal.registerExtension`. This is what the React helper wraps.

```ts
import { Portal, type ExtensionContext } from '@beamable/portal-toolkit'

Portal.registerExtension({
  beamId: 'my-view',   // must match the package.json name
  onMount: (container, context: ExtensionContext) => {
    // container is already in the document; render into it
    container.innerHTML = `<p>Hello from ${context.realm}</p>`
    return {}          // return any handle you want back at unmount
  },
  onUnmount: (instance) => {
    // tear down listeners, timers, framework roots
  },
})
```

1. `onMount` runs when the Console inserts your MicroView. It receives the `container` element (already in the document) and the runtime `context`. Render into `container` and return a handle for teardown
2. `onUnmount` runs before removal. It receives the handle from `onMount`. The Console waits for a returned promise to settle before detaching `container`

Registration publishes the MicroView on `window[beamId]`, which the Console reads to drive mount and unmount. The React template's `registerReactExtension` is exactly this, with `createRoot`, `StrictMode`, and `unmount` filled in for you.

## The runtime context

Both `onMount` and, in React, your `App` receive an `ExtensionContext`. It carries:

- `realm` and `cid`: the realm and organization identifiers
- `beam`: a promise resolving to the authenticated Beam SDK client
- `params`: route parameters matched from the mount's `page` pattern
- `location`: a read-only snapshot of the URL at mount time (`pathname`, `search`, `hash`)
- `navigate(path, opts?)`: move the Console to another route. A leading `/` is absolute; otherwise the path is realm-relative
- `mount`: the manifest entry that triggered this mount
- `config`: portal-wide settings as read-only observables (`dateRange`, `timezone`, `theme`, `account`), each with `.get()` and `.subscribe()`
- `updateBadge(value)`: set the sidebar badge, or clear it with `null`

See [Working with the context](./microapp-context.md) for the full reference on each field, including the Beam SDK, storage, site data, and args.

## Badges

A MicroView can show a sidebar badge, a count or short label, in one of four tones (`info`, `warning`, `error`, `accent`). Set it two ways:

- **Pull**: pass a `getBadge` callback to `Portal.registerExtension`. The Console calls it once per page load when the sidebar item is in view, before the MicroView mounts. It receives a narrow context (`realm`, `cid`, `beam`, `config`) and returns a badge or `null`
- **Push**: call `context.updateBadge(value)` while mounted to update the badge live

```ts
Portal.registerExtension({
  beamId: 'tickets',
  onMount: (container, context) => { /* ... */ },
  onUnmount: (instance) => { /* ... */ },
  getBadge: async (context) => {
    const beam = await context.beam
    const count = await getOpenTicketCount(beam)
    return count > 0 ? { value: count, tone: 'warning' } : null
  },
})
```
