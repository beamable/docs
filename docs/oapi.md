<!-- https://rapidocweb.com/api.html -->

<!--
    We could filter the available routes using a regex.
    match-paths="object|basic|api"
    match-type="regex" -->

<rapi-doc
    heading-text="Beamable"
    primary-color="#02c3ef"
    spec-url="../assets/beamable-oapi.json"
    update-route="true"
    show-header="false"
    render-style="focused"
    theme = "dark"
    layout="column"
    allow-try="false"
    allow-server-selection="false"
    show-info="false"
    goto-path="get-/basic/accounts/me"
    response-area-height="100px"
    bg-color="#00000000"
    >
    </rapi-doc>

<script lang="javascript">

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
