# Connectivity

The Connectivity system drives the heartbeat sent back to the Beamable backend platform. If the game client loses connectivity, the heartbeat will stop and the Beamable API will gracefully wait for reconnection before resuming the full online feature-set.

The system monitors internet connectivity and updates automatically if any changes occur; including remote server outages or loss of local ethernet/Wi-Fi internet.

## Connectivity API

Unlike many Beamable Features, Connectivity does not require a specific Beamable Feature Prefab to be used. The main entry point to this feature is C# programming.

The main API highlights include [`ConnectivityService`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Api_1_1Connectivity_1_1ConnectivityService.html#details).

| Method Name | Detail |
| :---------- | :----- |
| HasConnectivity | Getter. Determines if the app has internet connectivity |
| SetHasInternet | Setter. Determines if the app has internet connectivity<br><br>_Note: Calling this is not required. The Beamable system will automatically monitor connectivity and update the ConnectivityService._ |


### Sample Code

Here are some code examples to help you get started.

In this `ConnectivityServiceExample.cs`, the UI shows the current state of the internet connectivity and updates automatically if any changes occur (for example, if the ethernet / Wi-Fi is manually disabled or enabled by the user).

ConnectivityServiceExample.cs
```csharp
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

namespace Beamable.Examples.Services.ConnectivityService
{
    /// <summary>
    /// Holds data for use in the <see cref="ConnectivityServiceExampleUI"/>.
    /// </summary>
    [System.Serializable]
    public class ConnectivityServiceExampleData
    {
        public List<string> OutputLogs = new List<string>();
        public bool HasConnectivity = false;
    }
   
    [System.Serializable]
    public class RefreshedUnityEvent : UnityEvent<ConnectivityServiceExampleData> { }
    
    /// <summary>
    /// Demonstrates <see cref="ConnectivityService"/>.
    /// </summary>
    public class ConnectivityServiceExample : MonoBehaviour
    {
        //  Events  ---------------------------------------
        [HideInInspector]
        public RefreshedUnityEvent OnRefreshed = new RefreshedUnityEvent();
        
        //  Fields  ---------------------------------------
        private BeamContext _beamContext;
        private ConnectivityServiceExampleData _data = new ConnectivityServiceExampleData();
    
        //  Unity Methods  --------------------------------
        protected void Start()
        {
            Debug.Log($"Start() Instructions...\n\n" +
                      " * Ensure Computer's Internet Is Active\n" +
                      " * Run The Scene\n" +
                      " * See Onscreen UI Show HasConnectivity = true\n" +
                      " * Ensure Computer's Internet Is NOT Active (e.g. Turn off wifi/ethernet)\n" +
                      " * See Onscreen UI Show HasConnectivity = false\n");

            SetupBeamable();
        }
        
        //  Methods  --------------------------------------
        private async void SetupBeamable()
        {
            _beamContext = BeamContext.Default;
            await _beamContext.OnReady;

            Debug.Log($"beamContext.PlayerId = {_beamContext.PlayerId}");

            // Observe ConnectivityService Changes
            _beamContext.Api.ConnectivityService.OnConnectivityChanged += ConnectivityService_OnConnectivityChanged;
            
            // Update UI Immediately
            bool hasConnectivity = _beamContext.Api.ConnectivityService.HasConnectivity;
            ConnectivityService_OnConnectivityChanged(hasConnectivity);
        }
        
        public void ToggleHasInternet()
        {
            _beamContext.Api.ConnectivityService.SetHasInternet(!_data.HasConnectivity);
        }

        public void Refresh()
        {
            string refreshLog = $"Refresh() ..." +
                                $"\n * HasConnectivity = {_data.HasConnectivity}" + 
                                $"\n * OutputLogs = {_data.OutputLogs.Count}\n\n";
            
            //Debug.Log(refreshLog);
            
            // Send relevant data to the UI for rendering
            OnRefreshed?.Invoke(_data);
        }
        
        //  Event Handlers  -------------------------------
        private void ConnectivityService_OnConnectivityChanged(bool hasConnectivity)
        {
            _data.HasConnectivity = hasConnectivity;
            
            _data.OutputLogs.Add($"HasConnectivity = {_data.HasConnectivity}");
            
            Refresh();
        }
    }
}
```

### Disable Network Connection

Game makers can set a global disable to simulate not having Wi-Fi before BeamContext initialization.

```csharp
private static void ForceDisableConnectivity()
{
    // to simulate network outage even if the device is online
    IConnectivityServiceExtensions.GlobalForceDisabled = true;
}

private async void SetupBeamable()
{
    ForceDisableConnectivity();

    _beamContext = BeamContext.Default;
    await _beamContext.OnReady;

    Debug.Log($"beamContext.PlayerId = {_beamContext.PlayerId}");

    // Observe ConnectivityService Changes
    _beamContext.Api.ConnectivityService.OnConnectivityChanged += ConnectivityService_OnConnectivityChanged;

    // Update UI Immediately
    bool hasConnectivity = _beamContext.Api.ConnectivityService.HasConnectivity;
    ConnectivityService_OnConnectivityChanged(hasConnectivity);
}
```

### Custom Connectivity Service

From version 1.11 and above, you can override the `IConnectivityChecker` service via Dependency Injection and change how the connectivity logic works. The default implementation uses a polling approach and sends requests to Beamable's API Gateway.

In the code sample below, there is a custom implementation of `IConnectivityService` that pings a local server at `"http://127.0.0.1:3000/ping"`.

CustomConnectivityService.cs
```csharp
using System;
using System.Collections;
using Beamable.Api.Connectivity;
using Beamable.Common;
using UnityEngine;
using UnityEngine.Networking;

public class CustomConnectivityService : IConnectivityService
{
    private bool _isConnected = true;
    public float PollingInterval => 5f;
    public bool HasConnectivity => _isConnected && !Disabled;
    public bool ForceDisabled { get; set; }
    public bool Disabled => ForceDisabled || IConnectivityServiceExtensions.GlobalForceDisabled;
    public event Action<bool> OnConnectivityChanged;
    
    public  Promise SetHasInternet(bool hasInternet)
    {
        var promise = new Promise();
        
        if (!Disabled)
        {
            _isConnected = hasInternet;
            OnConnectivityChanged?.Invoke(hasInternet);
        }
        
        promise.CompleteSuccess();
        return promise;
    }

    public Promise ReportInternetLoss()
    {
        Debug.LogError("Internet connection lost");
        return SetHasInternet(false);
    }

    public void OnReconnectOnce(Action onReconnection)
    {
        if (HasConnectivity) onReconnection.Invoke();
    }

    public void OnReconnectOnce(ConnectionCallback promise, int order = 0)
    {
        if (HasConnectivity) _ = promise();
    }

    // For testing locally, go to Edit > Project Settings > Player > Other Settings
    // Then set Allow downloads over HTTP = Allowed in development builds
    public IEnumerator PingServer()
    {
        const string url = "http://127.0.0.1:3000/ping";
        using var webRequest = UnityWebRequest.Get(url);
        
        // Send the request asynchronously
        yield return webRequest.SendWebRequest();
        
        if (webRequest.result == UnityWebRequest.Result.Success)
        {
            // Request was successful, and you can handle the response data here.
            var responseText = webRequest.downloadHandler.text;
            Debug.Log("Response: " + responseText);
            // raise connectivity event status to true
            OnConnectivityChanged?.Invoke(!Disabled);
        }
        else
        {
            // Request failed; handle the error.
            Debug.LogError("Request failed: " + webRequest.error);
            // raise connectivity event status to false
            if (!Disabled) OnConnectivityChanged?.Invoke(false);
        }
    }
}
```

This code demonstrated how to override the existing `IConnectivityService`

```csharp
[BeamContextSystem]
public class Registrations
{
	[RegisterBeamableDependencies]
	public static void Build(IDependencyBuilder builder)
	{
		builder.RemoveIfExists<IConnectivityChecker>();
		builder.AddSingleton<IConnectivityChecker, CustomConnectivityService>();
	}
}
```

Load this code into a scene to see the custom implementation in action.

CustomConnectivityServiceExample.cs
```csharp
using System;
using System.Collections;
using System.Collections.Generic;
using System.Threading.Tasks;
using Beamable;
using Beamable.Api.Connectivity; // add this to docs
using UnityEngine;
using UnityEngine.Events;

/// <summary>
/// Holds data for use in the <see cref="ConnectivityServiceUI"/>.
/// </summary>
[Serializable]
public class ConnectivityServiceData
{
    public List<string> OutputLogs = new List<string>();
    public bool HasConnectivity = false;
}

[Serializable]
public class RefreshedUnityEvent : UnityEvent<ConnectivityServiceData> { }

/// <summary>
/// Demonstrates <see cref="CustomConnectivityService"/>.
/// </summary>
public class CustomConnectivityServiceExample : MonoBehaviour
{
    //  Events  ---------------------------------------
    [HideInInspector]
    public RefreshedUnityEvent OnRefreshed = new();
    
    //  Fields  ---------------------------------------
    private BeamContext _beamContext;
    private ConnectivityServiceData _data = new();
    private IConnectivityService _connectivityService;
    
    //  Properties  -----------------------------------
    public ConnectivityServiceData Data => _data;

    //  Unity Methods  --------------------------------
    protected async void Start()
    {
        Debug.Log($"Start() Instructions...\n\n" +
                  " * Ensure Computer's Internet Is Active\n" +
                  " * Run The Scene\n" +
                  " * See Onscreen UI Show HasConnectivity = true\n" +
                  " * Ensure Computer's Internet Is NOT Active (e.g. Turn off wifi/ethernet)\n" +
                  " * See Onscreen UI Show HasConnectivity = false\n");

        SetupConnectivityService(new CustomConnectivityService());
        await SetupBeamable();
        StartCoroutine(PingCustomServerPolling());
    }

    private IEnumerator PingCustomServerPolling()
    {
        if (_connectivityService is not CustomConnectivityService service) yield break;
        while (true)
        {
            StartCoroutine(service.PingServer());
            yield return new WaitForSeconds(service.PollingInterval);
        }
    }

    //  Methods  --------------------------------------
    private void SetupConnectivityService(IConnectivityService connectivityService) =>
        _connectivityService = connectivityService;

    private async Task SetupBeamable()
    {
        _beamContext = BeamContext.Default;
        await _beamContext.OnReady;

        Debug.Log($"beamContext.PlayerId = {_beamContext.PlayerId}");

        // Observe ConnectivityService Changes
        _connectivityService.OnConnectivityChanged += ConnectivityService_OnConnectivityChanged;
    }
    
    public void ToggleHasInternet()
    {
        _connectivityService.SetHasInternet(!_data.HasConnectivity);
    }

    public void Refresh()
    {
        string refreshLog = $"Refresh() ..." +
                            $"\n * HasConnectivity = {_data.HasConnectivity}" + 
                            $"\n * OutputLogs = {_data.OutputLogs.Count}\n\n";
        
        Debug.Log(refreshLog);
        
        // Send relevant data to the UI for rendering
        OnRefreshed?.Invoke(_data);
    }
    
    //  Event Handlers  -------------------------------
    private void ConnectivityService_OnConnectivityChanged(bool hasConnectivity)
    {
        _data.HasConnectivity = hasConnectivity;
        
        _data.OutputLogs.Add($"HasConnectivity = {_data.HasConnectivity}");
        
        Refresh();
    }
}
```

### Reduce NoConnectivityException

A few noteworthy clarifications:

1. There are two services responsible for connectivity:
  1. **ConnectivityChecker**: This service implements the call that determines whether Beamable is reachable.
  2. **ConnectivityService**: This service maintains the state on whether internet connectivity is currently available, and is also responsible for invoking any reconnect hooks and so forth
2. The NoConnectivityException errors can occur as a result of a couple of conditions:
  1. The **ConnectivityChecker**, which checks connectivity every 3 seconds, experiences a failure **OR**
  2. A request to Beamable experiences a timeout or HTTP status code 0 from Unity
     Beamable also makes regular heartbeat calls which may also fall into this class
3. When a NoConnectivityException is encountered, the **ConnectivityService** is notified that the internet connection has been lost, and the **ConnectivityService** then invokes any relevant hooks for reconnecting when the service is restored.

As such, this can result in false negatives (the **ConnectivityService** erroneously reports that connectivity has been lost if a single request, which may not be critical to the game, results in a timeout).

The below changes (dependency registration and connectivity service override) alter this behavior:

- **ConnectivityChecker** has been stubbed to always report that internet connectivity is available
- **ConnectivityService** has also been stubbed to always report that internet connectivity is available
- You can also update the Project Settings to:
  - Disable offline cache
  - Disable sending heartbeat
    - If you're using Beamable matchmaking, you want to keep this on.
  - Disable optimistic inventory updates

The result of this is as follows:

- When a request times out or results in a status code 0 -- it will not cause the **ConnectivityService** to declare that the internet connectivity is unavailable. That specific request will still result in a NoConnectivityException , so you can retry it if you choose, but it will not cascade into other requests.
- Beamable will no longer phone home frequently (heartbeat), resulting in noisy numbers of errors in case of a dropped connection

Overall, users with bad connections will see an error, as they should, but people with fine connections should experience markedly fewer false negatives.

#### Dependency Registration

```csharp
[BeamContextSystem]
public class DependencyRegistration
{
  [RegisterBeamableDependencies]
  public static void Register(IDependencyBuilder builder)
  {
    builder.ReplaceSingleton<IConnectivityChecker, AlwaysConnectivityChecker>();
    builder.ReplaceSingleton<IConnectivityService, AlwaysConnectivityService>();
    Debug.Log("Registered custom Beamable dependencies.");
  }
}
```

#### Connectivity Service Override

```csharp
public class AlwaysConnectivityChecker : IConnectivityChecker
{
  public bool ConnectivityCheckingEnabled { get; set; } = false;

  public Promise<bool> ForceCheck()
  {
    return Promise<bool>.Successful(true);
  }
}

public class AlwaysConnectivityService : IConnectivityService
{
  public Promise SetHasInternet(bool hasInternet)
  {
    // SetHasInternet(true) gets called frequently, so not logging it here.
    if (!hasInternet)
    {
      Debug.Log("Ignoring SetHasInternet(false) in AlwaysConnectivityService");
    }
    return Promise.Success;
  }

  public Promise ReportInternetLoss()
  {
    // ReportInternetLoss may be overly verbose, so this Debug.Log is commented out.
    // Debug.Log("Ignoring ReportInternetLoss in AlwaysConnectivityService");
    return Promise.Success;
  }

  public void OnReconnectOnce(Action onReconnection)
  {
    Debug.Log("Immediately calling Action for OnReconnectOnce in AlwaysConnectivityService");
    onReconnection();
  }

  public void OnReconnectOnce(ConnectionCallback promise, int order = 0)
  {
    Debug.Log("Immediately calling ConnectionCallback for OnReconnectOnce in AlwaysConnectivityService");
  }

  public bool HasConnectivity => true;
  public bool ForceDisabled
  {
    get => false;
    set => Debug.Log("Ignoring ForceDisabled.set in AlwaysConnectivityService");
  }

  public bool Disabled => false;

  // In AlwaysConnectivityService, we never invoke OnConnectivityChanged.
  public event Action<bool> OnConnectivityChanged;
}
```
