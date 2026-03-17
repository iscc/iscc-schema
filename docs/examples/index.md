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
  "$schema": "http://purl.org/iscc/schema",
  "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"
}
```

## Content Description

ISCC metadata with descriptive fields for a video:

```json
{
  "@context": "http://purl.org/iscc/context",
  "@type": "VideoObject",
  "$schema": "http://purl.org/iscc/schema",
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
  "@context": "http://purl.org/iscc/context",
  "@type": "CreativeWork",
  "$schema": "http://purl.org/iscc/schema",
  "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
  "name": "The Never Ending Story",
  "tdm": {
    "train": "reserved",
    "inference": "open",
    "derive": "reserved",
    "search": "open"
  }
}
```

## ISBN Seed Metadata

Seed metadata for interoperable Meta-Code generation from book industry data:

```json
{
  "@context": "http://purl.org/iscc/context",
  "@type": "ISBN",
  "$schema": "http://purl.org/iscc/schema/isbn.json",
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

Seed metadata for interoperable Meta-Code generation from sound recording data:

```json
{
  "@context": "http://purl.org/iscc/context",
  "@type": "ISRC",
  "$schema": "http://purl.org/iscc/schema/isrc.json",
  "isrc": "AA6Q72000047",
  "main_artist": "The Beatles",
  "track_title": "Yesterday",
  "version_title": "Remastered 2009",
  "duration": 125,
  "content_type": "sound",
  "pubdate": "20090909"
}
```

## TDM Service Metadata

Standalone TDM reservation signals served by an ISCC registry:

```json
{
  "@context": "http://purl.org/iscc/context",
  "@type": "TDM",
  "$schema": "http://purl.org/iscc/schema/tdm.json",
  "train": "reserved",
  "inference": "open",
  "derive": "reserved",
  "search": "open"
}
```

## GenAI Service Metadata

Standalone generative AI disclosure signals for content transparency:

```json
{
  "@context": "http://purl.org/iscc/context",
  "@type": "GenAI",
  "$schema": "http://purl.org/iscc/schema/genai.json",
  "involvement": "ai_generated",
  "ai_system": "DALL-E 3",
  "digital_source_type": "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"
}
```

## Schema-Driven Context Recovery

Plain JSON data can be upgraded to JSON-LD using `recover_context()`. The function reads the
`$schema` reference and injects the matching `@context`:

```python
from iscc_schema import recover_context

# Plain JSON without @context
data = {
    "$schema": "http://purl.org/iscc/schema",
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
# '{"@context":"http://purl.org/iscc/context","@type":"CreativeWork",...}'

# JCS canonical bytes (deterministic, for hashing)
meta.jcs()
# b'{"$schema":"http://purl.org/iscc/schema","@context":...}'
```

Working with seed and service metadata:

```python
from iscc_schema import ISBN, TDM, GenAI

# Create seed metadata
seed = ISBN(
    isbn="9789295055124",
    title="The Never Ending Story",
    language="eng",
    publisher="Penguin Random House",
)

# Create service metadata
tdm = TDM(train="reserved", inference="open")
genai = GenAI(involvement="ai_generated", ai_system="DALL-E 3")
```
