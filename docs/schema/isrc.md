# ISRC Seed Metadata

ISRC Seed Metadata for interoperable Meta-Code generation. See [IEP-0002](https://github.com/iscc/iscc-ieps/blob/main/ieps/iep-0002.md) for details on Meta-Code generation.

**JSON Schema**: [`isrc.json`](isrc.json)

!!! example

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

**Required fields**: `isrc`, `main_artist`, `track_title`, `version_title`, `duration`, `content_type`, `pubdate`

## **@context**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @context | `string-uri` | http://purl.org/iscc/context | The JSON-LD Context URI for ISCC metadata.         |

## **@type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @type | `string` | ISRC | The type of seed metadata.         |

## **$schema**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| $schema | `string-uri` | http://purl.org/iscc/schema/isrc.json | The JSON Schema URI for ISRC seed metadata.         |

## **isrc**
<http://schema.org/isrcCode>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| isrc | `string` | none | The International Standard Recording Code assigned to this recording.<br><br>**Example**: `AA6Q72000047`         |

## **main_artist**
<http://schema.org/byArtist>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| main_artist | `string` | none | The name of the featured artist or band.<br><br>**Example**: `The Beatles`         |

## **track_title**
<http://schema.org/name>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| track_title | `string` | none | The title of the recording.<br><br>**Example**: `Yesterday`         |

## **version_title**
<http://schema.org/alternativeHeadline>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| version_title | `string` | none | Additional information about the recording, such as 'live' or 'remastered'.<br><br>**Example**: `Remastered 2009`         |

## **duration**
<http://schema.org/duration>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| duration | `integer` | none | The elapsed playing time of the recording in seconds.<br><br>**Example**: `125`         |

## **content_type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| content_type | `string` | none | Indicates whether the recording is a sound recording or music video recording.<br><br>**Example**: `sound`         |

## **pubdate**
<http://schema.org/datePublished>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| pubdate | `string` | none | The date of first publication of the recording in ISO 8601 basic format (YYYYMMDD).<br><br>**Example**: `20090909`         |

