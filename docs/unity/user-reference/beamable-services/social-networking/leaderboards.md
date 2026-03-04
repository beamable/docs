# Leaderboards

The purpose of this feature is to allow players to see and participate in score-based Leaderboards.

Leaderboards provide competitive ranking systems that encourage player engagement and retention by displaying player performance relative to others.

## Leaderboards API

### Submiting Score

Here is a snippet from the sample [`LeaderboardFlowInterpolationExample.cs`](https://github.com/beamable/Beamable_SDK_Examples/tree/master/client/Assets/Examples/Runtime/Prefabs/LeaderboardFlowInterpolationExample/Scripts):

```csharp
private async void SetupBeamable()
{
    _beamContext = BeamContext.Default;
    await _beamContext.OnReady;
    Debug.Log($"_beamContext.PlayerId = {_beamContext.PlayerId}");

    LeaderboardContent leaderboardContent = 
    await _leaderboardMainMenuCustom.LeaderboardBehavior.Leaderboard.Resolve();

    Debug.Log($"PopulateLeaderboard Starting. Wait < 30 seconds... ");
    int leaderboardRowCountMin = 10;
    int leaderboardScoreMin = 99;
    int leaderboardScoreMax = 99999;

    // Populate with custom values 
    Dictionary<string, object> leaderboardStats = new Dictionary<string, object>();
    leaderboardStats.Add("leaderboard_score_timestamp", new 
    DateTimeOffset(DateTime.UtcNow).ToUnixTimeMilliseconds());
    leaderboardStats.Add("leaderboard_score_velocity", 99); // 99 score delta per second
            
    // Populates mock "alias" and "score" for each leaderboard row
    string loggingResult = await MockDataCreator.PopulateLeaderboardWithMockData(
    _beamContext, 
    leaderboardContent,
    leaderboardRowCountMin,
    leaderboardScoreMin,
    leaderboardScoreMax,
    leaderboardStats);
            
    Debug.Log($"PopulateLeaderboard Finish. Result = {loggingResult}");
}
```

### Rendering Score

Here is a snippet from  the sample [`LeaderboardItemCustom.cs`](https://github.com/beamable/Beamable_SDK_Examples/tree/master/client/Assets/Examples/Runtime/Prefabs/LeaderboardFlowInterpolationExample/Scripts):

```csharp
public void Update()
{
    // Prepare value
    long scoreTimestamp = long.Parse(_rankEntry.GetStat("leaderboard_score_timestamp"));
    long scoreVelocity = long.Parse(_rankEntry.GetStat("leaderboard_score_velocity"));
    long currentTimestamp = new DateTimeOffset(DateTime.UtcNow).ToUnixTimeMilliseconds();
    long millisecondsSinceSubmission = currentTimestamp - scoreTimestamp;
    long scoreSinceSubmission = (millisecondsSinceSubmission * scoreVelocity) / 1000;
   
    // Render value
    double score = _rankEntry.score + scoreSinceSubmission;
    TxtScore.text = $"{score:00000}";
}
```

### Getting Board

When calling either `GetBoard` or `GetAssignedBoard`, the parameters share the following semantics:

| Parameter | Description |
|-----------|-------------|
| `leaderBoard`/`boardId` | The board whose subset of rank entries you want to retrieve.<br>• For the partitioned case (`GetAssignedBoard`), it'll always return you the partition containing the requesting/authenticated user. |
| `from` | Is the first "rank" you want to retrieve. This parameter is ignored if a `focus` is given.<br>• If this value is greater than the lowest rank, you'll get no `RankEntries` back: if there are 10 entries in the board and you pass in `from=15`, you'll get an empty array of `RankEntries` in your `LeaderBoardView`. |
| `max` | Is the number of ranks, starting from `from`, and moving towards the lowest rank that you want to retrieve.<br>• As in, if `from=20` and `max=10`, you'll get ranks `[20~30]`.<br>• If there are not enough entries to fill this amount, the search is truncated. |
| `focus` | is a User's PlayerId that'll be used as the middle `RankEntry` of the resulting `LeaderBoardView`.<br>• Takes `max/2` ranks above the `focus` and `max/2` ranks from below the `focus`.<br>• It is inclusive. As in, if `focus` is at rank 50 and you pass in `max=10`, you should see `[40~61]`.<br>• If there are not enough entries in the leaderboard either above or below you, the corresponding `max/2` will be truncated. |
| `outlier` | A GamerTag whose `RankEntry` is guaranteed to be included. When this is passed in, the resulting entry is stored in `LeaderBoardView.rankgt`. |

Here is a snippet from [`LeaderboardServiceExample.cs`](https://github.com/beamable/Beamable_SDK_Examples/blob/master/client/Assets/Examples/Runtime/Services/LeaderboardService/LeaderboardServiceExample/Scripts/):

```csharp
private async Task<List<RankEntry>> LeaderboardServiceGetBoard(string id, long userId)
{
    LeaderBoardView leaderBoardView = await _beamContext.Api.LeaderboardService.GetBoard(id, 0, 100, 
    userId);

    foreach (RankEntry rankEntry in leaderBoardView.rankings)
    {
        // Get alias for userId of rankEntry
        long nextUserId = rankEntry.gt;
        var stats = 
                await _beamContext.Api.StatsService.GetStats("client", "public", "player", nextUserId );
                
        string alias = "";
        stats.TryGetValue(alias, out alias);
        if (string.IsNullOrEmpty(alias))
        {
            alias = "Unknown Alias";
        }
                
        // Log
        Debug.Log($"Rank = {rankEntry.rank}, Alias = {alias}, Score = {rankEntry.score}");
    }

    return leaderBoardView.rankings;
}
```
## WebGL Sample

You can try out this feature in the interactive WebGL demo:
[Unity WebGL Player - Leaderboard Flow Example](https://beamable.github.io/Beamable_SDK_Examples/Builds/WebGL/LeaderboardFlowExample/index.html)
