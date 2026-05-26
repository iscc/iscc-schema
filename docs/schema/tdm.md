---
icon: lucide/pickaxe
title: TDM Service
description: TDM service metadata.
---

# TDM Service Metadata

Machine-readable TDM rights signals conformant with W3C TDMRep. The tdm_reservation field is semantically equivalent to TDMRep's tdm-reservation property, and tdm_policy links to an ODRL policy document. These signals are designed for use within content identification and discovery protocols that provide additional identity, provenance, and trust context.

**JSON Schema**: [`tdm.json`](tdm.json)

!!! example

    ```json
    {
      "@context": "http://purl.org/iscc/context",
      "@type": "TDM",
      "$schema": "http://purl.org/iscc/schema/tdm.json",
      "iscc": "ISCC:MAACAJINXFXA2SQX",
      "tdm_reservation": 1,
      "tdm_policy": "https://example.com/tdmrep-policy.json"
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

## **iscc**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| iscc | `string` | none | An ISCC-CODE or ISCC-ID identifying the digital content this TDM declaration applies to.<br><br>**Example**: `ISCC:MAACAJINXFXA2SQX`         |

## **tdm_reservation**
<http://www.w3.org/ns/tdmrep#reservation>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| tdm_reservation | `integer` | none | Blanket TDM reservation flag, semantically equivalent to W3C TDMRep tdm-reservation. 1 = rights reserved (EU DSM Art. 4 opt-out), 0 = not reserved, absent = undeclared.<br><br>**Example**: `1`         |

## **tdm_policy**
<http://www.w3.org/ns/tdmrep#policy>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| tdm_policy | `string-uri` | none | URL of a TDM Policy document (typically a JSON-LD ODRL Offer profiling TDMRep). Semantically equivalent to W3C TDMRep tdm-policy.<br><br>**Example**: `https://example.com/tdmrep-policy.json`         |

