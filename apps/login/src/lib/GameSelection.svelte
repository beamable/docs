<script>
    import {
        games,
        auth,
        gid,
        realms,
        pid,
        reviewData,
    } from "../stores/connection";

    let selection = $state({
        pid: undefined,
    });

    games.subscribe((x) => {
        if (x.length == 1) {
            $gid = x[0].pid;
        }
    });

    const selectGame = () => {
        pid.set(selection.pid);

        const table = $realms.reduce((agg, curr) => {
            agg[curr.pid] = curr;
            return agg;
        }, {});
        reviewData.set({
            game: {
                projectName: table[$gid].projectName,
            },
            realm: {
                projectName: table[$pid].projectName,
            },
        });
    };
    const signout = () => {
        // dump it.
        auth.set({});
    };
</script>

<div>
    <hgroup>
        <h3>Select Realm</h3>
        <p>
            To connect this sample to your Beamable account, you need to select
            a Game and Realm.
        </p>
    </hgroup>
    <select bind:value={$gid} placeholder="game">
        {#each $games as game}
            <option value={game.pid}>{game.projectName}</option>
        {/each}
    </select>
    <small>Select Game</small>

    <select placeholder="realm" bind:value={selection} disabled={!$gid}>
        {#each $realms as realm}
            <option value={realm}>{realm.projectName}</option>
        {/each}
    </select>
    <small>Select Realm</small>

    <div class="buttons">
        <button class="secondary" onclick={signout}> Sign Out </button>
        <button class="link-btn" onclick={selectGame}> Link to Realm </button>
    </div>
</div>

<style>
    hgroup > p {
        font-size: 0.9em !important;
    }

    .buttons {
        display: flex;
        flex-direction: 1;
        .link-btn {
            flex-grow: 1;
            margin-left: 24px;
        }
    }
</style>
