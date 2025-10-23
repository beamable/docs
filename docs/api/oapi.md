<!-- https://rapidocweb.com/api.html -->

<!-- 
    We could filter the available routes using a regex.
    match-paths="object|basic|api"
    match-type="regex" -->

<rapi-doc 
    heading-text="Beamable"
    primary-color="#02c3ef"
    spec-url="/Docs/assets/beamable-oapi.json" 
    update-route="true"
    show-header="false"
    render-style="focused"
    theme = "dark"
    layout="column"
    show-curl-before-try="true"
    allow-server-selection="false"
    show-info="false"
    goto-path="get-/basic/accounts/me"
    response-area-height="100px"
    bg-color="#00000000"
    >
    </rapi-doc>


<p style="opacity: .7; margin-top: 4px">
    Note: All shortcut keys are disabled on this page to avoid accidental API invocations.
</p>

<script lang="javascript">

    document.addEventListener('keydown', event => {
        // Disable Material's search shortcuts
        event.stopPropagation();
    });

    const sidebar = document.querySelector('.md-sidebar.md-sidebar--secondary')
    console.log('removing sidebar', sidebar)
    sidebar.remove();

    const main = document.querySelector('main.md-main');
    main.classList.add('oapi')

    const reverseInterval = setInterval(function(){
        try {

            const rapiDoc = document.querySelector('rapi-doc');
            rapiDoc.shadowRoot.querySelector('#the-main-body').style['flex-direction'] = 'row-reverse';

            const nav = rapiDoc.shadowRoot.querySelector('#the-main-body > nav')
            const main = rapiDoc.shadowRoot.querySelector('#the-main-body > main')

            setInterval(function() {
                nav.style['height'] = 'max(100vh,' + (main.clientHeight) + 'px)' 
            }, 1)
            clearInterval(reverseInterval);
        } catch {
            // let it go.
        }
    }, 10)
</script>