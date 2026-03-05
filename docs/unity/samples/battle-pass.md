# Building a Battle Pass

A battle pass is a common engagement feature for players. You can implement a Battle Pass for your game by utilizing 
Beamable's Custom Content capabilities. This is a quick guide for how to think about using Beamable for this feature.

-------------------

## Custom Content
First, define a custom content type for the Battle Pass by creating a class that inherits from `ContentObject`.
Each Battle Pass will have tiers, and each tier can have rewards.

```csharp
[ContentType("battlepass")]  
public class Battlepass : ContentObject  
{  
    public string Name;
    public string EndDate;
    public List<Tier> Tiers;  
}

[Serializable]  
public class Tier  
{  
    public int Level;  
    public List<Reward> Rewards;  
}

[Serializable]  
public class Reward  
{  
    public string RewardName;  
    public int Quantity;  
}
```

### Content Setup

Once the custom type is defined, follow these steps to add a Battle Pass content object in the Beamable 
Content Manager:

- **Step 1: Open the Content Manager:**
  - Unity → Window → Beamable → Open Beam Content
- **Step 2: Create a new content object of type Battlepass:**
  - Select "Battlepass" from the content type list.
  - Press the "Create" button.
  - Provide a name for the Battle Pass content.
- **Step 3: Populate the fields in the Unity Inspector:**
  - Name the Battle Pass
  - Set the `EndDate` using the ISO 8601 format (e.g., `2024-12-31T23:59:59Z`).
  - Define the tiers and rewards (Example in screenshot)
  
![Battle Pass Content](docs/media/imgs/battlepass-content.jpg)

- **Step 4: Publish the content:**
  - Once the Battle Pass is configured, press the **Publish** button in the Content Manager to push the Battle Pass 
  content live.

------------------------------------------------

## Fetching and Using the Battle Pass at Runtime

After the Battle Pass is defined and published, use Beamable’s features to fetch and use the content at runtime. 
In this example, we'll retrieve the Battle Pass.

```csharp
// Fetch the Battle Pass content
await battlepassRef.Resolve()
    .Then(content =>
    {
        _battlePass = content;
        Debug.Log($"Fetched Battle Pass: {_battlePass.Name}");
    })
    .Error(ex =>
    {
        Debug.LogError("Failed to fetch the Battle Pass content.");
    });

await DisplayBattlePassDetails();

private async Promise DisplayBattlePassDetails()
{
    Debug.Log($"Battle Pass: {_battlePass.Name}");
    foreach (var tier in _battlePass.Tiers)
    {
        Debug.Log($"Tier {tier.Level}");
        foreach (var reward in tier.Rewards)
        {
            Debug.Log($"Reward: {reward.RewardName}, Quantity: {reward.Quantity}");
        }
    }
    // Parse and display the end date
    if (DateTime.TryParseExact(_battlePass.EndDate, "yyyy-MM-ddTHH:mm:ssZ", CultureInfo.InvariantCulture, DateTimeStyles.AssumeUniversal, out DateTime endDate))
    {
        Debug.Log($"Battle Pass End Date: {endDate}");
    }
    else
    {
        Debug.LogWarning("Failed to parse the Battle Pass End Date.");
    }

    var isValid = await _service.BattlePassService_IsBattlepassValid(battlepassRef);
    Debug.Log($"Is Battle Pass Valid: {isValid}");
}
```

## Adding the Battle Pass to Player Inventory
You can add the Battle Pass to a player's inventory using Beamable's Inventory system. Here's how you can use the 
`Inventory.Update` method to store the Battle Pass details, such as its name and end date.

To access `items.battlepass`, an item named `battlepass` should be created and published through the Content Manager.

```csharp
private async Task AddBattlepassToInventory()
{
    _beamContext = await BeamContext.Default.Instance;
    var inventory = _beamContext.Inventory;

    // Add Battle Pass to the player's inventory
    await inventory.Update(builder => builder.AddItem("items.battlepass", new Dictionary<string, string>
    {
        { "name", _battlePass.Name },
        { "endDate", _battlePass.EndDate }  // Add additional properties for the battle pass
    }));

    Debug.Log("Battle Pass added to inventory!");
}
```

## Handling End Date and Expiration Validation in a Microservice

You can use Beamable’s Microservices to validate the Battle Pass expiration. Since `Battlepass` is a custom 
`ContentObject`, the type won't be findable by default in Microservices. You can create or move the `Battlepass`
custom content script into the Beamable's `Common` folder, which is also referenced in the Microservices. The folder
can be found in `Assets/Beamable/Common`.

Microservice method:
```csharp
[ClientCallable]
public async Task<bool> IsBattlepassValid(ContentRef<Battlepass> battlepass)
{
    var battlePass = await Services.Content.GetContent(battlepass);
    if (battlePass == null)
    {
        throw new Exception($"Battle Pass with ID {battlepass.GetId()} not found");
    }

    var currentTime = DateTimeOffset.UtcNow.ToUnixTimeSeconds();
    if (DateTimeOffset.TryParseExact(battlePass.EndDate, "yyyy-MM-ddTHH:mm:ssZ", 
            CultureInfo.InvariantCulture, DateTimeStyles.AssumeUniversal, out var endDate))
    {
        long endDateUnix = endDate.ToUnixTimeSeconds();
        return currentTime <= endDateUnix;
    }
    else
    {
        throw new Exception("EndDate is not in a valid ISO 8601 format.");
    }
}
```
------------------------------

Download the full sample code from [Beamable Battle Pass Sample](https://github.com/beamable/battle-pass-example).
*Note*: This sample uses the latest Beamable SDK V5.0.0.

------------------------------

## Season Passes
You can also create a season pass that can be used to unlock new content or features.
Currently, there is no sample for this feature; however, here is how to do it. It is very similar to the Battle Pass.

1. **Create a `Season Pass` content object:** This will include the metadata needed for the season 
(its offerings, rewards, end time, etc.).

2. **Inventory or Stats services:** You can use these services to track per-player ownership of a season pass, 
whether they bought it or not.

3. **Microservices:** Here you can enforce the business side of the season pass (checking current date/time if 
it's within the window, granting the season's rewards, or performing a cleanup or reset at season boundaries).

