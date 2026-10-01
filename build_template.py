#!/usr/bin/env python3
"""Builds evan-aiostreams-template.json — Evan's AIOStreams config template."""
import json
import uuid

RSE_URL = "https://raw.githubusercontent.com/redhair777/aio-quality-profiles/main/profiles/2160p-remux.expressions.json"
REGEX_URL = "https://raw.githubusercontent.com/redhair777/aio-quality-profiles/main/profiles/2160p-remux.regexes.json"

def nab_endpoint(id, name, description, url_label, url_default=None, url_options=None):
    """A nab-endpoint input: renders URL + API key with a server-side test button.

    Holds its value as an object {url, apiKey}; referenced in config with dot
    notation, e.g. {{inputs.indexers.nzbnest}} or inputs.indexers.nzbnest.apiKey.
    """
    url_sub = {
        "id": "url",
        "name": url_label,
        "description": "Full Newznab API endpoint URL, usually ending in /api.",
        "type": "select-with-custom" if url_options else "url",
        "required": False,
    }
    if url_options:
        url_sub["options"] = url_options
    if url_default:
        url_sub["default"] = url_default
    return {
        "id": id,
        "name": name,
        "description": description,
        "type": "nab-endpoint",
        "required": False,
        "nab": {"namespace": "newznab"},
        "subOptions": [
            url_sub,
            {
                "id": "apiKey",
                "name": "API Key",
                "description": f"Your {name} API key. Leave blank to skip {name}.",
                "type": "password",
                "required": False,
            },
        ],
    }


inputs = [
    {
        "id": "indexers",
        "name": "Usenet Indexers",
        "description": "NZBNest and Hashnab Newznab indexers. Each indexer is added twice — once for ID-based (Auto) search and once for title-text (Query) search — so NZBs surface whether or not the indexer supports ID lookups. Fill in an API key to include that indexer; leave it blank to skip it.",
        "type": "subsection",
        "required": False,
        "subOptions": [
            nab_endpoint(
                "nzbnest",
                "NZBNest",
                "NZBNest Newznab indexer.",
                "NZBNest URL",
                url_default="https://nzbnest.com/api",
                url_options=[
                    {
                        "label": "NzbNest",
                        "value": "https://nzbnest.com/api",
                        "apiKeyUrl": "https://nzbnest.com/profile",
                    }
                ],
            ),
            nab_endpoint(
                "hashnab",
                "Hashnab",
                "Hashnab Newznab indexer.",
                "Hashnab URL",
            ),
        ],
    },
    {
        "id": "indexerNote",
        "name": "NNTP providers",
        "description": "Usenet results are fetched through the built-in AIOStreams NNTP engine, so add your NNTP providers under Dashboard -> Usenet -> Providers after applying (providers are instance-level and cannot be part of a template).",
        "type": "alert",
        "intent": "info",
    },
    {
        "id": "localAddons",
        "name": "Local Addons",
        "description": "Zilean runs on alderaan. Leave the URL as-is unless it moved.",
        "type": "subsection",
        "required": False,
        "subOptions": [
            {
                "id": "zileanUrl",
                "name": "Zilean URL",
                "description": "Base URL of your Zilean instance.",
                "type": "url",
                "required": False,
                "default": "http://192.168.68.64:8181",
            },
        ],
    },
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


def newznab_preset(name, input_path):
    return {
        "__if": f"inputs.{input_path}.apiKey",
        "type": "newznab",
        "instanceId": "",
        "enabled": True,
        "options": {
            "name": name,
            "api": "{{inputs." + input_path + "}}",
            "timeout": 15000,
            "mediaTypes": [],
            "services": ["aiostreams"],
            "searchMode": "both",
            "seasonEpisodeStrategy": "dynamic",
            "paginate": True,
            "useMultipleInstances": False,
        },
        "category": "Usenet",
    }


presets = [
    newznab_preset("NZBNest", "indexers.nzbnest"),
    newznab_preset("Hashnab", "indexers.hashnab"),
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
        "type": "zilean",
        "instanceId": "",
        "enabled": True,
        "options": {
            "name": "Zilean",
            "url": "{{inputs.localAddons.zileanUrl}}",
            "timeout": 5000,
            "mediaTypes": [],
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
            "showRefreshActions": True,
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
            "description": "Evan's personal AIOStreams setup: TorBox + Torrin (via StremThru) + Usenet through the built-in NNTP engine, NZBNest and Hashnab Newznab indexers, Comet/Torrentio/MediaFusion/StremThru Torz scrapers, Zilean on alderaan, cached-first sorting with the Library pinned high, and the Redhair777 2160p Remux SEL + regex lists synced.",
            "author": "Evan",
            "source": "custom",
            "version": "1.0.0",
            "category": "AIO",
            "serviceRequired": False,
            "services": ["torbox", "torrin", "aiostreams"],
            "inputs": inputs,
        },
        "config": config,
    }
]

out = "/home/hatch/workspace/goals/aiostreams-importable-template/files/aiostreams-template/evan-aiostreams-template.json"
with open(out, "w") as f:
    json.dump(template, f, indent=2)
    f.write("\n")
print("wrote", out)
