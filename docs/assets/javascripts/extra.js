// Per Version Consts
const VERSION_NAME = "" // "Unity", "Unreal", "WebSDK" or "" for all

// ---- Helpers ---------------------------------------------------------------
function WaitForVersionNav(selector, callback) {
    const interval = setInterval(() => {
        const element = document.querySelector(selector);
        if (element !== null) {
            clearInterval(interval);
            callback(element);
        }
    }, 500);
}

function insertHeader(container, label, beforeNode) {
    const header = document.createElement("div");
    header.className = "md-version__header";
    header.innerText = label;
    container.insertBefore(header, beforeNode);
}

function headerLabel(name) {
    const map = { Unity: "Unity SDK", Unreal: "Unreal SDK", WebSDK: "Web SDK" };
    return map[name] || name || "Versions";
}

function isVersionEntry(node) {
    // mike typically renders <a class="md-version__link">...</a> or <li>...</li>
    return node?.classList?.contains('md-version__link') || node.tagName === 'A' || node.tagName === 'LI';
}

// ---- Main ------------------------------------------------------------------
WaitForVersionNav('.md-version__list', function(element) {
    const nodes = Array.from(element.children); // snapshot (avoid live-collection index shifts)

    // If VERSION_NAME is empty: show everything and add the three section headers like the original
    if (!VERSION_NAME) {
        // Find the first occurrence for each family BEFORE inserting anything
        const firstUnity  = nodes.find(n => isVersionEntry(n) && n.textContent.includes("Unity"));
        const firstUnreal = nodes.find(n => isVersionEntry(n) && n.textContent.includes("Unreal"));
        const firstWeb    = nodes.find(n => isVersionEntry(n) && n.textContent.includes("WebSDK"));

        if (firstUnity)  insertHeader(element, "Unity SDK",  firstUnity);
        if (firstUnreal) insertHeader(element, "Unreal SDK", firstUnreal);
        if (firstWeb)    insertHeader(element, "Web SDK",    firstWeb);
        return; // don't filter anything
    }

    // Otherwise: filter to only items that include VERSION_NAME
    const visible = [];
    for (const node of nodes) {
        if (!isVersionEntry(node)) continue;
        if (node.textContent.includes(VERSION_NAME)) {
            visible.push(node);
        } else {
            node.style.display = 'none';
            node.setAttribute('aria-hidden', 'true');
        }
    }

    if (visible.length > 0) {
        insertHeader(element, headerLabel(VERSION_NAME), visible[0]);
    } else {
        const emptyMsg = document.createElement('div');
        emptyMsg.className = 'md-version__empty';
        emptyMsg.textContent = `No versions available for “${VERSION_NAME}”.`;
        element.prepend(emptyMsg);
    }
});