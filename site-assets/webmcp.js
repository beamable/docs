/* Documentation-only tools. No account or API operations run here. */
(() => {
  const context = document.modelContext;
  if (!context || typeof context.registerTool !== "function") return;

  let controller = new AbortController();
  let indexPromise;
  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch("/agents/docs-index.json", { signal: controller.signal })
        .then(async response => {
          if (!response.ok) throw new Error("Documentation index is unavailable");
          const index = await response.json();
          if (!Array.isArray(index.products)) throw new Error("Invalid documentation index");
          return index;
        }).catch(error => {
          indexPromise = undefined;
          throw error;
        });
    }
    return indexPromise;
  }

  function validateInput(input, allowed) {
    if (!input || typeof input !== "object" || Array.isArray(input)) throw new Error("Expected an object");
    if (Object.keys(input).some(key => !allowed.includes(key))) throw new Error("Unexpected input property");
    for (const [key, value] of Object.entries(input)) {
      if (typeof value !== "string" || value.length > 2048) throw new Error(`Invalid ${key}`);
    }
  }

  async function execute(callback) {
    try { return await callback(); }
    catch (error) { return { error: error.message }; }
  }

  const tools = [
    {
      name: "list_documentation_versions",
      description: "List public Beamable documentation products and versions, including the current Latest mapping and documentation links",
      inputSchema: {
        type: "object", properties: { product: { type: "string" } }, additionalProperties: false
      },
      annotations: { readOnlyHint: true },
      execute: async (input = {}) => execute(async () => {
        validateInput(input, ["product"]);
        const index = await loadIndex();
        const products = index.products.filter(product => !input.product || product.name === input.product);
        if (!products.length) throw new Error("Unknown product");
        return { products: products.map(product => ({
          name: product.name, latest: product.latest,
          versions: product.versions.map(({ version, url, markdownUrl }) => ({ version, url, markdownUrl }))
        })) };
      })
    },
    {
      name: "open_documentation",
      description: "Open a public Beamable documentation page in this tab; defaults to the product's Latest version and homepage",
      inputSchema: {
        type: "object", required: ["product"], additionalProperties: false,
        properties: { product: { type: "string" }, version: { type: "string" }, path: { type: "string" } }
      },
      execute: async input => execute(async () => {
        validateInput(input, ["product", "version", "path"]);
        const index = await loadIndex();
        const product = index.products.find(product => product.name === input.product);
        if (!product) throw new Error("Unknown product");
        const requested = !input.version || input.version === "Latest" ? product.latest : input.version;
        const version = product.versions.find(version => version.version === requested);
        if (!version) throw new Error("Unknown version");
        const page = version.pages.find(page => page.path === (input.path || ""));
        if (!page) throw new Error("Unknown page path");
        const url = new URL(page.url);
        if (url.origin !== location.origin || !url.pathname.startsWith(`/${version.version}/`)) {
          throw new Error("Invalid documentation URL");
        }
        location.assign(url.href);
        return { url: url.href };
      })
    }
  ];

  const register = () => {
    for (const tool of tools) {
      Promise.resolve().then(() => context.registerTool(tool, { signal: controller.signal }))
        .catch(error => console.warn(`Could not register ${tool.name}:`, error));
    }
  };
  register();
  window.addEventListener("pagehide", () => controller.abort());
  // A restored page needs a fresh signal and registrations.
  window.addEventListener("pageshow", event => {
    if (event.persisted) {
      controller = new AbortController();
      indexPromise = undefined;
      register();
    }
  });
})();
