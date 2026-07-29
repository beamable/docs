# Build a MicroView with React

Beamable ships a React template for MicroViews, plus a component library that matches the Console's look and theme. This is the fastest way to build a MicroView — we build standard Console pages (such as the players and analytics pages) this way. We strongly recommend using React for MicroViews, but if you need another library or framework, the [extension contract](./microviews-contract.md) can interoperate with it.

## Scaffold and run

1. Scaffold the template from your workspace: `beam project new portal-extension MyView`. The CLI asks where it mounts, or pass `--mount-page` and `--mount-selector` (add `--mount-group` and `--mount-label` for a full-page nav entry)
2. Install dependencies: `npm install`
3. Register it with the local CLI so the Console can find it: `beam project run --ids MyView`
4. Open the page in the Console

Always run your MicroView through `beam project run --ids <your-view>`. That command builds the bundle and registers it with the Console, which is what makes it discoverable. The `beam-build` script produces the deployable bundle (see the [extension contract](./microviews-contract.md#requirements) for what it emits).

!!! warning "Use the CLI to run, not `npm run dev`"

    The Vite dev server (`npm run dev`) builds the app but does not register it with the Console, so your MicroView never appears there. Run through `beam project run --ids <your-view>` instead.

### Choosing where it mounts

Valid mount points are defined by the Portal, not invented by you, so `beam project new portal-extension` reads the live list from the Console. Run it without `--mount-page` and `--mount-selector` and it walks you through a picker: first whether you are adding a **page** (a new route with its own sidebar entry) or a **component** (injected into an existing Console page), then the specific page and selector. Passing the flags skips the wizard, and the CLI validates them against the same list.

To browse the options yourself:

```sh
beam portal extension list-mount-sites
```

If you are authoring a brand-new mount site locally (for example in the in-browser sandbox), add `--ignore-validation` so the CLI accepts a page and selector the deployed Portal does not know about yet.

### Hot reload

While `beam project run` is active it watches your source and rebuilds the bundle on every save, so you do not re-run the command as you work. Reload the Console page to pick up the latest build.

## Three files

A MicroView is a normal Vite and React project. Three files carry the Beamable-specific wiring.

### vite.config.ts

```ts
import { definePortalExtensionConfig } from '@beamable/portal-toolkit/vite'

export default definePortalExtensionConfig({ entry: 'src/main.tsx', name: 'my-view' })
```

`definePortalExtensionConfig` handles the build details the Console expects: IIFE output, the `index.js` and `style.css` file names, and sharing React with the host.

### src/main.tsx

```tsx
import { registerReactExtension } from '@beamable/portal-toolkit/react'
import './app.css'
import App from './App'

registerReactExtension({ beamId: 'my-view', App })
```

`registerReactExtension` is the entry point. It mounts your `App` into the Console, wraps it in `StrictMode`, and handles teardown. `beamId` must match the `name` in your `package.json`.

`registerReactExtension` also takes:

- `getBadge`: supply a sidebar badge (see [Badges](#badges))
- `wrapper`: wrap `App` in your own providers (theme, query client, and the like)
- `disableStrictMode`: opt out of `StrictMode` (rarely needed)

### src/App.tsx

Your `App` receives the runtime `context` as its only prop.

```tsx
import { type ExtensionContext } from '@beamable/portal-toolkit'
import { BeamCard, BeamPageHeader } from '@beamable/portal-toolkit/react'

export default function App({ context }: { context: ExtensionContext }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <BeamPageHeader label="My Page" description="What this page is for." />
      <BeamCard>
        <div style={{ padding: '1.25rem' }}>Hello from my MicroView.</div>
      </BeamCard>
    </div>
  )
}
```

Two more files complete a TypeScript project: a standard `tsconfig.json`, and `src/vite-env.d.ts` with the toolkit's type augmentation, so the `beam-*` components typecheck.

```ts
/// <reference types="vite/client" />
import '@beamable/portal-toolkit/react'
```

`beam project new portal-extension` scaffolds all of these, so you rarely write them by hand.

## The context

`context` is your MicroView's connection to the Console. [Working with the context](./microviews-context.md) is the full reference; the fields you reach for most:

- `params`: route parameters matched from the mount's `page` pattern (see [Route params](#route-params))
- `navigate(path, opts?)`: move the Console to another route (see [Routes: realm-relative and absolute](#routes-realm-relative-and-absolute))
- `config`: portal-wide settings as observables (date range, theme, timezone, account)
- `realm` and `cid`: the realm and organization the MicroView runs under
- `mount`: the manifest entry that triggered this mount, so one bundle can serve several pages

### Routes: realm-relative and absolute

The Console addresses every page under the realm you have selected. A realm's full URL prefix is:

```
/<cid>/games/<gameId>/realms/<pid>/
```

where `<pid>` is the selected realm. Both `mount.page` (where your MicroView appears) and `context.navigate` (where you send the user) are written against that prefix, and the rule is the same for both:

- A path **without** a leading `/` is **realm-relative**. The Console prepends the prefix above, so the path resolves inside the selected realm. `players/list` becomes `/<cid>/games/<gameId>/realms/<pid>/players/list`. Switch realms and the same relative path now points into the new realm
- A path **with** a leading `/` is **absolute** to the domain. The Console uses it as-is, with no realm prefix. Reach for this only to leave the realm context, such as a login screen or an org-level page

```tsx
context.navigate('analytics/dashboard')             // realm-relative: stays in this realm
context.navigate('players/abc', { replace: true })  // realm-relative, replaces history
context.navigate('/auth/login')                     // absolute: leaves the realm
```

`replace: true` swaps the current history entry instead of pushing a new one, which suits redirects.

Prefer realm-relative paths. They keep your MicroView working across realms without hardcoding the current one, and they let a user switch realms without leaving your page.

### Route params

Write `mount.page` as a pattern. Dynamic segments use `:name`, and the matched values arrive on `context.params`:

- `players/:playerId` matching `.../players/abc` gives `context.params.playerId` of `abc`
- a trailing `*` is a wildcard: `players/list/:playerId/*` puts the matched tail on `context.params['*']`

```tsx
const playerId = context.params.playerId   // the ':playerId' segment
const tail = context.params['*']           // whatever matched the trailing '*'
```

A mount whose `page` has no params matches a fixed path, and `context.params` is empty. Child MicroViews mounted through a site (see [Composition and tabs](#composition-and-tabs)) also start with empty params unless their own `page` declares some.

### Reacting to portal config

`context.config` exposes observables for settings the user changes in the top bar. Read the current value with `.get()`, and subscribe to stay in sync. `.subscribe()` returns its unsubscribe function, so return it from an effect:

```tsx
import { useEffect, useState } from 'react'

function DateRangeLabel({ context }: { context: ExtensionContext }) {
  const [range, setRange] = useState(context.config.dateRange.get())
  useEffect(() => context.config.dateRange.subscribe(setRange), [context])
  return <p>Date range: {range}</p>
}
```

## Talking to the Beam SDK

Use the `useBeam` hook to get an authenticated Beam SDK client. It returns `null` until the SDK resolves, then re-renders with the instance. Calling it from your top-level `App` is normal:

```tsx
import { useBeam, BeamSpinner } from '@beamable/portal-toolkit/react'

function PlayerStats({ context }: { context: ExtensionContext }) {
  const beam = useBeam(context)
  if (!beam) return <BeamSpinner />
  const stats = beam.player.stats   // read-only getter, Record<string, string>
  return <pre>{JSON.stringify(stats, null, 2)}</pre>
}
```

`beam.player` exposes read-only getters like `id` and `stats`. To write data, or to read anything the getters do not expose, call the generated functions in `@beamable/sdk/api`, passing `beam.requester`:

```tsx
import { playersPostStatsByPlayerId } from '@beamable/sdk/api'

await playersPostStatsByPlayerId(beam.requester, beam.player.id, { set: { level: '7' } }, 'client', 'Public')
```

See [The Beam SDK](./microviews-context.md#the-beam-sdk) for the full data-access pattern, and [Which player?](./microviews-context.md#which-player) for the operator-vs-subject identity model. The raw promise is also on `context.beam` for use outside React.

### Calling your own microservice

To call your microservice's `[ClientCallable]` endpoints, generate a client with `beam portal extension add-microservice MyView MyService`, then register and call it. In React, do this inside an effect once `beam` is ready:

```tsx
import { useEffect, useState } from 'react'
import { useBeam, BeamSpinner } from '@beamable/portal-toolkit/react'
import { MyServiceClient } from '../beamable/clients/MyServiceClient'

function Score({ context }: { context: ExtensionContext }) {
  const beam = useBeam(context)
  const [score, setScore] = useState<number | null>(null)

  useEffect(() => {
    if (!beam) return
    beam.use(MyServiceClient)
    void beam.myServiceClient.getPlayerScore().then((r) => setScore(r.score))
  }, [beam])

  if (!beam) return <BeamSpinner />
  return <span>Score: {score ?? '…'}</span>
}
```

The microservice must be running (locally or deployed) for the call to resolve. See [Calling your microservice](./microviews-context.md#calling-your-microservice) for the full workflow.

!!! info "The SDK comes with the toolkit"

    You can import from `@beamable/sdk` and `@beamable/sdk/api` directly. The SDK installs automatically as a peer dependency of `@beamable/portal-toolkit`, so you do not add it to your `package.json`. If you call a microservice, list its BeamId in the manifest's `microserviceDependencies` (see the [manifest reference](./microviews-contract.md#the-manifest)).

## UI components

!!! tip "Browse every component live in the Console"

    The complete, always-current component gallery ships inside the Console.

    **React components:** open **[console.beamable.com/react-components](https://console.beamable.com/react-components)** for the full list of React components, their props, and live examples.

    **Not using React?** The same components are available as plain web components at **[console.beamable.com/components](https://console.beamable.com/components)**.

    Review these galleries before building UI. They are the authoritative reference for what exists and how each component is used.

`@beamable/portal-toolkit/react` ships a component library that already matches the Console's theme in light and dark. Reach for these before hand-rolling UI, so your MicroView looks native. A few common ones:

- Layout: `BeamPage`, `BeamPageHeader`, `BeamCard`, `BeamSectionLabel`
- Data: `BeamKpiRow`, `BeamKpiCard`, `BeamTable`, `BeamStatusPill`, `BeamRelativeTime`
- Input: `BeamButton`, `BeamInput`, `BeamSelect`, `BeamCheckbox`, `BeamSwitch`
- Feedback: `BeamSpinner`, `BeamCallout`, `BeamToast`, `BeamConfirmDialog`

A KPI row, as used on the players overview page:

```tsx
import { BeamKpiRow, BeamKpiCard } from '@beamable/portal-toolkit/react'

<BeamKpiRow>
  <BeamKpiCard value="892,461" label="Reachable Players" change="+4.3%" tone="positive" />
  <BeamKpiCard value="67.4%" label="Engagement Rate" change="+2.8%" tone="positive" />
  <BeamKpiCard value="41.2%" label="Retention (D30)" change="-0.8%" tone="negative" />
</BeamKpiRow>
```

The components are web components under the hood, so the Console's theme tokens (`--color-beam-accent`, `--color-beam-text-muted`, and the rest) cross into your MicroView. You rarely need to branch on theme yourself.

For the full list, use the in-Console galleries linked above; in your editor, the same components autocomplete from `@beamable/portal-toolkit/react`. You can still use plain HTML, your own CSS, and other React components or npm packages alongside them. Reach for the Beam components first so your MicroView stays visually native to the Console.

## Editing and saving

For screens that edit a set of rows and save them together, the toolkit ships a change tracker and a change bar that pair with an editable `BeamTable`. `useChangeTracker` holds a draft over a server baseline, computes the diff, and validates it; `<BeamChangeBar>` renders the pending changes with save and discard actions. This is the pattern the built-in player pages use.

```tsx
import {
  useChangeTracker, BeamChangeBar, BeamTable, BeamColumn, BeamInput,
} from '@beamable/portal-toolkit/react'

interface Row { rowKey: string; statKey: string; value: string }

function StatsEditor({ context, serverRows }: { context: ExtensionContext; serverRows: Row[] }) {
  const tracker = useChangeTracker<Row>({
    original: serverRows,                                  // the server baseline
    getKey: (r) => r.rowKey,
    isEqual: (a, b) => a.value === b.value,                // when is a row "modified"?
    validate: (r) => (r.statKey.trim() ? [] : [{ key: r.rowKey, field: 'key', message: 'Key required' }]),
  })

  // Project the tracker's diff into the shape BeamChangeBar renders.
  const changeSet = {
    added: tracker.changes.added.map((r) => ({ key: r.rowKey, label: r.statKey, value: r.value })),
    modified: tracker.changes.modified.map((m) => ({
      key: m.key, label: m.current.statKey, previousValue: m.original.value, value: m.current.value,
    })),
    deleted: tracker.changes.deleted.map((r) => ({ key: r.rowKey, label: r.statKey, value: r.value })),
    summary: tracker.changes.summary,
  }

  async function save() {
    if (!tracker.isValid) return
    const beam = await context.beam
    // ...persist tracker.changes via @beamable/sdk/api, then reset the baseline:
    tracker.applyOriginal(tracker.draft)
  }

  return (
    <>
      <BeamTable<Row> data={tracker.draft} rowKey={(r) => r.rowKey}>
        <BeamColumn<Row>
          field="value"
          header="Value"
          children={(row) => (
            <BeamInput
              value={row.value}
              onValueChange={(v: string) => tracker.updateItem(row.rowKey, (r) => ({ ...r, value: v }))}
            />
          )}
        />
      </BeamTable>
      <BeamChangeBar
        changes={changeSet}
        errors={tracker.errors}
        onWaSave={save}
        onWaDiscard={tracker.discard}
      />
    </>
  )
}
```

The tracker gives you `draft` (baseline plus edits), `isDirty`, `changes` (`added` / `modified` / `deleted` / `summary`), `errors`, and `isValid`, plus `updateItem`, `addItem`, `deleteItem`, `discard`, and `applyOriginal`. Drive `BeamChangeBar` from `changes`, gate `save` on `isValid`, and call `applyOriginal` with the fresh server data after a successful save.

## Where your MicroView appears

The `mounts` array in `package.json` declares where the MicroView shows up. Each entry's `page` is a realm-relative [route pattern](#routes-realm-relative-and-absolute); the Console mounts your MicroView wherever the current URL matches, and can add a sidebar entry. The [manifest reference](./microviews-contract.md#the-manifest) lists every field. In the players hub, two mount shapes cover most cases.

A **hub** is a top-level sidebar destination. Its `page` is a single segment with no `/`, so it sits directly under the realm: `players` resolves to `.../realms/<pid>/players`. The nav fields turn it into a sidebar entry:

```jsonc
{
  "page": "players",
  "selector": "#extension-page",
  "navLabel": "Players",
  "navIcon": "users",
  "navDescription": "Player profiles & lifecycle",
  "navColor": "var(--color-beam-cyan)"
}
```

A **sub-page** under a hub adds `navGroup` and ordering:

```jsonc
{
  "page": "players/players-overview",
  "selector": "#extension-page",
  "navGroup": "Insights",
  "navLabel": "Overview",
  "navIcon": "gauge",
  "navLabelOrder": 1
}
```

`selector: "#extension-page"` is the full-page mount: your MicroView owns the page body. `page` supports route params (`players/:playerId`), which arrive in `context.params`.

One bundle can declare several mounts. Each mount gets its own React tree and its own `context`, so branch on `context.mount` to serve different pages from one bundle.

### Styling the sidebar entry

For a hub or any full-page mount, the `nav*` fields control its sidebar presentation:

- `navLabel`: the text of the entry
- `navGroup`: a heading to group the entry under. Sub-pages sharing a group stack together
- `navIcon`: an icon name (see below)
- `navDescription`: a short subtitle, shown in the hub picker
- `navColor`: the hub accent, any CSS color or gradient (for example `var(--color-beam-cyan)` or `linear-gradient(135deg, #826CCF, #04C6F1)`)
- `navGroupOrder` and `navLabelOrder`: integers that order groups and entries, lowest first

!!! info "Which icons `navIcon` accepts"

    Icon names are [Font Awesome](https://fontawesome.com/icons) names (the Console renders them through Web Awesome's `<wa-icon>`). Use the Free solid names, for example `users`, `gauge`, `chart-line`, `life-ring`, `gear`. The same names work in the `BeamIcon` component.

## Composition and tabs

A MicroView can host other MicroViews. Render a `<BeamExtensionSite>` to expose a slot, and any MicroView whose mount targets that slot (with `selector: "#<site-selector>"`) renders inside it. `mountKind` sets how multiple matches lay out:

- `additive` (default): stack every match
- `tabs`: render matches in a tab group with internal tab state
- `tabs-route`: render matches in a tab group where the active tab is driven by the URL, so tabs are deep-linkable

The player detail page uses `tabs-route`. The host renders the tab site:

```tsx
// players-detail, mounted at players/list/:playerId/*
<BeamExtensionSite selector="player-tabs" mountKind="tabs-route" />
```

Each tab is a separate MicroView that targets that site and declares its own URL:

```jsonc
// players-detail-engagement
{
  "page": "players/list/:playerId/engagement",
  "selector": "#player-tabs",
  "navLabel": "Engagement",
  "navIcon": "bullhorn",
  "navLabelOrder": 5
}
```

Clicking a tab navigates to that child's URL, so each tab is a real, linkable route. To mount one specific child by name instead of a whole site, use `<BeamChildExtension extensionName="...">`.

## Badges

A MicroView can put a badge on its sidebar item: a count, or a short label like `LIVE`. Badges come in four tones: `info` (cyan), `warning` (amber), `error` (red), and `accent` (purple). There are two ways to set one.

**Before the page is open**, supply `getBadge` to `registerReactExtension`. The Console calls it once per page load when the sidebar item scrolls into view, so the badge shows even if the user has never opened the page:

```tsx
registerReactExtension({
  beamId: 'players-tickets',
  App,
  getBadge: async (context) => {
    const openTickets = 3   // swap for a real SDK call
    return openTickets > 0 ? { value: openTickets, tone: 'warning' } : null
  },
})
```

`getBadge` runs before your `App` mounts, so it gets a narrow context (`realm`, `cid`, `beam`, `config`) and cannot touch the React tree.

**While the page is open**, call `context.updateBadge` to update the badge live. Pass `null` to clear it:

```tsx
context.updateBadge({ value: unread, tone: 'warning' })
context.updateBadge(null)
```

Use `getBadge` for the initial value and `updateBadge` to keep it current. A string value defaults to `accent` tone and a number to `info`.

## Deploying

A MicroView is part of your workspace's service manifest, exactly like a microservice, so it deploys the same way with no MicroView-specific step.

1. Plan the deployment to preview what will change: `beam deploy plan`
2. Release it: `beam deploy release`

`beam deploy release` publishes everything in the manifest to the current realm, and the MicroView appears in that realm's Console. The same realm rules as your services apply: release to a staging realm first, then promote. Because a MicroView travels with your services, one release can ship a microservice and the MicroView that fronts it together.

## Troubleshooting

- **It does not appear in the Console.** Confirm you ran `beam project run --ids <your-view>` (not `npm run dev`), that the run is still active, and that `beamId` in `registerReactExtension` matches the `name` in `package.json`. Check that `--mount-page` and `--mount-selector` are valid with `beam portal extension list-mount-sites`
- **Type errors on `beam-*` components or `<BeamX>` props.** Add `src/vite-env.d.ts` with `import '@beamable/portal-toolkit/react'` (see [Three files](#three-files))
- **A microservice call fails.** The service must be running (locally with `beam project run --ids <service>`, or deployed) and listed in `microserviceDependencies`. Regenerate the client with `beam portal extension add-microservice` after endpoint changes
- **Blank page after it mounts.** Check the browser console for a runtime error in your `App`, and confirm the build produced `assets/index.js` and `assets/style.css`
