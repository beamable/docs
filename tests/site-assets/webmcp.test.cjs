const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const script = fs.readFileSync(path.join(__dirname, "../../site-assets/webmcp.js"), "utf8");
const origin = "https://help.beamable.com";
const index = { products: [{ name: "Unity", latest: "Unity-6.2", versions: [{
  version: "Unity-6.2", url: `${origin}/Unity-6.2/`, markdownUrl: `${origin}/markdown/Unity-6.2/index.md`,
  pages: [
    { path: "", url: `${origin}/Unity-6.2/` },
    { path: "guide/", url: `${origin}/Unity-6.2/guide/` }
  ]
}] }] };

async function environment({ supported = true, failFetch = false, rejectRegistration = false, data = index } = {}) {
  const tools = new Map(), listeners = {}, navigations = [], signals = [], warnings = [];
  let requests = 0;
  const context = {
    document: supported ? { modelContext: { registerTool(tool, options) {
      if (rejectRegistration) return Promise.reject(new Error("Unsupported draft"));
      tools.set(tool.name, tool);
      signals.push(options.signal);
      options.signal.addEventListener("abort", () => tools.delete(tool.name));
      return Promise.resolve();
    } } } : {},
    window: { addEventListener(name, callback) { listeners[name] = callback; } },
    location: { origin, assign(url) { navigations.push(url); } },
    fetch: async url => {
      requests++;
      assert.equal(url, "/agents/docs-index.json");
      return { ok: !failFetch, json: async () => data };
    },
    console: { warn(...message) { warnings.push(message); } },
    AbortController, URL
  };
  vm.runInNewContext(script, context);
  await new Promise(resolve => setImmediate(resolve));
  return { tools, listeners, navigations, signals, warnings, requests: () => requests };
}

test("unsupported browsers keep normal navigation and perform no fetches", async () => {
  const env = await environment({ supported: false });
  assert.equal(env.tools.size, 0);
  assert.equal(env.requests(), 0);
});

test("lists product versions and Latest using one shared fetch", async () => {
  const env = await environment();
  const tool = env.tools.get("list_documentation_versions");
  const result = await tool.execute({ product: "Unity" });
  assert.equal(result.products[0].latest, "Unity-6.2");
  assert.equal(result.products[0].versions[0].url, `${origin}/Unity-6.2/`);
  assert.equal(result.products[0].versions[0].pages, undefined);
  assert.equal((await tool.execute({ product: "Internal" })).error, "Unknown product");
  assert.equal(env.requests(), 1);
});

test("opens only indexed public pages and defaults to Latest/home", async () => {
  const env = await environment();
  const tool = env.tools.get("open_documentation");
  assert.equal((await tool.execute({ product: "Unity" })).url, `${origin}/Unity-6.2/`);
  assert.equal((await tool.execute({ product: "Unity", version: "Unity-6.2", path: "guide/" })).url, `${origin}/Unity-6.2/guide/`);
  for (const input of [
    { product: "Internal" }, { product: "Unity", version: "Unknown" },
    { product: "Unity", path: "../../Internal/" }, { product: "Unity", path: "https://evil.example/" },
    { product: "Unity", extra: true }, { product: 3 }, []
  ]) assert.ok((await tool.execute(input)).error);
  assert.equal(env.navigations.length, 2);
});

test("foreign URLs in a corrupt index cannot redirect the browser", async () => {
  const data = structuredClone(index);
  data.products[0].versions[0].pages[0].url = "https://evil.example/Unity-6.2/";
  const env = await environment({ data });
  assert.equal((await env.tools.get("open_documentation").execute({ product: "Unity" })).error, "Invalid documentation URL");
  assert.equal(env.navigations.length, 0);
});

test("index fetch failure is reported and a later call retries", async () => {
  const env = await environment({ failFetch: true });
  const tool = env.tools.get("list_documentation_versions");
  assert.equal((await tool.execute({})).error, "Documentation index is unavailable");
  assert.equal((await tool.execute({})).error, "Documentation index is unavailable");
  assert.equal(env.requests(), 2);
});

test("registration failures are caught", async () => {
  const env = await environment({ rejectRegistration: true });
  assert.equal(env.warnings.length, 2);
});

test("pagehide cleans up and bfcache restoration registers fresh signals", async () => {
  const env = await environment();
  env.listeners.pagehide();
  assert.ok(env.signals.every(signal => signal.aborted));
  assert.equal(env.tools.size, 0);
  env.listeners.pageshow({ persisted: true });
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(env.tools.size, 2);
  assert.ok(env.signals.slice(2).every(signal => !signal.aborted));
});
