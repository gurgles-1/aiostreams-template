#!/usr/bin/env python3
"""Builds evan-aiostreams-template.json — Evan's AIOStreams config template."""
import json
import uuid

RSE_URL = "https://raw.githubusercontent.com/redhair777/aio-quality-profiles/main/profiles/2160p-remux.expressions.json"
REGEX_URL = "https://raw.githubusercontent.com/redhair777/aio-quality-profiles/main/profiles/2160p-remux.regexes.json"

# Version/changelog: AIOStreams matches applied templates to updates by
# metadata.id, so the id below ("evan.aiostreams.setup") must NEVER change
# between versions — only bump TEMPLATE_VERSION.
TEMPLATE_VERSION = "4.0.0"

CHANGELOG = [
    {
        "date": "2026-10-01",
        "version": "1.0.0",
        "content": "Initial template: NZBNest + Hashnab newznab indexers, Zilean native preset, full addon lineup.",
    },
    {
        "date": "2026-10-01",
        "version": "2.0.0",
        "content": "Dropped Hashnab; Zilean via Torznab preset instead of native.",
    },
    {
        "date": "2026-10-01",
        "version": "3.0.0",
        "content": "Dropped all indexers from the template (managed via the Prowlarr marketplace addon instead).",
    },
    {
        "date": "2026-10-01",
        "version": "4.0.0",
        "content": "Fixed Library preset showRefreshActions type; stable template ID so AIOStreams can offer in-place updates.",
    },
]

inputs = [
    {
        "id": "metaApis",
        "name": "Metadata APIs",
        "description": "Keys used for posters and metadata lookups. TMDB is strongly recommended.",
        "type": "subsection",
        "required": False,
        "subOptions": [
            {
                "id": "tmdbApiKey",
                "name": "TMDB API Key",
                "description": "Your TMDB API key.",
                "type": "password",
                "required": False,
            },
            {
                "id": "tvdbApiKey",
                "name": "TVDB API Key",
                "description": "Your TVDB API key (optional).",
                "type": "password",
                "required": False,
            },
        ],
    },
    {
        "id": "aiometa",
        "name": "AIOMetadata (optional)",
        "description": "Cross-ID metadata addon. Paste the manifest URL only if you run AIOMetadata; otherwise leave blank and the addon entry is skipped.",
        "type": "subsection",
        "required": False,
        "subOptions": [
            {
                "id": "aiometaUrl",
                "name": "AIOMetadata manifest URL",
                "description": "Full manifest URL of your AIOMetadata instance.",
                "type": "url",
                "required": False,
            },
        ],
    },
]


presets = [
    {
        "type": "comet",
        "instanceId": "",
        "enabled": True,
        "options": {
            "name": "Comet",
            "timeout": 5000,
            "resources": ["stream"],
            "mediaTypes": [],
            "includeP2P": True,
            "removeTrash": True,
            "useMultipleInstances": False,
        },
        "category": "Debrid",
    },
    {
        "type": "torrentio",
        "instanceId": "",
        "enabled": True,
        "options": {
            "name": "Torrentio",
            "timeout": 5000,
            "resources": ["stream"],
            "mediaTypes": [],
            "providers": [],
            "useMultipleInstances": False,
        },
        "category": "Debrid",
    },
    {
        "type": "mediafusion",
        "instanceId": "",
        "enabled": True,
        "options": {
            "name": "MediaFusion",
            "timeout": 5000,
            "resources": ["stream"],
            "mediaTypes": [],
            "useCachedResultsOnly": True,
            "enableWatchlistCatalogs": False,
            "downloadViaBrowser": False,
            "contributorStreams": False,
            "certificationLevelsFilter": [],
            "nudityFilter": [],
            "includeP2P": True,
            "useMultipleInstances": False,
        },
        "category": "Debrid",
    },
    {
        "type": "stremthruTorz",
        "instanceId": "",
        "enabled": True,
        "options": {
            "name": "StremThru Torz",
            "timeout": 5000,
            "resources": ["stream"],
            "mediaTypes": [],
            "includeP2P": True,
            "useMultipleInstances": False,
        },
        "category": "Debrid",
    },
    {
        "type": "torbox",
        "instanceId": "",
        "enabled": True,
        "options": {
            "name": "TorBox",
            "timeout": 5000,
            "resources": ["stream", "meta", "catalog"],
            "mediaTypes": [],
        },
        "category": "Debrid",
    },
    {
        "type": "library",
        "instanceId": "",
        "enabled": True,
        "options": {
            "name": "Library",
            "timeout": 5000,
            "resources": ["catalog", "meta", "stream"],
            "mediaTypes": [],
            "showRefreshActions": ["catalog"],
            "skipProcessing": False,
            "hideStreams": False,
            "useMultipleInstances": False,
        },
        "category": "Library",
    },
    {
        "__if": "inputs.aiometa.aiometaUrl",
        "type": "custom",
        "instanceId": "",
        "enabled": True,
        "options": {
            "name": "AIOMetadata",
            "manifestUrl": "{{inputs.aiometa.aiometaUrl}}",
            "timeout": 5000,
            "resources": ["meta", "catalog"],
            "mediaTypes": [],
        },
        "category": "Metadata",
    },
]

# AIOStreams' config schema requires every preset to carry a unique non-empty
# instanceId (z.string().min(1)); empty strings fail validation at install time.
for _preset in presets:
    _preset["instanceId"] = str(uuid.uuid4())

config = {
    "preferredLanguages": ["English"],
    "tmdbApiKey": {"__if": "inputs.metaApis.tmdbApiKey", "__value": "{{inputs.metaApis.tmdbApiKey}}"},
    "tvdbApiKey": {"__if": "inputs.metaApis.tvdbApiKey", "__value": "{{inputs.metaApis.tvdbApiKey}}"},
    "presets": presets,
    "syncedRankedStreamExpressionUrls": [RSE_URL],
    "syncedRankedRegexUrls": [REGEX_URL],
    "sortCriteria": {
        "global": [{"key": "cached", "direction": "desc"}],
        "cached": [
            {"key": "library", "direction": "desc"},
            {"key": "service", "direction": "desc"},
            {"key": "resolution", "direction": "desc"},
            {"key": "quality", "direction": "desc"},
            {"key": "streamExpressionScore", "direction": "desc"},
            {"key": "language", "direction": "desc"},
            {"key": "encode", "direction": "desc"},
            {"key": "bitrate", "direction": "desc"},
        ],
        "uncached": [
            {"key": "resolution", "direction": "desc"},
            {"key": "quality", "direction": "desc"},
            {"key": "streamExpressionScore", "direction": "desc"},
            {"key": "language", "direction": "desc"},
            {"key": "encode", "direction": "desc"},
            {"key": "bitrate", "direction": "desc"},
        ],
    },
    "formatter": {
        "id": "custom",
        "definitions": {
            "custom": {
                "name": "{stream.title} | {stream.resolution} {stream.quality} | {stream.size} | {stream.languages} | SEL:{stream.seScore}",
                "description": "Matched: {stream.rseMatched} | {stream.visualTags} {stream.audioTags} | {stream.releaseGroup} | {stream.bitrate} | via {stream.indexer}",
            }
        },
    },
    "failover": {
        "enabled": True,
        "contentTypes": ["usenet", "debrid"],
        "allowCrossType": True,
        "maxAttempts": 5,
        "parallel": 2,
        "position": "beforeLimiting",
        "includeExternalFailover": True,
        "sameReleaseLimit": 2,
        "precacheFailover": False,
    },
    "deduplicator": {
        "enabled": True,
        "excludeAddons": [],
        "multiGroupBehaviour": "aggressive",
        "keys": ["filename", "infoHash", "smartDetect"],
        "cached": "single_result",
        "uncached": "single_result",
        "p2p": "single_result",
        "http": "per_addon",
        "smartDetectAttributes": [
            "size", "resolution", "quality", "visualTags", "audioTags",
            "audioChannels", "languages", "encode", "edition", "network",
            "remastered", "bitrate", "releaseGroup",
        ],
        "smartDetectRounding": 10,
        "libraryBehaviour": "prefer",
        "merge": {
            "enabled": True,
            "failoverVariants": True,
            "fields": ["sizes", "seadex", "library", "subtitles", "languages"],
        },
    },
    "cacheAndPlay": {"enabled": True, "streamTypes": ["usenet"]},
    "checkOwned": True,
}

template = [
    {
        "metadata": {
            "id": "evan.aiostreams.setup",
            "name": "Evan's AIOStreams Setup",
            "description": "Evan's personal AIOStreams setup: TorBox + Torrin (via StremThru), Comet/Torrentio/MediaFusion/StremThru Torz scrapers, cached-first sorting with the Library pinned high, and the Redhair777 2160p Remux SEL + regex lists synced. Indexers are managed separately (e.g. the Prowlarr marketplace addon).",
            "author": "Evan",
            "source": "custom",
            "version": TEMPLATE_VERSION,
            "category": "AIO",
            "serviceRequired": False,
            "services": ["torbox", "torrin", "aiostreams"],
            "inputs": inputs,
            "changelog": CHANGELOG,
        },
        "config": config,
    }
]

out = "/home/hatch/workspace/goals/aiostreams-importable-template/files/aiostreams-template/evan-aiostreams-template.json"
with open(out, "w") as f:
    json.dump(template, f, indent=2)
    f.write("\n")
print("wrote", out)
