---
icon: lucide/link
title: JSON-LD Contexts
description: Machine-readable JSON-LD @context documents for ISCC metadata.
---

# JSON-LD Contexts

This directory hosts the machine-readable JSON-LD `@context` documents that map ISCC metadata properties to their semantic IRIs. A JSON-LD processor dereferences a whole context document by URL. For human-readable term definitions, see the [Vocabulary](../terms/index.md) page — the `/terms/` namespace the term IRIs resolve into.

## Canonical Context

[`http://purl.org/iscc/context`](iscc.jsonld) always resolves to the latest release (currently 0.7.0).

## Versioned Contexts

Serialized ISCC records carry a version-pinned `@context`, fixing the vocabulary to a specific release:

- [`http://purl.org/iscc/context/0.7.0.jsonld`](0.7.0.jsonld) — current release
- [`http://purl.org/iscc/context/0.6.0.jsonld`](0.6.0.jsonld)
- [`http://purl.org/iscc/context/0.5.0.jsonld`](0.5.0.jsonld)
- [`http://purl.org/iscc/context/0.4.1.jsonld`](0.4.1.jsonld)
- [`http://purl.org/iscc/context/0.4.0.jsonld`](0.4.0.jsonld)
- [`http://purl.org/iscc/context/0.3.9.jsonld`](0.3.9.jsonld)
- [`http://purl.org/iscc/context/0.3.8.jsonld`](0.3.8.jsonld)
- [`http://purl.org/iscc/context/0.3.7.jsonld`](0.3.7.jsonld)
- [`http://purl.org/iscc/context/0.3.6.jsonld`](0.3.6.jsonld)
- [`http://purl.org/iscc/context/0.3.5.jsonld`](0.3.5.jsonld)
- [`http://purl.org/iscc/context/0.3.4.jsonld`](0.3.4.jsonld)
- [`http://purl.org/iscc/context/0.3.3.jsonld`](0.3.3.jsonld)
- [`http://purl.org/iscc/context/0.3.2.jsonld`](0.3.2.jsonld)
- [`http://purl.org/iscc/context/0.3.1.jsonld`](0.3.1.jsonld)
- [`http://purl.org/iscc/context/0.3.0.jsonld`](0.3.0.jsonld)
- [`http://purl.org/iscc/context/0.2.1.jsonld`](0.2.1.jsonld)
- [`http://purl.org/iscc/context/0.2.0.jsonld`](0.2.0.jsonld)
- [`http://purl.org/iscc/context/0.1.0.jsonld`](0.1.0.jsonld)

