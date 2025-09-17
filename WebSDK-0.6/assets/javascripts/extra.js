// Runs once the Version element is created by the mike scripts
function WaitForVersionNav(selector, callback) {
    const interval = setInterval(() => {
        const element = document.querySelector(selector);
        if (element !== null) {
            clearInterval(interval);
            callback(element);
        }
    }, 500); // Check each 500ms
}
WaitForVersionNav('.md-version__list', function(element) {
    console.log("Elemento encontrado:");
    console.log(element)

    var unrealIndex = -1;
    var unityIndex = -1;
    var websdkIndex = -1;

    const items = element.children;
    for (let i = 0; i < items.length; i++) {
        if(items[i].innerHTML.includes("Unity")){unityIndex = i;break;}
    }

    for (let j = 0; j < items.length; j++) {
        if(items[j].innerHTML.includes("Unreal")){unrealIndex = j;break;}
    }

    for (let j = 0; j < items.length; j++) {
        if(items[j].innerHTML.includes("WebSDK")){websdkIndex= j;break;}
    }

    // Unity Header
    if(unityIndex !== -1) {
        var unityHeader = document.createElement("div");
        unityHeader.className = "md-version__header";
        unityHeader.innerText = "Unity SDK";
        element.insertBefore(unityHeader, items[unityIndex]);
    }

    // Unreal Header
    if(unrealIndex !== -1) {
        var unrealHeader = document.createElement("div");
        unrealHeader.className = "md-version__header";
        unrealHeader.innerText = "Unreal SDK";
        element.insertBefore(unrealHeader, items[unrealIndex]);
    }
    
    // WebSDK Header
    if(websdkIndex !== -1) {
        var websdkHeader = document.createElement("div");
        websdkHeader.className = "md-version__header";
        websdkHeader.innerText = "Web SDK";
        element.insertBefore(websdkHeader, items[websdkIndex]);
    }
});