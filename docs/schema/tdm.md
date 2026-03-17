---
icon: lucide/pickaxe
title: TDM Service
description: TDM service metadata.
---

# TDM Service Metadata

Machine-readable TDM reservation signals for AI-related content usage categories. A 'reserved' status indicates an explicit opt-out from TDM exceptions (e.g., EU DSM Directive Art. 4). An 'open' status indicates that no rights are reserved. Omitted fields indicate that the reservation status has not been determined. These signals are designed for use within content identification and discovery protocols that provide additional identity, provenance, and trust context.

**JSON Schema**: [`tdm.json`](tdm.json)

!!! example

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

## **@context**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @context | `string-uri` | http://purl.org/iscc/context | The JSON-LD Context URI for ISCC metadata.         |

## **@type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @type | `string` | TDM | The type of service metadata.         |

## **$schema**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| $schema | `string-uri` | http://purl.org/iscc/schema/tdm.json | The JSON Schema URI for TDM service metadata.         |

## **train**
<http://purl.org/iscc/terms/#train>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| train | `string` | none | TDM reservation status for AI model training. Covers pre-training, fine-tuning, RLHF, distillation, and embedding training.<br><br>**Example**: `reserved`         |

## **inference**
<http://purl.org/iscc/terms/#inference>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| inference | `string` | none | TDM reservation status for inference-time content retrieval. Covers RAG, grounding, fact-checking, and context augmentation.<br><br>**Example**: `open`         |

## **derive**
<http://purl.org/iscc/terms/#derive>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| derive | `string` | none | TDM reservation status for AI-assisted content transformation. Covers summarization, translation, format adaptation, and content reformulation.<br><br>**Example**: `reserved`         |

## **search**
<http://purl.org/iscc/terms/#search>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| search | `string` | none | TDM reservation status for search and discovery indexing. Covers content indexing with title, snippet, and source attribution.<br><br>**Example**: `open`         |

## **analyze**
<http://purl.org/iscc/terms/#analyze>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| analyze | `string` | none | TDM reservation status for automated content analysis. Covers classification, sentiment analysis, topic modeling, and metadata extraction.<br><br>**Example**: `open`         |

