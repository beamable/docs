#!/usr/bin/env node
/** How to run - From the repo root: node scripts/generate-api-summary.mjs */
import { promises as fs } from "fs";
import path from "path";

const API_REF_DIR = "docs/web/user-reference/api-reference";
const MODULES_MD = path.posix.join(API_REF_DIR, "modules.md");
const SUMMARY_MD = "docs/web/user-reference/SUMMARY.md";

const START_MARK = "    [//]: # (BEGIN AUTO-GENERATED: API MODULES)";
const END_MARK = "    [//]: # (END AUTO-GENERATED: API MODULES)";

async function main() {
  // The script assumes current working directory is the repo root (where mkdocs.yml lives).
  const cwd = process.cwd();
  const modulesPath = path.join(cwd, MODULES_MD);
  const summaryPath = path.join(cwd, SUMMARY_MD);
  const apiRefAbs = path.join(cwd, API_REF_DIR);

  const modulesContent = await fs.readFile(modulesPath, "utf8");
  const moduleItems = parseModules(modulesContent);
  if (moduleItems.length === 0) {
    throw new Error('No modules found in modules.md under "## Modules".');
  }

  // Map each module to its directory, excluding the README.md part
  const moduleDirs = moduleItems.map((item) => ({
    ...item,
    dir: normalizePosix(path.posix.dirname(item.relPath)),
  }));

  // Build a quick lookup of submodule directories to avoid duplicates in nested listings
  const dirList = moduleDirs.map((m) => m.dir);
  const subdirsByDir = new Map();
  for (const m of moduleDirs) {
    const subs = new Set(
      dirList.filter((d) => d !== m.dir && d.startsWith(m.dir + "/")),
    );
    subdirsByDir.set(m.dir, subs);
  }

  // Gather nested markdown files per module
  const nestedByRelPath = new Map();
  for (const m of moduleDirs) {
    const startDirAbs = path.join(apiRefAbs, m.dir);
    const files = await walkMarkdown(startDirAbs);
    const nested = files
      .map((abs) => normalizePosix(path.posix.relative(apiRefAbs, abs)))
      // exclude the module's own README.md
      .filter((rel) => rel !== path.posix.join(m.dir, "README.md"))
      // exclude anything that lives under a declared submodule dir
      .filter((rel) => {
        const exclude = subdirsByDir.get(m.dir) || new Set();
        for (const sub of exclude) {
          if (rel.startsWith(sub + "/")) return false;
        }
        return true;
      })
      // Ignore the global modules.md if discovered
      .filter((rel) => !rel.endsWith("/modules.md") && rel !== "modules.md");

    // stable, deterministic order
    nested.sort((a, b) => a.localeCompare(b));
    nestedByRelPath.set(m.relPath, nested);
  }

  // Build generated lines
  const generated = [];
  for (const item of moduleItems) {
    const moduleLine = `    - [${item.label}](api-reference/${item.relPath})`;
    generated.push(moduleLine);

    const nested = nestedByRelPath.get(item.relPath) || [];
    for (const rel of nested) {
      const label = labelFor(rel);
      generated.push(`        - [${label}](api-reference/${rel})`);
    }
  }

  // Insert/replace into SUMMARY.md beneath the API Reference section (after Overview)
  const summaryContent = await fs.readFile(summaryPath, "utf8");
  const updated = updateSummary(summaryContent, generated);
  await fs.writeFile(summaryPath, updated, "utf8");
  console.log(
    `Updated ${SUMMARY_MD} with ${moduleItems.length} modules and nested items.`,
  );
}

function parseModules(markdown) {
  const lines = markdown.split(/\r?\n/);
  const startIdx = lines.findIndex(
    (l) => l.trim().toLowerCase() === "## modules",
  );
  if (startIdx === -1) return [];

  const items = [];
  let i = startIdx + 1;
  // Skip blank lines after the heading
  while (i < lines.length && lines[i].trim() === "") i++;
  for (; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();
    if (!trimmed.startsWith("- [")) break; // stop at first non-list item
    const match = /^- \[(.+?)\]\((.+?)\)/.exec(trimmed);
    if (match) {
      const label = match[1];
      const href = match[2];
      items.push({ label, relPath: normalizePosix(href) });
    }
  }
  return items;
}

async function walkMarkdown(dirAbs) {
  const out = [];
  try {
    const entries = await fs.readdir(dirAbs, { withFileTypes: true });
    for (const entry of entries) {
      const full = path.join(dirAbs, entry.name);
      if (entry.isDirectory()) {
        // Skip common non-doc dirs
        if (entry.name === "assets") continue;
        const nested = await walkMarkdown(full);
        out.push(...nested);
      } else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) {
        out.push(full);
      }
    }
  } catch (e) {
    // If a module folder is missing, just skip
  }
  return out;
}

function labelFor(relPath) {
  const posixPath = normalizePosix(relPath);
  const dir = path.posix.dirname(posixPath);
  const base = path.posix.basename(posixPath);
  const name = base.replace(/\.md$/i, "");
  if (name.toLowerCase() === "readme") {
    return path.posix.basename(dir);
  }
  return name;
}

function updateSummary(summaryContent, generatedLines) {
  const eol = summaryContent.includes("\r\n") ? "\r\n" : "\n";
  const lines = summaryContent.split(/\r?\n/);

  // Locate API Reference section
  const apiIdx = lines.findIndex(
    (l) => l.replace(/^\uFEFF/, "").trim() === "- API Reference",
  );
  if (apiIdx === -1) {
    throw new Error('Could not find "- API Reference" section in SUMMARY.md');
  }

  // Find the Overview line under API Reference to insert after
  let insertAfter = apiIdx;
  for (let i = apiIdx + 1; i < lines.length; i++) {
    const l = lines[i];
    const isTopLevel = l.startsWith("- ");
    if (isTopLevel) break; // next top-level section reached
    const t = l.trim();
    if (t.startsWith("- [")) insertAfter = i; // keep moving as long as sub-items exist
  }

  const startExisting = lines.findIndex((l) => l.includes(START_MARK));
  const endExisting = lines.findIndex((l) => l.includes(END_MARK));

  const block = [START_MARK, ...generatedLines, END_MARK].join(eol);

  // If a previous block exists, remove it first so we can reinsert
  let workingLines = lines;
  if (
    startExisting !== -1 &&
    endExisting !== -1 &&
    endExisting > startExisting
  ) {
    workingLines = lines
      .slice(0, startExisting)
      .concat(lines.slice(endExisting + 1));
  }

  // Recompute insertion point on the working lines
  const apiIdx2 = lines.findIndex(
    (l) => l.replace(/^\uFEFF/, "").trim() === "- API Reference",
  );
  if (apiIdx2 === -1) {
    throw new Error(
      'Could not find "- API Reference" section in SUMMARY.md after cleaning existing block',
    );
  }
  let insertAfter2 = apiIdx2;
  for (let i = apiIdx2 + 1; i < workingLines.length; i++) {
    const l = workingLines[i];
    const isTopLevel = l.startsWith("- ");
    if (isTopLevel) break;
    const t = l.trim();
    if (t.startsWith("- [")) insertAfter2 = i;
  }

  const before = workingLines.slice(0, insertAfter2 + 1).join(eol);
  const after = workingLines.slice(insertAfter2 + 1).join(eol);
  const sep1 = before.endsWith(eol) || before.length === 0 ? "" : eol;
  const sep2 = after.startsWith(eol) || after.length === 0 ? "" : eol;
  return `${before}${sep1}${block}${sep2}${after}`;
}

function normalizePosix(p) {
  return p.split("\\").join("/");
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
