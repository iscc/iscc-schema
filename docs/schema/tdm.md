# TDM Service Metadata

Text and Data Mining reservation metadata for AI content usage rights.

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
      "search": "open",
      "analyze": "open"
    }
    ```

**Required fields**: `train`, `inference`, `derive`, `search`, `analyze`

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
| train | `string` | none | Reservation status for AI model training. Covers pre-training, fine-tuning, RLHF, distillation, and embedding training.<br><br>**Example**: `reserved`         |

## **inference**
<http://purl.org/iscc/terms/#inference>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| inference | `string` | none | Reservation status for inference-time content retrieval. Covers RAG, grounding, fact-checking, and context augmentation.<br><br>**Example**: `open`         |

## **derive**
<http://purl.org/iscc/terms/#derive>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| derive | `string` | none | Reservation status for AI-generated derivative works. Covers summarization, translation, format adaptation, and content reformulation.<br><br>**Example**: `reserved`         |

## **search**
<http://purl.org/iscc/terms/#search>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| search | `string` | none | Reservation status for search and discovery indexing. Covers content indexing with title, snippet, and source attribution.<br><br>**Example**: `open`         |

## **analyze**
<http://purl.org/iscc/terms/#analyze>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| analyze | `string` | none | Reservation status for automated content analysis. Covers classification, sentiment analysis, topic modeling, and metadata extraction.<br><br>**Example**: `open`         |

