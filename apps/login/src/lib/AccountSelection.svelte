<script>
  import {authPostTokenBasic} from 'beamable-sdk/api'
  import {auth, cid, requester} from '../stores/connection'
  const { useDefaultCallback = () => {} } = $props();

  let password = $state('')
  let email = $state('')
  let error = $state('')

  let isLoggingIn = $state(false)
  let disabled = $derived(password.length == 0 || email.length == 0 || $cid.length == 0 || isLoggingIn)

  const useDefault = () => {
    useDefaultCallback()
  }
  const login = async () => {

    isLoggingIn = true;
    try {
      error = null;
      const login = await authPostTokenBasic($requester, {
          customerScoped: true,
          grant_type: 'password',
          username: email,
          password: password
      })

      auth.set(login.body)
    } 
    catch (err){
      console.log(err.message)
      error = err.message;
      error = 'Unable to log in.'
      if (err.message.includes('InvalidCredentialsError'))
        error = 'Invalid credentials'
      if (err.message.includes('AccountNotFoundError'))
        error = 'No account found'

    }
    finally {
      isLoggingIn = false;
    }
  }
</script>

<div>
  <hgroup>
    <h3> Link Account </h3>
    <p> We recommend connecting your Beamable account to this sample so you can interact with the data in Portal. Alternatively, you may use a demo account, but you will not be able to interact with it in Portal. </p>
  </hgroup>
  <input 
    type="text" 
    name="alias" 
    bind:value={$cid} 
    placeholder="alias" 
    aria-invalid={$cid ? false : true}
    disabled={isLoggingIn}
  />
  <small>Account Alias or CID</small>


  <input 
    type="email" 
    name="email" 
    bind:value={email} 
    placeholder="email"
    aria-invalid={email ? false : true}
    disabled={isLoggingIn}
  />
  <small>Developer Email</small>


  <input 
    type="password" 
    name="password" 
    bind:value={password} 
    placeholder="password"
    aria-invalid={password ? false : true}
    disabled={isLoggingIn}

    />
  <small style="display: flex;">
    <span style="flex-grow: 1;">
    Developer Password
    </span>
    <a href="https://portal.beamable.com/forgot-password" target="_blank">Forgot Password</a>
  </small>
  


  <div class="buttons">
    <button 
      class="secondary"
      onclick={useDefault}
      disabled={isLoggingIn}>
      Use Demo Account
    </button>
        
    <div class="link-btn">
      <a href="https://portal.beamable.com/signup/registration" target="_blank">Create an Account</a>
      <button 
        onclick={login} 
        aria-busy={isLoggingIn}
        disabled={disabled}>
        Link Account
      </button>
    </div>
  </div>

  <div>
    {#if error}
    <p class="error">{error}</p>
    {/if}
  </div>
</div>


<style>
    .error {
      color: var(--del-color, #e74c3c); /* use Pico's delete color if available */
      font-weight: 500;
    }
    hgroup > p {
        font-size: 0.9em !important;
    }

    .buttons {
        display: flex;
        flex-direction: 1;
        .link-btn {
            flex-grow: 1;
            margin-left: 24px;
            position: relative;
            display: flex;
            flex-direction: column;

            a {
              position: absolute;
              right: 0;
              top: 100%;
            }
        }
    }
</style>
