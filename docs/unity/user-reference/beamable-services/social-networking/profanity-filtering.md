# Profanity Filtering

Beamable moderates certain player-provided text on the server side. When a
player sends a chat message, sets a group name, tag, or message of the day,
or registers an alias, the platform checks the text against the realm's
configured moderation provider before accepting it.

There are two kinds of check:

- **Assertions** reject text outright. If the provider flags the text, the
  request fails with an HTTP 400 error whose `error` field is `"Profanity"`.
  Group names and tags, alias registration, and the chat profanity-check
  endpoints behave this way.
- **Masking** accepts the text but censors it before it is stored or
  delivered. Chat messages and group messages of the day behave this way.

!!! note "Provider transition"

    As of July 2026, Beamable's previous third-party moderation integration
    (Community Sift) has been retired and replaced with support for OpenAI's
    moderation API. Realms are not moderated by default; moderation is
    enabled per realm through Realm Config as described below.

Moderation Providers
--------------------

The moderation engine is selected per realm with the `"profanity"` /
`"provider"` Realm Config value:

| provider value | behavior |
| -------------- | -------- |
| _unset_ or `"none"` | No moderation. All text passes unmodified. This is the default. |
| `"openai"` | Text is classified by OpenAI's moderation API using an OpenAI API key that you supply. |
| `"local"` | Text is checked against a small built-in English word list. |

### OpenAI provider

The `"openai"` provider sends the text to OpenAI's
[moderation endpoint](https://platform.openai.com/docs/guides/moderation)
and uses OpenAI's own `flagged` verdict. The moderation endpoint is free
of charge on OpenAI's side; you supply your own OpenAI API key, and the
key never leaves the Beamable backend.

Because OpenAI's moderation API classifies a whole input string and does
not report which words caused the verdict, masking with this provider is
all-or-nothing: a flagged chat message is replaced entirely by the censor
mask (default `***`) rather than having individual words censored.

The provider degrades gracefully. If the moderation endpoint is
unreachable, returns an error, or no API key is configured, text passes
through unfiltered rather than failing the player's request. A moderation
outage therefore never breaks chat, group updates, or registration; it
only suspends filtering until the provider recovers.

### Local provider

The `"local"` provider checks each word against a built-in list of about
700 English terms using substring matching. It requires no external
account and works offline, but it is crude in both directions: it flags
innocent words that contain a listed term as a substring, and it misses
most real-world profanity, including anything outside English. Prefer the
OpenAI provider for production use; treat the local list as a last resort.

Realm Configuration
-------------------

To configure moderation, go to the Beamable Portal at
https://portal.beamable.com/ and, after choosing the desired realm, use
Operate > Config to navigate to Realm Config. Use _+ Add Config_ to add
values in the `"profanity"` namespace.

| namespace | key | value |
| --------- | --- | ----- |
| `"profanity"` | `"provider"` | `"openai"`, `"local"`, or `"none"` (default `"none"`) |
| `"profanity"` | `"openai_key"` | your OpenAI API key (`sk-...`); required for the `"openai"` provider |
| `"profanity"` | `"openai_model"` | optional; the OpenAI moderation model, default `"omni-moderation-latest"` |
| `"profanity"` | `"censor_mask"` | optional; the replacement for flagged text when masking, default `"***"` |

Configuration changes take effect without a redeploy. Removing
`"provider"` (or setting it to `"none"`) turns moderation off for the
realm.

To use the OpenAI provider you need an account on
https://platform.openai.com with API access and a secret API key created
under Settings > API keys. New OpenAI accounts may need a payment method
on file before API keys become active, even though the moderation
endpoint itself is free.

Checking Text Explicitly
------------------------

Beyond the automatic checks, the chat service exposes an endpoint that
asserts a piece of text is clean. It returns `{"result": "ok"}` for clean
text and an HTTP 400 error for flagged text:

```
GET /basic/chat/profanityAssert?text=<text to check>
```

```json
{
    "status": 400,
    "service": "chat",
    "error": "Profanity",
    "message": "<the flagged text>"
}
```

The request requires an authenticated player. A useful pair of test
strings for the OpenAI provider: `I want to kill them.` is composed of
harmless words but reliably flags in the violence category, while a
sentence like `What a lovely day for sailing.` passes. Note that single
crude words in isolation often pass OpenAI moderation, because the model
judges the meaning of the whole text rather than matching a word list;
that is the intended behavior of a semantic moderator.
