<script>
  import AccountSelection from "./lib/AccountSelection.svelte";
  import GameSelection from "./lib/GameSelection.svelte";
  import ReviewSelection from "./lib/ReviewSelection.svelte";
  import { auth, pid, cid, gid, resolvedCid, requester } from "./stores/connection";

  const { 
    title = "",
    showTitle = true,
    callback = (data) => { console.log('no handler', data) }
  } = $props();

  let hasAuth = $derived($auth.access_token);
  let hasData = $derived($pid.length > 0 && $cid.length > 0);

  auth.subscribe((x) => {
    if (!x.access_token) {
      // dump the gid,
      gid.set("");
      pid.set("");
    }
  });

  const triggerCallback = () => {
    console.log($requester)
    callback({
      cid: $resolvedCid, 
      pid: $pid,
      host: 'https://api.beamable.com',
      refreshToken: $auth.refresh_token
    })
  }
  const triggerDefault = () => {
    callback({cid: null, pid: null, host:null})
  }



</script>

<div class="beam-login pico">
  <div class="beam-container">
    {#if showTitle}
      <h2>{title}</h2>
    {/if}

    {#if hasData}
      <ReviewSelection callback={triggerCallback} />
    {:else if hasAuth}
      <GameSelection />
    {:else}
      <AccountSelection useDefaultCallback={triggerDefault}/>
    {/if}
  </div>
</div>

<style>
  .beam-container {
    margin: 24px auto;
    max-width: 70%;
  }
</style>
