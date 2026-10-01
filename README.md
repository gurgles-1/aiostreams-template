# Evan's AIOStreams Template

Versioned, importable [AIOStreams](https://github.com/Viren070/AIOStreams) configuration template.

## Import

In AIOStreams: **About → Get Started → Use a Template → Import Template**, then paste a URL below and hit **Go**. Or download the JSON and use **Import from File**.

| File | URL |
|---|---|
| Latest | `https://raw.githubusercontent.com/gurgles-1/aiostreams-template/main/evan-aiostreams-template.json` |
| v2 (pinned) | `https://raw.githubusercontent.com/gurgles-1/aiostreams-template/main/evan-aiostreams-template.v2.json` |
| v1 (pinned) | `https://raw.githubusercontent.com/gurgles-1/aiostreams-template/main/evan-aiostreams-template.v1.json` |

Importing creates a **new** AIOStreams configuration — it never overwrites your existing one.

## What's in it (v2)

- **Debrid:** TorBox + Torrin (via StremThru), Comet, Torrentio, MediaFusion, StremThru Torz scrapers
- **Usenet:** NZBNest Newznab indexer through the built-in NNTP engine (add your NNTP providers under Dashboard → Usenet → Providers after import — providers are instance-level and can't be in a template)
- **Local:** Zilean via its Torznab endpoint, AIOMetadata (optional)
- **Sorting:** cached-first, Library pinned high, Redhair777 2160p Remux SEL + regex lists synced
- 9 presets, no anime

v1 also included a Hashnab indexer and used AIOStreams' native Zilean preset; v2 drops Hashnab and switches Zilean to the Torznab preset.

## Versions

- `evan-aiostreams-template.json` — always the latest
- `evan-aiostreams-template.vX.json` — pinned snapshots; import one of these to freeze a known-good config

## Secrets

API keys (TMDB, TVDB, indexer keys) are **template inputs**, not baked into the JSON. You enter them once at import; they're stored in your AIOStreams configuration only.

## Rebuilding

`build_template.py` regenerates `evan-aiostreams-template.json` from the declarative config (edit the script, run it, commit the result).
