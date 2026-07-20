# Beamable Toolkit

The Beamable Toolkit lets you extend the [Beamable Console](console.md) with your own web apps, called **MicroViews**. Use it to add pages, dashboards, and live-ops tools built on your Beamable data and microservices, right inside the Console your team already uses.

## Start here

- **[MicroViews](microviews.md)**: what a MicroView is and the two ways to build one
- **[Build with React](microviews-react.md)**: the fast path, using the React template and component library
- **[The extension contract](microviews-contract.md)**: the framework-agnostic bundle contract, for any framework or none
- **[Working with the context](microviews-context.md)**: the runtime API every MicroView receives, covering the Beam SDK, routing, config, badges, and calling your own microservice
- **[Toolkit](toolkit.md)**: the `@beamable/portal-toolkit` package

## Quickstart

From your Beamable workspace:

```sh
beam project new portal-extension MyView
beam project run --ids MyView
```

Then open your MicroView in the Console. See [Build with React](microviews-react.md) for the full walkthrough, from scaffolding through [deploying](microviews-react.md#deploying).
