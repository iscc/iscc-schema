---
icon: lucide/list-checks
title: Identifiers Service
description: Asset-to-identifier discovery response for ISCC registries.
---

# Identifiers Service Metadata

Set of typed external identifiers served for an asset identified by an ISCC.

**JSON Schema**: [`identifiers.json`](identifiers.json)

!!! example

    ```json
    {
      "@context": "http://purl.org/iscc/context/0.8.0.jsonld",
      "@type": "Identifiers",
      "$schema": "http://purl.org/iscc/schema/identifiers-0.8.0.json",
      "iscc": "ISCC:MAACAJINXFXA2SQX",
      "identifier": [
        {
          "scheme": "iswc",
          "code": "T-034.524.680-1",
          "scope": "work",
          "primary": true
        },
        {
          "scheme": "isrc",
          "code": "USRC17607839",
          "scope": "manifestation"
        }
      ]
    }
    ```

**Required fields**: `identifier`

## Field Reference

## **@context**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @context | `string-uri` | http://purl.org/iscc/context | The JSON-LD Context URI for ISCC metadata.         |

## **@type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @type | `string` | Identifiers | The type of service metadata.         |

## **$schema**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| $schema | `string-uri` | http://purl.org/iscc/schema/identifiers-0.8.0.json | The JSON Schema URI for Identifiers service metadata.         |

## **iscc**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| iscc | `string` | none | An ISCC-CODE or ISCC-ID identifying the digital content these identifiers apply to. Mapped to JSON-LD @id when present; when omitted, the serving transport must preserve the asset subject out of band.<br><br>**Example**: `ISCC:MAACAJINXFXA2SQX`         |

## **identifier**
<http://schema.org/identifier>
<small>Status: **draft**</small>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| identifier | `array` | none | One or more typed external identifiers associated with the asset.         |

### **identifier item fields**

| Name | Type | Required | Definition |
| ---- | ---- | -------- | ---------- |
| scheme | `string` | yes | Lowercase token naming the identifier namespace, such as doi, isrc, iswc, isbn, issn, ror, or orcid. |
| code | `string` | yes | Identifier value within the declared scheme, normalized by the producer according to the scheme's conventions. |
| scope | `string` | no | Optional lowercase token naming the level the identifier applies to, such as work, series, manifestation, asset, organization, or person. |
| primary | `boolean` | no | Preferred identifier flag within the same scope. True means preferred; false is equivalent to omission and is normalized away by the model construction path. |

