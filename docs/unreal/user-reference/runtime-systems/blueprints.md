# Beamable Blueprint Systems

Beamable provides several types of Blueprint 
nodes to interact with its systems. These are organized into three main
categories: Low Level, Local State, and Operators. Each category serves different purposes and complexity levels in your
game development workflow.

## Low Level Blueprints

Low Level Blueprints provide direct access to Beamable's core functionality. These nodes handle fundamental operations
such as raw API calls, direct data manipulation, and basic service interactions. They are typically used when you need
precise control over the behavior or when building custom systems on top of Beamable's foundation.

![blueprint-lowlevel.png](../../../media/imgs/blueprint-lowlevel.png)

Common use cases include:

- Direct API requests
- Raw or customized workflows
- Manual local state management

## Operators Blueprints

Operators provide high-level Blueprint nodes for online requests to the Beamable services. It's designed to simplify common game operations. These nodes combine
multiple low-level operations into single, easy-to-use nodes that handle complex workflows automatically. They're
perfect for rapid development and standard game features.


![operators-sample.png](../../../media/imgs/blueprint-operators.png)
<center>Sample of a Operator Blueprint Node that encapsulate the Purchase Operation for a Listing from the Skin Store.</center>

Common use cases include:

- Player authentication flows
- Inventory transactions
- Leaderboard operations
- Friends and Parties operations
- Sync and Update Local State data with the backend version

## Local State Blueprints

Local State Blueprints manage the player's local cached version of the data available in the backend. In other words these nodes
handle the player's local data version of the remote database.

![blueprints-localstate.png](../../../media/imgs/blueprint-localstate.png)
<center>Sample of a Local State Blueprint Node that returns the local cached state of the player's Items of the Inventory.</center>

Common use cases include:

- Access current Player stats and Id
- Player inventory management including items and currencies
- Access all local cached data of the beamable services subsystems

# Other Utilities
We also provide additional utility Blueprint nodes such as:

- Direct access to Beamable Subsystems (e.g., Identity, Inventory, Stats)
- Event nodes for handling various system events
- Iterator nodes for processing collections of data
- Helper nodes for common operations and data transformations

![blueprint-subsystems.png](../../../media/imgs/blueprint-subsystems.png)
<center>Sample of a Blueprint graph that access athe Beamable Inventory Subsystem and retrieve a currency amount from the local cached state</center>

![blueprint-event.png](../../../media/imgs/blueprint-event.png)
<center>Sample of a Blueprint Event Node called when the Local State of the Inventory is Updated.</center>

# Beam Flow Mode
Multiple Blueprint nodes can be set as "Beam Flow Mode" in their detail settings. When enabled, these nodes will expose output flow nodes and other useful outpts instead of custom event pin nodes. This allows you to connect them in a more linear fashion, making it easier to visualize and manage complex workflows.

![blueprints-beam-mode.png](../../../media/imgs/blueprints-beam-mode.png)

