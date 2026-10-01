# Evan's AIOStreams Template

Versioned, importable [AIOStreams](https://github.com/Viren070/AIOStreams) configuration template.

## Import

In AIOStreams: **About → Get Started → Use a Template → Import Template**, then paste a URL below and hit **Go**. Or download the JSON and use **Import from File**.

| File | URL |
|---|---|
| Latest | `https://raw.githubusercontent.com/gurgles-1/aiostreams-template/main/evan-aiostreams-template.json` |
| v3 (pinned) | `https://raw.githubusercontent.com/gurgles-1/aiostreams-template/main/evan-aiostreams-template.v3.json` |
| v2 (pinned) | `https://raw.githubusercontent.com/gurgles-1/aiostreams-template/main/evan-aiostreams-template.v2.json` |
| v1 (pinned) | `https://raw.githubusercontent.com/gurgles-1/aiostreams-template/main/evan-aiostreams-template.v1.json` |

Importing creates a **new** AIOStreams configuration — it never overwrites your existing one.

## What's in it (v3)

- **Debrid:** TorBox + Torrin (via StremThru), Comet, Torrentio, MediaFusion, StremThru Torz scrapers
- **Library** addon, AIOMetadata (optional)
- **Sorting:** cached-first, Library pinned high, Redhair777 2160p Remux SEL + regex lists synced
- 7 presets, no anime

Indexers are managed separately via the Prowlarr marketplace addon (v3 drops the template's indexer inputs/presets entirely).

v2 had NZBNest (newznab) + Zilean (torznab); v1 also had Hashnab and used the native Zilean preset.

## Versions

- `evan-aiostreams-template.json` — always the latest
- `evan-aiostreams-template.vX.json` — pinned snapshots; import one of these to freeze a known-good config

## Secrets

API keys (TMDB, TVDB) are **template inputs**, not baked into the JSON. You enter them once at import; they're stored in your AIOStreams configuration only.

## Rebuilding

`build_template.py` regenerates `evan-aiostreams-template.json` from the declarative config (edit the script, run it, commit the result).
