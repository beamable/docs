# Stats

## Overview

The Beamable SDK Stats feature allows player to track a variety of built-in and custom player stat variables with configurable visibility levels. Two main use cases are:

- **Data Store**- can hold key/value pairs associated with a particular user.
- **Targeting**-  These key/value pairs can be used by other Beamable systems for various things (Announcement Campaings, Matchmaking and others).

## Types of stats

There are two important specifiers of each stat.

First one is `visibility`, in Unreal represented by enum `EBeamStatsVisibility`, it describes who can see stat:

- `private`- Visible only to owning User and Backend.
- `public`- Visible to any User.

Second one is stat `domain`, in Unreal represented by enum `EBeamStatsDomain`, it describes if stat can be retrieved from game itself or does it require using microservices:

- `client`- Can be accessed from both the **Unreal** and **Microservices**.
- `game`- Cannot be accessed from **Unreal** directly, it can still be accessed via **Microservice** using `ClientCallable` calls.