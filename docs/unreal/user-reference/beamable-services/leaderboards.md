# Leaderboards

The Beamable **Leaderboards** allow the game makers to track player scores in social rankings which are "global" (with hundreds of millions of players) or "segmented" (in smaller groups). It supports:

 - Assign a player to a specific leaderboard
 - Retrieve entries from specific ranges in the leaderboard
 - Leaderboard pagination
 - Retrieve a specific player rank
 - Retrieve the friends ranks

## Getting started

This section covers common leaderboard use cases and how to implement them.

### Creating the leaderboards

There are two ways to create a new leaderboard, using the Portal or as a content.

!!! note "Type of leaderboard"
	If you created the leaderboard in the content, it will appear in the Portal as expected. But if you create the leaderboard directly in the Portal, it Will not appear in the content.

#### Creating via content

To create leaderboard content, open the **Beamable Window** in the top right and select the **Content** tab.

Then select the leaderboard content type as shown in the image below.

![The Content window's Type dropdown open with BeamLeaderboardContent highlighted among the content type options.](../../../media/imgs/leaderboards-select-content-type.png)

After selecting the leaderboard content type, type the name of the leaderboard in the input field.

![The Content window with the Type set to BeamLeaderboard and the Name field holding "new-leaderboard" next to a Create button, all highlighted.](../../../media/imgs/leaderboards-content-create.png)

You will be able to see the leaderboard as a new content in the content list. That means it was created successfully, but it still needs to be published.

Before publishing, there are some configurations that can affect how your leaderboard works.

![The newly created leaderboards.new-leaderboard content selected in the Content window, its detail panel exposing Client Permission, Partitioned, Max Entries, and Cohort Settings fields.](../../../media/imgs/leaderboards-content-details.png)

 - **Client Permission**: Allow the clients to update their score in the leaderboard. **Warning:** This is a potential vulnerability in your game
 - **Partitioned**: Determines whether this leaderboard automatically partitions into smaller leaderboards
 - **Max Entries**: Determines the maximum number of entries in a given leaderboard partition
 - **Cohort Settings**: Specifies criteria for grouping players together


### Assigning a player to a leaderboard

There are two ways to assign a player to a leaderboard:

 - Set a Score Directly: Submit a score for the player on the desired leaderboard. This automatically associates the player with that leaderboard

![An Operation - Leaderboards - UpdateLeaderboardScoreOperation node with a Player Gamer Tag and a Score of 10 feeding, through its On Operation Event pin, an Operation - Leaderboards - FetchLeaderboardOperation node.](../../../media/imgs/leaderboards-blueprint-update-score.png)

 - Use `FetchAssignedLeaderboardOperation` with `Join` = `true`: This operation is particularly useful for partitioned leaderboards. By passing the base leaderboard ID, this operation returns the specific partitioned leaderboard ID (e.g., "leaderboards.my_partitioned_board" becomes "leaderboards.my_partitioned_board#0")

![An Operation - Leaderboards - FetchAssignedLeaderboardOperation node with its Join input checked, feeding a Local State - Leaderboards - TryGetAssignedLeaderboard node that outputs the partitioned leaderboard ID.](../../../media/imgs/leaderboards-blueprint-fetchassigned.png)


!!! warning "If you assign a player without a score"
	If you assign a player without a score, it will be the first of the empty scores. So for example if you have 3 players, the first one with 10 of score the second one with 0 and the third one with 0, when you assign a new player to this leaderboard the new player will take the second place.
	The priority is same score, last assigned.

!!! note "Non Partitioned Leaderboard"
	If you use this operation on a non-partitioned leaderboard, it returns the original leaderboard ID without any partition suffix.

## Modifying entries

You can modify metadata and scores for leaderboard entries. On the microservice side, this is more flexible — a client-authoritative leaderboard cannot change entries other than the authenticated player's.

### Adding score to a player

Here is an example of how to add a score for a client-authoritative client.

![An Operation - Leaderboards - UpdateLeaderboardScoreOperation node with a Player Gamer Tag and a Score of 10 feeding, through its On Operation Event pin, an Operation - Leaderboards - FetchLeaderboardOperation node.](../../../media/imgs/leaderboards-blueprint-update-score.png)

Stats in the leaderboard are primarily used to cache per-entry information, reducing API requests. You can only set stats when updating the score; here is an example.

![A Make Map node holding the key player_top_kills with value 150, fed through a Set node into the Stats input of an Operation - Leaderboards - UpdateLeaderboardScoreOperation node with a Score of 30.](../../../media/imgs/leaderboards-blueprint-set-stats.png)

## Leaderboard samples

### Fetch top 10 players

![An Operation - Leaderboards - FetchLeaderboardOperation node with From 1 and Max 10 inputs feeding a Local State - Leaderboards - TryGetAllRankEntries node that loops over the returned rank entries.](../../../media/imgs/leaderboards-blueprint-top10.png)

With the SDK, you can create leaderboards similar to those in [Brawl Stars](https://supercell.com/en/games/brawlstars/)

### Show the player rank

![An Operation - Leaderboards - FetchPlayerRankOperation node feeding a Local State - Leaderboards - TryGetPlayerRankEntry node that outputs the player's rank, score, and stats.](../../../media/imgs/leaderboards-blueprint-player-rank.png)

Using the Blueprint shown above, you can get the player rank and display it separately

### Leaderboard pagination

![A Blueprint graph where a FetchLeaderboardPageOperation node's result feeds a Local State - Leaderboards - IsLeaderboardPageCached check that branches into either a TryGetPageRankEntries node or another FetchLeaderboardPageOperation, implementing paged leaderboard fetching.](../../../media/imgs/leaderboards-blueprint-pagination.png)

The blueprint shown above is a part of how to have pagination in your leaderboards.




