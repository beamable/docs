<script>
    import { cid, reviewData, pid } from "../stores/connection";

    const { callback = () => {} } = $props();

    const change = () => {
        pid.set("");
    };

    const go = () => {
        callback();
    };
</script>

<div>
    <hgroup>
        <h3>Start Sample</h3>
        <p>You are connecting this sample directly to your account.</p>
    </hgroup>

    <input type="text" readonly value={$cid} />
    <small>Beamable Account</small>
    <input type="text" readonly value={$reviewData.game.projectName} />
    <small>Game Selection</small>
    <input type="text" readonly value={$reviewData.realm.projectName} />
    <small>Realm Selection</small>

    <div class="buttons">
        <button class="secondary" onclick={change}> Change Connection </button>
        <button class="link-btn" onclick={go}> Start Sample </button>
    </div>
</div>

<style>
    hgroup > p {
        font-size: 0.9em  !important;
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
