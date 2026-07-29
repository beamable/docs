# MicroViews

A MicroView is a small web app that mounts into the [Beamable Console](./console.md) to add new pages and workflows. Anything the Console does not ship out of the box, such as live-ops tools, player dashboards, or content editors, you can add as a MicroView.

Every MicroView is a web bundle. The Console loads it, mounts it at a location you declare, and hands it a runtime `context` for talking to the Console and the Beamable SDK.

There are two ways to build one. Pick the guide that fits how you want to work.

- **[Build with React](./microviews-react.md)** is the fast path. Beamable ships a React template and a component library ([`@beamable/portal-toolkit`](https://www.npmjs.com/package/@beamable/portal-toolkit)) that match the Console's look. Start here if you are comfortable in React. We build standard Console pages this way
- **[The extension contract](./microviews-contract.md)** is the framework-agnostic path. Underneath, a MicroView is just a JavaScript bundle that follows a small contract. Read this to use another framework, no framework, or to understand what the React template does for you

Both paths hand your MicroView the same runtime `context`. See [Working with the context](./microviews-context.md) for the full reference on the Beam SDK, storage, site data, args, and the rest.

## Prerequisites

Before you build a MicroView you need:

- **A Beamable organization and workspace.** A MicroView is a project inside a Beamable workspace (the folder with a `.beamable` directory), created next to your microservices
- **The Beam CLI**, installed as a .NET tool. It scaffolds, runs, and deploys MicroViews
- **Node.js 22.14 or newer**, with npm. The template is a Vite and React 19 project

## Getting started

From your workspace, scaffold a new MicroView with:

```shell
beam project new portal-extension MyView
```

The CLI asks where the MicroView mounts (or pass `--mount-page` and `--mount-selector`) and creates a React project inside your workspace, next to your services. Continue in [Build with React](./microviews-react.md) to build, run, and [deploy](./microviews-react.md#deploying) it.
