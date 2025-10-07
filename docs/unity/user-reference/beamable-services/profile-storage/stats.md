# Stats - Overview

The **Stats** feature allows game makers to store and track pieces of data about players. You can use stats to track anything you want about your players, such as how many characters they own, their highest score, or their favorite color. Stats are simple key/value pairs that can be read and written both from the game client and from the Beamable Portal.

**Example Use Cases**

- Data Store - A simple place to read/write info (Ex. How many characters does the player own?)
- Targeting - Stats are the vector for player segmentation (Ex. A/B testing, targeted offer, focused message campaign, announcement for subset of player-base)

The Stats feature offers two main entry points:

- **StatsService API** - This has high flexibility.
- **StatsBehaviour Component** - This has high ease-of-use. 

## Custom Stats
Beamable allows game makers to create custom status for the specific needs of the game design. Mind the following rules when creating defining those:

| Category | Type/Option | Description | Examples/Notes |
|----------|-------------|-------------|----------------|
| **Data Types** | String | For common alphanumeric data storage | Player names, status messages |
| | Numeric | Supports numeric evaluations on the back-end (\<, >, =) and a fast, atomic `increment` API | Scores, levels, currency amounts |
| **Visibility** | Public Stat | Visible to owning player and others | Player Alias, Player Avatar |
| | Private Stat | Visible only to the owning player | "How many characters do I have?" |
| **Data Complexity** | Simple Data Only | Stats are intended to be simple key/value pairs | • Do not store C# objects<br>• Do not store Json blobs |

!!! warning "Important Notes"

    - Custom stats are created on-demand the first time they are written to. There is no need to pre-define stats in the Beamable Portal.
    - Each stat's visibility (public/private) is defined when first written to and cannot be changed after creation
    - Beamable does not support storing complex data types in stats

## Built-In Stats

Beamable automatically creates a specific set of _game private_ stats for each new player. Game makers may read these values if/when its useful for the project's game design.

| Stat Name | Detail |
|-----------|--------|
| `ADVERTISING_ID` | The GAID or IDFA of the device that started the session (If provided) |
| `CLIENT_VERSION` | Version of the client/app which started the session (e.g. 1.0.0) |
| `DATE_INSTALL` | Timestamp of the player install (first session) expressed as unix time (milliseconds since epoch) |
| `DATE_SESSION` | Timestamp of the player's most recent session start expressed as unix time (millisecond since epoch) |
| `DAYS_SINCE_INSTALL` | Total number of days that have passed since the player installed. Or in other words, total number of days between the player's first session and most recent session |
| `INSTALL_DATE` | Date string of the player install (first session) expressed in format yyyy-MM-dd |
| `PURCHASES_3D`<br>`PURCHASES_7D`<br>`PURCHASES_14D`<br>`PURCHASES_28D` | Total number of purchases in the last X days<br><br>_Note: Specifically this refers to X days preceding the most recent player session since stats are not updated when the player doesn't play_ |
| `PURCHASES_TOTAL` | Total number of in-app purchases, irrespective of the value of the purchases |
| `SESSIONS_3D`<br>`SESSIONS_7D`<br>`SESSIONS_14D`<br>`SESSIONS_28D` | Total number of sessions in the last X days<br><br>_Note: Specifically this refers to X days preceding the most recent player session since stats are not updated when the player doesn't play_ |
| `SESSIONS_TOTAL` | Total number of sessions this player has started |
| `SESSION_DAYS` | The total number of days the player has played (i.e. started at least one session) |
| `SPEND_3D`<br>`SPEND_7D`<br>`SPEND_14D`<br>`SPEND_28D` | Total player spend (USD) in the last X days<br><br>_Note: Specifically this refers to X days preceding the most recent player session since stats are not updated when the player doesn't play_ |
| `SPEND_TOTAL` | Total player spend (USD) expressed in cents |
| `THORIUM_GAME_DEVICE` | Type of device if provided |
| `THORIUM_GAME_PLATFORM` | Platform the player is playing on (e.g. Facebook, iOS)<br><br>_Note: Unity reports all iOS devices as "iPhonePlayer" regardless of device type._ |
| `THORIUM_GAME_SOURCE` | Source of the session (If provided, e.g. "web") |
| `TRIALS` | Total list of A/B Testing trials the player is actively associated with (comma delimited list)<br>locale language ISO code of the player (If provided, e.g. "en") |
| `trialmember:<trial name>` | Specific trial the player is a part of, with the value being the specific cohort/group the player is associated with (e.g. `trialmember:button_trial` = `blue_button_group`) |

## StatsService API

The [StatsService](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Api_1_1Stats_1_1StatsService.html#details) provides programmatic access to player statistics. Here are the main methods available:

| Method | Signature | Description |
|--------|-----------|-------------|
| `GetStats` | `GetStats(domain, access, type, id)` | Retrieve one or more stat values for a specific player |
| `SetStats` | `SetStats(access, statsDictionary)` | Set one or more stat values for the current player |

Both `GetStats` and `SetStats` methods require specific parameters to define the scope and access level of the statistics operations:

| Parameter | Type | Required | Valid Values | Description |
|-----------|------|----------|--------------|-------------|
| `domain` | `string` | Yes (GetStats only) | `"client"`, `"game"` | Specifies where the stats can be accessed:<br>• **client** - Accessible from Unity and microservices<br>• **game** - Only accessible from microservices |
| `access` | `string` | Yes | `"public"`, `"private"` | Defines visibility permissions:<br>• **public** - Visible to owning player and others<br>• **private** - Only visible to the owning player |
| `type` | `string` | Yes (GetStats only) | `"player"` | Stat type identifier (legacy parameter, always use "player") |
| `id` | `long` | Yes (GetStats only) | Player ID | The numeric user ID of the player who owns the stats<br>_Note: For private stats, must match your login ID_ |
| `statsDictionary` | `Dictionary<string, string>` | Yes (SetStats only) | Key-value pairs | Dictionary containing stat names as keys and values as strings |

### Usage Examples

**Setting Stats (Write)**
This example demonstrates how to set multiple public stats for the current player.
```csharp
var beamContext = BeamContext.Default;
await beamContext.OnReady;

Dictionary<string, string> statsToSet = new Dictionary<string, string>
{
    { "player_level", "25" },
    { "total_score", "15000" },
    { "favorite_character", "warrior" }
};

await beamContext.Api.StatsService.SetStats("public", statsToSet);
```

**Getting Public Stats (Read)**
This example shows how to retrieve public stats for a specific player.
```csharp
var beamContext = BeamContext.Default;
await beamContext.OnReady;

long targetPlayerId = beamContext.PlayerId; // or any other player's ID
Dictionary<string, string> playerStats = await beamContext.Api.StatsService
    .GetStats("client", "public", "player", targetPlayerId);

// Access specific stats
if (playerStats.TryGetValue("player_level", out string level))
{
    Debug.Log($"Player level: {level}");
}
```

**Getting Private Stats (Microservices Only)**

!!! warning "Security Restriction"

    Private stats can only be retrieved using Beamable Microservices for security reasons. Client code cannot access private stats of other players.

## Viewing Stats in Portal

The Beamable Portal allows you to view and edit player stats directly through the web interface:

![Portal Stats Editor](../../../../../media/imgs/portal-stats-profile-edit.png)

## Getting Started
This section walks through the steps to create a custom stat and then read/write that stat via the `StatBehaviour` and via raw C# coding.

### Creating a Stat Type
Custom stats are created on-demand the first time they are written to. However, it is a best practice to create a `Stat` asset in Unity to define the stat's metadata before it is first written to. This ensures that the stat is created with the correct metadata.

| Step | Detail |
|------|--------|
| 1. Create the Stat | ![Create Stat](../../../../../media/imgs/stats-create-stat-step1.jpg)<br><br>• Unity → Assets → Create → Beamable → Stat |
| 2. Name the asset file | ![Name Asset](../../../../../media/imgs/stats-name-asset-step2.jpg) |
| 3. Populate all data fields | ![Populate Fields](../../../../../media/imgs/stats-populate-fields-step3.jpg)<br><br>_Best Practice: It is a best practice to match the `Stat Key` value with the asset file name_ |
| 4. Save the Unity Project | • Unity → File → Save Project<br><br>_Best Practice: If you are working on a team, commit to version control in this step._ |

There are two main methods for interacting with Stats: 

- Using the [`StatBehaviour`](https://csharp.cdocs.beamable.com/latest/classBeamable_1_1Stats_1_1StatBehaviour.html) Component
- Raw C# coding using the StatsService.
 
Game makers can use either/both methods to meet the needs of the game project.

### Using StatsBehaviour Component

This method offers higher ease-of-use using pre made components

| Unity Hierarchy | Unity Inspector |
| :-------------- | :-------------- |
| ![StatBehaviour Hierarchy](../../../../../media/imgs/stats-behaviour-hierarchy.jpg) | ![StatBehaviour Inspector](../../../../../media/imgs/stats-behaviour-inspector.jpg) |

StatBehaviourExample.cs
```csharp
using Beamable.Stats;
using UnityEngine;

namespace Beamable.Examples.Services.StatsService
{
   /// <summary>
   /// Demonstrates <see cref="StatsService"/>.
   /// </summary>
   public class StatBehaviourExample : MonoBehaviour
   {
      //  Fields  ---------------------------------------
      [SerializeField]
      private StatBehaviour _myStatBehaviour = null;

      //  Unity Methods  --------------------------------
      protected void Start()
      {
         Debug.Log($"Start()");

         //Async refresh value
         _myStatBehaviour.OnStatReceived.AddListener(MyStatBehaviour_OnStatReceived);

         // Set Value
         _myStatBehaviour.SetCurrentValue("0");
         _myStatBehaviour.SetCurrentValue("1");

         // Get Value
         Debug.Log($"_statsBehaviour.value = {_myStatBehaviour.Value}");
      }

      //  Event Handlers  -------------------------------
      private void MyStatBehaviour_OnStatReceived(string value)
      {
         // Observe Value Change
         Debug.Log($"MyStatBehaviour_OnStatReceived() value = {_myStatBehaviour.Value}");
      }
   }
}
```

### Using the StatsService API

This method offers higher flexibility using raw C# coding using the StatsService

| Unity Hierarchy | Unity Inspector |
| :-------------- | :-------------- |
| ![Coding Hierarchy](../../../../../media/imgs/stats-coding-hierarchy.jpg) | ![Coding Inspector](../../../../../media/imgs/stats-coding-inspector.jpg) |

The SetStats and GetStats methods require additional parameters.

| Parameter Name | Detail |
|----------------|--------|
| `access` | Possible values include "public" or "private"<br><br>Public client stats can be retrieved by anyone who knows your ID. Private client stats can only be retrieved for yourself. The distinction is not meaningful in backend, but in practice "game" stats are usually also "private" |
| `domain` | Possible values include "game" (backend) or "client" (Unity)<br><br>Domain is one of "game" (backend) or "client" (Unity). Game stats can only be retrieved from microservices, but client stats can be retrieved both in microservices and in Unity code |
| `id` | The numeric user ID of the player who owns the stats<br><br>_Note: For client private stats this must match the ID of your login (e.g. `beamContext.PlayerId`)_ |
| `type` | Possible values include only "player"<br><br>_Note: This parameter exists for legacy purposes only_ |

StatCodingExample.cs
```csharp
using System.Collections.Generic;
using UnityEngine;

namespace Beamable.Examples.Services.StatsService
{
    /// <summary>
    /// Demonstrates <see cref="StatsService"/>.
    /// </summary>
    public class StatCodingExample : MonoBehaviour
    {
        //  Unity Methods  --------------------------------
        protected void Start()
        {
            Debug.Log($"Start()");

            SetupBeamable();
        }

        //  Other Methods   ------------------------------
        private async void SetupBeamable()
        {
            var context = BeamContext.Default;
            await context.OnReady;

            Debug.Log($"context.PlayerId = {context.PlayerId}");

            string statKey = "MyExampleStat";
            string access = "public";
            string domain = "client";
            string type = "player";
            long id = context.PlayerId;

            // Set Value
            Dictionary<string, string> setStats =
                new Dictionary<string, string>() { { statKey, "99" } };

            await context.Api.StatsService.SetStats(access, setStats);

            // Get Value
            Dictionary<string, string> getStats =
                await context.Api.StatsService.GetStats(domain, access, type, id);

            string myExampleStatValue = "";
            getStats.TryGetValue(statKey, out myExampleStatValue);

            Debug.Log($"myExampleStatValue = {myExampleStatValue}");
        }
    }
}
```

## Stats Vs Analytics

Beamable offers both analytics events and stats. See [Analytics » Code (Analytics Events vs Stats)](doc:analytics-code#analytics-events-vs-stats) for more info. While the use cases for analytics events and stats are often different, there are indeed common workflows where both are used in concert. For example. Beamable automatically tracks an analytics event (deep history) every time a Stat is changed (fast speed). This is the best of both worlds!

Note that The `source` value is set automatically with each Analytics event and stats