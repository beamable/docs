# Announcements - Overview

The Beamable **Announcements** feature allows game makers to create and manage in-game announcements for players.

Announcements provide a powerful way to communicate with players about updates, events, news, and other important information directly within your game. If Your game releases new downloadable content every week, and the main menu displays the content in a news panel. This can be created from modifying the Announcements prefab to suit your game's UI scheme, or pulling the announcement via code.

Announcements exist in the form of content objects. They are created and published via the [Content Manager](../profile-storage/content/content-unity.md#content-manager-editor), and viewable via the Announcements Prefab or another custom solution.

The content included in an announcement is quite easy to edit via the Inspector:

![Announcements Content Manager Inspector](../../../../../media/imgs/announcements-content-manager-inspector.png){: style="height:auto;width:400px"}

## Announcements API

Retrieving announcements via C# code is quite simple, and resembles the [Content](../profile-storage/content/content-overview.md) syntax. This is a more flexible solution, since game makers can fit the announcement content to their own UI, rather than using the UI packaged with the Announcements Prefab.

### Initializing the BeamContext

Before we can perform any actions, the current player must be logged in and Beamable must be initialized.

```csharp
private BeamContext _beamContext;
    
private async void Start()
{
    _beamContext = BeamContext.Default;
    await _beamContext.OnReady;
    Debug.Log($"User Id: {_beamContext.PlayerId}");
}
```

### Retrieving the Announcements via GetCurrent

The simplest way to retrieve announcements is via the `GetCurrent()` method from the `AnnouncementService`. This will return an `AnnouncementQueryResponse`, which contains a list of Announcements.

```csharp
private async Task<List<AnnouncementView>> GetAnnouncements()
{
    var response = await _beamContext.Api.AnnouncementService.GetCurrent();
    return response?.announcements;
}
```

### Retrieving Announcements via Subscription

The `AnnouncementService` also features a `Subscribe` method, allowing the game client to react to new announcements as they are published.

```csharp
private void SubscribeToAnnouncements()
{
    _beamContext.Api.AnnouncementService.Subscribe(response =>
    {
        PrintAnnouncements(response?.announcements);
    });
}
```

### Displaying Announcements

Once we have retrieved the announcements, they can be displayed in the app. The function below simply reads the title and body of the content and logs them to the console, but the specific game implementation will require some custom solution.

```csharp
private void PrintAnnouncements(List<AnnouncementView> announcements)
{
    foreach (var announcement in announcements)
    {
        Debug.Log(announcement.title);
        Debug.Log(announcement.body);
    }
}
```

### Validating the Implementation

Call either the `SubscribeToAnnouncements()` or `GetAnnouncements()` functions and inspect the Unity console to validate that your functions are working. Below is the console for a successful run.

![Announcement Test Results](../../../../../media/imgs/announcements-test-console.png){: style="height:auto;width:400px"}

### Sample Code

Below is the full script that shows how to initialize Beamable, retrieve announcements, and print them to the console.

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Beamable;
using Beamable.Common.Api.Announcements;
using UnityEngine;

public class AnnouncementsTest : MonoBehaviour
{
    private BeamContext _beamContext;

    private async void Start()
    {
        _beamContext = BeamContext.Default;
        await _beamContext.OnReady;
    
        Debug.Log($"User Id: {_beamContext.PlayerId}");

        var announcements = await GetAnnouncements();
        PrintAnnouncements(announcements);
        
        SubscribeToAnnouncements();
    }

    private async Task<List<AnnouncementView>> GetAnnouncements()
    {
        var response = await _beamContext.Api.AnnouncementService.GetCurrent();
        return response?.announcements;
    }

    private void SubscribeToAnnouncements()
    {
        _beamContext.Api.AnnouncementService.Subscribe(response =>
        {
            PrintAnnouncements(response?.announcements);
        });
    }

    private void PrintAnnouncements(List<AnnouncementView> announcements)
    {
        foreach (var announcement in announcements)
        {
            Debug.Log(announcement.title);
            Debug.Log(announcement.body);
        }
    }
}
```
