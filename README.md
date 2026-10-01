# Evan's AIOStreams Template

Versioned, importable [AIOStreams](https://github.com/Viren070/AIOStreams) configuration template.

## Import

In AIOStreams: **About → Get Started → Use a Template → Import Template**, then paste a URL below and hit **Go**. Or download the JSON and use **Import from File**.

| File | URL |
|---|---|
| Latest | `https://raw.githubusercontent.com/gurgles-1/aiostreams-template/main/evan-aiostreams-template.json` |
| v1 (pinned) | `https://raw.githubusercontent.com/gurgles-1/aiostreams-template/main/evan-aiostreams-template.v1.json` |

Importing creates a **new** AIOStreams configuration — it never overwrites your existing one.

## What's in it (v1)

- **Debrid:** TorBox + Torrin (via StremThru), Comet, Torrentio, MediaFusion, StremThru Torz scrapers
- **Usenet:** NZBNest + Hashnab Newznab indexers through the built-in NNTP engine (add your NNTP providers under Dashboard → Usenet → Providers after import — providers are instance-level and can't be in a template)
- **Local:** Zilean, AIOMetadata (optional)
- **Sorting:** cached-first, Library pinned high, Redhair777 2160p Remux SEL + regex lists synced
- 12 presets, no anime

## Versions

- `evan-aiostreams-template.json` — always the latest
- `evan-aiostreams-template.vX.json` — pinned snapshots; import one of these to freeze a known-good config

## Secrets

API keys (TMDB, TVDB, indexer keys, Prowlarr key) are **template inputs**, not baked into the JSON. You enter them once at import; they're stored in your AIOStreams configuration only.

## Rebuilding

`build_template.py` regenerates `evan-aiostreams-template.json` from the declarative config (edit the script, run it, commit the result).
