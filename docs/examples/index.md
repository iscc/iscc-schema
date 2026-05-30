---
icon: lucide/code
title: Examples
description: Sample ISCC metadata for different use cases and schema categories.
---

# Examples

A collection of ISCC metadata samples for different use cases.

## Minimal ISCC Metadata

The simplest valid ISCC metadata, just an `iscc` field with the `$schema` reference:

```json
{
  "$schema": "http://purl.org/iscc/schema/0.7.0.json",
  "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"
}
```

## Content Description

ISCC metadata with descriptive fields for a video:

```json
{
  "@context": "http://purl.org/iscc/context/0.7.0.jsonld",
  "@type": "VideoObject",
  "$schema": "http://purl.org/iscc/schema/0.7.0.json",
  "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
  "name": "The Never Ending Story",
  "description": "a 1984 fantasy film co-written and directed by Wolfgang Petersen",
  "creator": "Wolfgang Petersen"
}
```

## Content with TDM Rights

ISCC metadata with embedded TDM (text and data mining) reservation signals:

```json
{
  "@context": "http://purl.org/iscc/context/0.7.0.jsonld",
  "@type": "CreativeWork",
  "$schema": "http://purl.org/iscc/schema/0.7.0.json",
  "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
  "name": "The Never Ending Story",
  "tdm": {
    "tdm_reservation": 1,
    "tdm_policy": "https://example.com/tdmrep-policy.json"
  }
}
```

## ISBN Seed Metadata

Seed metadata for interoperable Meta-Code generation from book industry data. The `$schema`
reference makes the data self-describing - any consumer can recover the full JSON-LD context from
the schema on demand (see [Schema-Driven Context Recovery](#schema-driven-context-recovery)):

```json
{
  "$schema": "http://purl.org/iscc/schema/isbn-0.7.0.json",
  "isbn": "9789295055124",
  "productform": "EA",
  "title": "The Never Ending Story",
  "language": "eng",
  "imprint": "Penguin Classics",
  "publisher": "Penguin Random House",
  "country": "US",
  "pubdate": "20240214"
}
```

## ISRC Seed Metadata

Seed metadata for interoperable Meta-Code generation from sound recording data. Like ISBN seed
metadata, the `$schema` reference enables JSON-LD context recovery without carrying the full
context in every object:

```json
{
  "$schema": "http://purl.org/iscc/schema/isrc-0.7.0.json",
  "isrc": "AA6Q72000047",
  "main_artist": "The Beatles",
  "track_title": "Yesterday",
  "version_title": "Remastered 2009",
  "duration": 125,
  "content_type": "sound",
  "pubdate": "20090909"
}
```

## STM Seed Metadata

Seed metadata for DOI-identified scholarly works (scientific, technical, medical), populated from
Crossref/DataCite records for interoperable Meta-Code generation:

```json
{
  "$schema": "http://purl.org/iscc/schema/stm-0.7.0.json",
  "doi": "10.5555/example.2020.0001",
  "resource_type": "JournalArticle",
  "title": "On the Stability of Quasilinear Forms",
  "publisher": "Meridian Academic Press",
  "pubyear": 2020,
  "version_type": "VoR",
  "container_title": "Journal of Applied Analysis",
  "issn": "1234-5678"
}
```

## TDM Service Metadata

Standalone TDM reservation signals served by an ISCC registry:

```json
{
  "@context": "http://purl.org/iscc/context/0.7.0.jsonld",
  "@type": "TDM",
  "$schema": "http://purl.org/iscc/schema/tdm-0.7.0.json",
  "iscc": "ISCC:MAACAJINXFXA2SQX",
  "tdm_reservation": 1,
  "tdm_policy": "https://example.com/tdmrep-policy.json"
}
```

## GenAI Service Metadata

Standalone generative AI disclosure signals for content transparency:

```json
{
  "@context": "http://purl.org/iscc/context/0.7.0.jsonld",
  "@type": "GenAI",
  "$schema": "http://purl.org/iscc/schema/genai-0.7.0.json",
  "involvement": "ai_generated",
  "ai_system": "DALL-E 3",
  "digital_source_type": "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"
}
```

## IsccNote Protocol Record

A permanent ISCC Declaration log record for ISCC-HUB timestamping. Protocol records default to
compact JSON with a version-specific `$schema` as the sole version anchor:

```json
{
  "$schema": "http://purl.org/iscc/schema/iscc-note-0.7.0.json",
  "iscc_code": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
  "datahash": "1e20253d0f3460085c276f038de345c8e953a306f4a07f9fa77f5af8563c3d7274c5",
  "nonce": "0013a3c214c05796673503e6e549446d",
  "signature": {
    "version": "ISCC-SIG v1.0",
    "controller": "did:web:example.com",
    "pubkey": "z6MkmeDbeC5BecFmVnTHA5PWEBaVUrGLdB3weGE2KYnXfHso",
    "proof": "z5j9nrpPw3oYSAN4XbCvk2sUtkwrueTD6V2Y35gS1KFTode2ED2YQWokPmoXw6QBYtYEFxtAQfzBhdNyr8PMwP79G"
  }
}
```

## Schema-Driven Context Recovery

Plain JSON data can be upgraded to JSON-LD using `recover_context()`. The function reads the
`$schema` reference and injects the matching `@context`:

```python
from iscc_schema import recover_context

# Plain JSON without @context
data = {
    "$schema": "http://purl.org/iscc/schema/0.7.0.json",
    "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
    "name": "The Never Ending Story",
}

# Recover JSON-LD context from the schema reference
result = recover_context(data)

# Result is now valid JSON-LD
assert "@context" in result
```

When `$schema` is absent, context can be recovered from `@type`:

```python
from iscc_schema import recover_context

data = {"@type": "ISBN", "isbn": "9789295055124"}
result = recover_context(data)
assert "@context" in result
```

## Python Usage

Creating and serializing ISCC metadata objects:

```python
from iscc_schema import IsccMeta

meta = IsccMeta(
    iscc="ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
    name="The Never Ending Story",
)

# Dict serialization (set fields only)
meta.dict()
# {'iscc': 'ISCC:KACY...', 'name': 'The Never Ending Story'}

# JSON serialization (includes schema defaults)
meta.json()
# '{"@context":"http://purl.org/iscc/context/0.7.0.jsonld","@type":"CreativeWork","$schema":"http://purl.org/iscc/schema/0.7.0.json",...}'

# JCS canonical bytes (deterministic, for hashing)
meta.jcs()
# b'{"$schema":"http://purl.org/iscc/schema/0.7.0.json","@context":...}'
```

Seed metadata defaults to compact JSON (`ld=False`), service metadata to full JSON-LD
(`ld=True`). All methods accept an `ld` parameter to override:

```python
from iscc_schema import ISBN, TDM

seed = ISBN(
    isbn="9789295055124",
    productform="EA",
    title="The Never Ending Story",
    language="eng",
    imprint="Penguin Classics",
    publisher="Penguin Random House",
    country="US",
    pubdate="20240214",
)

# Compact by default for seed metadata
seed.json()
# '{"$schema":"http://purl.org/iscc/schema/isbn-0.7.0.json","isbn":"9789295055124",...}'

# Full JSON-LD when needed
seed.json(ld=True)
# '{"@context":"http://purl.org/iscc/context/0.7.0.jsonld","@type":"ISBN","$schema":...}'

# Service metadata defaults to full JSON-LD
tdm = TDM(iscc="ISCC:MAACAJINXFXA2SQX", tdm_reservation=1)
tdm.json()
# '{"@context":"http://purl.org/iscc/context/0.7.0.jsonld","@type":"TDM",...}'
```
