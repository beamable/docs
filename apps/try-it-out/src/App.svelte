<script>
  import { slide } from "svelte/transition";
  const { gitFragment = "", gitCommit = "", title = "", args = "" } = $props();

  const gitUrl = `https://github.com/beamable/BeamableProduct/blob/${gitCommit}/client/${gitFragment}`;

  let active = $state(false);
  let logs = $state([]);
  let logsActive = $state(false);

  let logCount = $derived(logs.length > 9 ? "9+" : logs.length);

  const tryItOut = () => {
    active = !active;

    if (!active){
      logsActive = false;
      logs = []
    }
  };

  const toggleLogs = () => {
    logsActive = !logsActive;
  };

  // const handleLog = (evt) => {
  // }
  function handleLog(evt) {
    logs.push({
      level: evt.detail.level,
      time: formatDate(new Date()),
      args: evt.detail.logArgs,
    });
  }

  function formatDate(d) {
    const pad = (num, size = 2) => String(num).padStart(size, "0");

    const year = d.getFullYear();
    const month = pad(d.getMonth() + 1);
    const day = pad(d.getDate());
    const hours = pad(d.getHours());
    const minutes = pad(d.getMinutes());
    const seconds = pad(d.getSeconds());

    const ms = pad(d.getMilliseconds(), 3); // 3 fractional digits

    return `${year}-${month}-${day}T${hours}:${minutes}:${seconds}.${ms}`;
  }
</script>

<div class="pico">
  <div class="try-it-out">
    <div>
      {#if active}
        <button class="outline secondary" on:click={tryItOut}>
          Close Sample
        </button>

        {#if logs.length > 0}
          <button
            class="outline secondary"
            on:click={toggleLogs}
            transition:slide
          >
            Logs <span class="log-bubble">{logCount}</span>
          </button>
        {/if}
      {:else}
        <button on:click={tryItOut}> Try It Out </button>
      {/if}
    </div>

    <a href={gitUrl} title="View On Github" target="_blank">
      <span>View On Github</span>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"
        ><!--! Font Awesome Free 7.0.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2025 Fonticons, Inc.--><path
          fill="currentColor"
          d="M173.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6m-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3m44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9M252.8 8C114.1 8 8 113.3 8 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C436.2 457.8 504 362.9 504 252 504 113.3 391.5 8 252.8 8M105.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1m-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7m32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1m-11.4-14.7c-1.6 1-1.6 3.6 0 5.9s4.3 3.3 5.6 2.3c1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2"
        ></path></svg
      >
    </a>
  </div>

  {#if active}
    <div class="sample-root" transition:slide>
      <light-beam {title} {args} show-title="false" on:unity-log={handleLog} />

      {#if logsActive}
        <div class="logs" transition:slide>
          <div class="log-header">
            <h4>Logs</h4>
            <button class="close outline secondary" on:click={toggleLogs}>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"
                ><!--!Font Awesome Free v7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
                  d="M183.1 137.4C170.6 124.9 150.3 124.9 137.8 137.4C125.3 149.9 125.3 170.2 137.8 182.7L275.2 320L137.9 457.4C125.4 469.9 125.4 490.2 137.9 502.7C150.4 515.2 170.7 515.2 183.2 502.7L320.5 365.3L457.9 502.6C470.4 515.1 490.7 515.1 503.2 502.6C515.7 490.1 515.7 469.8 503.2 457.3L365.8 320L503.1 182.6C515.6 170.1 515.6 149.8 503.1 137.3C490.6 124.8 470.3 124.8 457.8 137.3L320.5 274.7L183.1 137.4z"
                /></svg
              >
            </button>
          </div>
          <div class="log-container">
            {#each logs as log}
              <div style="margin: 8px 2px;">
                <code style="width: 100%">
                  {#if log.level === "log"}
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 640 640"
                      ><!--!Font Awesome Free v7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
                        d="M320 576C461.4 576 576 461.4 576 320C576 178.6 461.4 64 320 64C178.6 64 64 178.6 64 320C64 461.4 178.6 576 320 576zM288 224C288 206.3 302.3 192 320 192C337.7 192 352 206.3 352 224C352 241.7 337.7 256 320 256C302.3 256 288 241.7 288 224zM280 288L328 288C341.3 288 352 298.7 352 312L352 400L360 400C373.3 400 384 410.7 384 424C384 437.3 373.3 448 360 448L280 448C266.7 448 256 437.3 256 424C256 410.7 266.7 400 280 400L304 400L304 336L280 336C266.7 336 256 325.3 256 312C256 298.7 266.7 288 280 288z"
                      /></svg
                    >
                  {:else}
                    <svg
                      class="error"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 640 640"
                      ><!--!Font Awesome Free v7.1.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
                        d="M320 576C178.6 576 64 461.4 64 320C64 178.6 178.6 64 320 64C461.4 64 576 178.6 576 320C576 461.4 461.4 576 320 576zM320 384C302.3 384 288 398.3 288 416C288 433.7 302.3 448 320 448C337.7 448 352 433.7 352 416C352 398.3 337.7 384 320 384zM320 192C301.8 192 287.3 207.5 288.6 225.7L296 329.7C296.9 342.3 307.4 352 319.9 352C332.5 352 342.9 342.3 343.8 329.7L351.2 225.7C352.5 207.5 338.1 192 319.8 192z"
                      /></svg
                    >
                  {/if}
                  <b>{log.time}: </b>
                  <p style="margin: 0;">{log.args}</p></code
                >
              </div>
            {/each}
          </div>
        </div>
      {/if}
    </div>
  {/if}
</div>

<style>
  .try-it-out {
    display: flex;
    align-items: start;
    justify-content: space-between;
    border-left: solid 2px #524ed2;
    padding-left: 12px;
    a {
      text-align: right;
    }
    svg {
      height: 16px;
    }
    button {
      padding: 8px;
      font-size: 1em;
    }
  }
  .sample-root {
    margin-top: 12px;
    position: relative;

    .logs {
      /* display: none; */
      position: absolute;
      left: 0;
      right: 0;
      top: 0;
      bottom: 0;
      background-color: rgba(0, 0, 0, 0.6);
      padding-top: 24px;
    }
  }

  .log-container {
    overflow: scroll;
    max-height: calc(100% - 70px);
    svg {
      height: 16px;
    }
    .error {
      fill: red;
    }
  }

  .log-header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: baseline;
    padding-left: 12px;
    svg {
      height: 24px;
    }
    .close {
      padding: 2px;
      margin: 14px;
    }
  }

  .log-bubble {
    background: #524ed2;
    border-radius: 50%;
    width: 24px;
    display: inline-block;
    color: white;
  }
</style>
