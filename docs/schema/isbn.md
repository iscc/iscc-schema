---
icon: lucide/book-text
title: ISBN Seed
description: ISBN seed metadata.
---

# ISBN Seed Metadata

ISBN Seed Metadata for interoperable Meta-Code generation. See [IEP-0002](https://github.com/iscc/iscc-ieps/blob/main/ieps/iep-0002.md) for details on Meta-Code generation.

**JSON Schema**: [`isbn.json`](isbn.json)

!!! example

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

**Required fields**: `isbn`, `productform`, `title`, `language`, `imprint`, `publisher`, `country`, `pubdate`

## **@context**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @context | `string-uri` | http://purl.org/iscc/context | The JSON-LD Context URI for ISCC metadata.         |

## **@type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @type | `string` | ISBN | The type of seed metadata.         |

## **$schema**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| $schema | `string-uri` | http://purl.org/iscc/schema/isbn.json | The JSON Schema URI for ISBN seed metadata.         |

## **isbn**
<http://schema.org/isbn>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| isbn | `string` | none | International Standard Book Number in 13-digit format, without spaces or hyphens.<br><br>**Example**: `9789295055124`         |

## **productform**
<http://purl.org/iscc/terms/#productform>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| productform | `string` | none | Product form code indicating the medium and format of the publication (ONIX codelist 150).<br><br>**Example**: `EA`         |

## **title**
<http://schema.org/name>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| title | `string` | none | The title of the publication.<br><br>**Example**: `The Never Ending Story`         |

## **language**
<http://schema.org/inLanguage>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| language | `string` | none | ISO 639-2/B three-letter language code.<br><br>**Example**: `eng`         |

## **imprint**
<http://schema.org/publisherImprint>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| imprint | `string` | none | The brand name under which the publication is published.<br><br>**Example**: `Penguin Classics`         |

## **publisher**
<http://schema.org/publisher>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| publisher | `string` | none | The person or organization that owns the imprint at the date of publication.<br><br>**Example**: `Penguin Random House`         |

## **country**
<http://schema.org/countryOfOrigin>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| country | `string` | none | Country of publication in accordance with ISO 3166-1 alpha-2 country codes.<br><br>**Example**: `US`         |

## **pubdate**
<http://schema.org/datePublished>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| pubdate | `string` | none | The date of first publication under this ISBN in ISO 8601 basic format (YYYYMMDD).<br><br>**Example**: `20240214`         |

