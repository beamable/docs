[beamable-sdk](../../modules.md) / [services](../README.md) / AnnouncementsService

# Class: AnnouncementsService

Defined in: [src/services/AnnouncementsService.ts:19](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AnnouncementsService.ts#L19)

Represents a service that can be refreshed.

## Extends

- [`ApiService`](ApiService.md)

## Implements

- [`RefreshableService`](../interfaces/RefreshableService.md)<[`AnnouncementView`](../../schema/type-aliases/AnnouncementView.md)[]\>

## Constructors

### Constructor

> **new AnnouncementsService**(`props`): `AnnouncementsService`

Defined in: [src/services/AnnouncementsService.ts:23](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AnnouncementsService.ts#L23)

#### Parameters

##### props

[`ApiServiceProps`](../interfaces/ApiServiceProps.md)

#### Returns

`AnnouncementsService`

#### Overrides

`ApiService.constructor`

## Methods

### claim()

> **claim**(`params`): `Promise`<`void`\>

Defined in: [src/services/AnnouncementsService.ts:85](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AnnouncementsService.ts#L85)

Claims one or more announcements for the current player.

#### Parameters

##### params

[`AnnouncementIdParams`](../interfaces/AnnouncementIdParams.md)

#### Returns

`Promise`<`void`\>

#### Remarks

This marks the announcements as claimed, allowing the player to access any associated rewards.

#### Example

```ts
// client-side:
const announcements = beam.announcements;
// server-side:
const announcements = beamServer.announcements(playerId);
// claim a single announcement
await announcements.claim({ id: "id" });
// claim multiple announcements
await announcements.claim({ id: ["id-1", "id-2"] });
```

#### Throws

If the announcement ID is invalid or the operation fails.

***

### delete()

> **delete**(`params`): `Promise`<`void`\>

Defined in: [src/services/AnnouncementsService.ts:159](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AnnouncementsService.ts#L159)

Deletes one or more announcements for the current player.

#### Parameters

##### params

[`AnnouncementIdParams`](../interfaces/AnnouncementIdParams.md)

#### Returns

`Promise`<`void`\>

#### Remarks

Ensure any claimable announcements are handled appropriately before deletion.

#### Example

```ts
// client-side:
const announcements = beam.announcements;
// server-side:
const announcements = beamServer.announcements(playerId);
// delete a single announcement
await announcements.delete({ id: "id" });
// delete multiple announcements
await announcements.delete({ id: ["id-1", "id-2"] });
```

#### Throws

If the announcement ID is invalid or the operation fails.

***

### list()

> **list**(): `Promise`<[`AnnouncementView`](../../schema/type-aliases/AnnouncementView.md)[]\>

Defined in: [src/services/AnnouncementsService.ts:56](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AnnouncementsService.ts#L56)

Fetches all active announcements for the current player.

#### Returns

`Promise`<[`AnnouncementView`](../../schema/type-aliases/AnnouncementView.md)[]\>

#### Example

```ts
// client-side
const announcements = await beam.announcements.list();
// server-side
const announcements = await beamServer.announcements(playerId).list();
```

#### Throws

If the request fails.

***

### markAsRead()

> **markAsRead**(`params`): `Promise`<`void`\>

Defined in: [src/services/AnnouncementsService.ts:122](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AnnouncementsService.ts#L122)

Marks one or more announcements as read for the current player.

#### Parameters

##### params

[`AnnouncementIdParams`](../interfaces/AnnouncementIdParams.md)

#### Returns

`Promise`<`void`\>

#### Example

```ts
// client-side:
const announcements = beam.announcements;
// server-side:
const announcements = beamServer.announcements(playerId);
// mark a single announcement as read
await announcements.markAsRead({ id: "id" });
// mark multiple announcements as read
await announcements.markAsRead({ id: ["id-1", "id-2"] });
```

#### Throws

If the announcement ID is invalid or the operation fails.

***

### refresh()

> **refresh**(): `Promise`<[`AnnouncementView`](../../schema/type-aliases/AnnouncementView.md)[]\>

Defined in: [src/services/AnnouncementsService.ts:41](https://github.com/beamable/BeamableProduct/blob/c39f644099ee36ab2d4430de7f8a10c2265b0568/web/src/services/AnnouncementsService.ts#L41)

Refreshes the announcements for the current player.

#### Returns

`Promise`<[`AnnouncementView`](../../schema/type-aliases/AnnouncementView.md)[]\>

#### Remarks

This method fetches the latest announcements and updates the player's announcement list.

#### Example

```ts
await beam.announcements.refresh();
```

#### Throws

If the refresh fails.

#### Implementation of

[`RefreshableService`](../interfaces/RefreshableService.md).[`refresh`](../interfaces/RefreshableService.md#refresh)
