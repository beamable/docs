const LIGHTBEAM_TAG = 'mk'
const GIT_TAG = 'main'

class TryItOut extends HTMLElement {
    connectedCallback() {

        const title = this.getAttribute('title') || 'Untitled';
        const args = this.getAttribute('args') || '';
        const gitFragment = this.getAttribute('git-fragment') || '';
        // 
        // 
        window.TryItOutApp.bind(this, {
            gitFragment: gitFragment,
            gitCommit: GIT_TAG,
            args: args,
            title: title
        });
    }
}

class LightBeam extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        const srcVersion = LIGHTBEAM_TAG;
        const srcBaseline = `https://beamable-lightbeams.s3.us-west-2.amazonaws.com/version/${srcVersion}/index.html`
        const title = this.getAttribute('title') || 'Untitled';
        const args = this.getAttribute('args') || '';
        const showTitle = this.getAttribute('show-title') != 'false';
        console.log('SHOW TITLE', showTitle)

        var logs = [];

        // Container
        const container = document.createElement('div');
        container.classList.add('lightbeam');

        // Iframe
        const iframe = document.createElement('iframe');
        iframe.src = `${srcBaseline}?${args}`;
        iframe.classList.add('disable');
        iframe.style.border = 'none';
        iframe.style.width = '960px';
        iframe.style.height = '690px';

        // Mask
        const mask = document.createElement('div');
        mask.classList.add('beam-mask');

        // Assemble DOM
        container.appendChild(mask);
        container.appendChild(iframe);
        this.appendChild(container);
        const component = this;

        let hasLogStart = false;
        function onOut(args) {
            var isStartMessage = args.trim() == 'LIGHTBEAM_BOOT_COMPLETE'
            hasLogStart |= isStartMessage;

            // HACKS; logs we know we do not care about. These are unity standard logs.
            if (args.startsWith('UnloadTime:')) return;
            if (args.startsWith('Unloading')) return;
            if (args.startsWith('Total:')) return;
            

            if (!hasLogStart || isStartMessage) return;
            component.dispatchEvent(new CustomEvent('unity-log', {
                detail: {
                    level: 'log',
                    logArgs: args
                },
                bubbles: false,  // allow it to bubble up through DOM
                composed: true  // allow it to cross shadow DOM boundary
            }));
        }
        function onError(args) {
            if (!hasLogStart) return;

            // hack; this is a known log we do not care about
            if (args.includes('probably just doing extra work')) return;

            component.dispatchEvent(new CustomEvent('unity-log', {
                detail: {
                    level: 'error',
                    logArgs: args
                },
                bubbles: false,  // allow it to bubble up through DOM
                composed: true  // allow it to cross shadow DOM boundary
            }));
        }

        // Call your external login function
        if (window.LoginApp && typeof window.LoginApp.bind === 'function') {
            window.LoginApp.bind(mask, {
                title: title,
                showTitle: showTitle
            }, (data) => {
                mask.remove();

                const host = 'https://beamable-lightbeams.s3.us-west-2.amazonaws.com'
                const originalSrc = iframe.getAttribute('src');
                const modifiedSrc = data?.cid
                    ? `${originalSrc}&cid=${data.cid}&pid=${data.pid}&host=${data.host}&refresh_token=${data.refreshToken}`
                    : originalSrc;

                iframe.setAttribute('src', modifiedSrc);
                iframe.classList.remove('disable');

                iframe.addEventListener('load', () => {
                    iframe.contentWindow.postMessage(
                        'startGame',
                        host
                    );

                    var origin = crypto.randomUUID();
                    // Handle messages coming from the iframe
                    window.addEventListener('message', (event) => {
                        const data = event.data;
                        if (!data || data.type !== 'iframe-console') return;
                        if (data.origin !== origin) {
                            return;
                        }

                        if (data.level === 'log') onOut(...data.args);
                        if (data.level === 'error') onError(...data.args);
                    });
                    iframe.contentWindow.postMessage({
                        type: 'overrideLogs',
                        origin: origin
                    }, host)
                });
            });
        } else {
            console.warn('LoginApp.bind not found');
        }
    }
}

// register webComponents
customElements.define('light-beam', LightBeam);
customElements.define('try-it-out', TryItOut);
