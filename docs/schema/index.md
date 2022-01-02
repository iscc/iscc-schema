# JSON Schema for ISCC Metadata

## iscc-minimal
Minimal ISCC Metadata

??? example

    ```json
    {
      "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"
    }
    ```
### **iscc**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| iscc | `string` | **ISCC-CODE** in canonical representation. This is the minimal required field for a valid ISCC Metadata object.                     |

## iscc-basic
Basic user presentable ISCC Metadata conformant with [ERC721](https://eips.ethereum.org/EIPS/eip-721)

??? example

    ```json
    {
      "name": "The Never Ending Story",
      "description": "a 1984 fantasy film co-written and directed by *Wolfgang Petersen*",
      "image": "https://picsum.photos/200/300.jpg"
    }
    ```
### **name**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| name | `string` | The name or title of the intangible creation manifested by the idendified *digital content*.                     |

### **description**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| description | `string` | Description of the *digital content* identified by the **ISCC** (used as input for Meta-Code generation). Any user presentable text string (including Markdown text) indicative of the identity  of the referent may be used.                     |

### **image**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| image | `string-uri` | URI for a user-presentable image that serves as a preview of the *digital content*. The URI may be a Data-URL [RFC2397](https://datatracker.ietf.org/doc/html/rfc2397). If **ISCC** metadata is used as NFT metadata according to [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) or [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/) the URI should reference the actual digital content represented by the NFT.                     |

## iscc-extended
Extended ISCC Metadata

??? example

    ```json
    {
      "content": "http://example.com/the-asset.epub",
      "identifier": "urn:isbn:3-8273-7019-1",
      "creator": "Frank Fancy",
      "license": "http://example.com/license.txt",
      "redirect": "http://example.com/about-the-asset"
    }
    ```
### **content**
<contentUrl>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| content | `string-uri` | URI of the *digital content* that was used to create this ISCC.                     |

### **identifier**
<https://purl.org/iscc/context/#identifier>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| identifier | `['string', 'array']` | Other identifier(s) referencing the work, product or other abstraction of which the referenced **digital content** is a full or partial manifestation.
                     |

### **creator**
<https://purl.org/dc/elements/1.1/creator>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| creator | `['string', 'array']` | An entity primarily responsible for making the resource.                     |

### **license**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| license | `string-uri` | URI of license for the identified *digital content*.                     |

### **redirect**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| redirect | `string-uri` | URL to which a resolver should redirect an ISCC-ID that has been minted from a declartion that includes the IPFS-hash of this metadata instance.
                     |

## iscc-properties
Arbitrary properties. Values may be strings, numbers, object or arrays. Should be used for industry specific structured metadata.

??? example

    ```json
    {
      "properties": {
        "simple_property": "example value",
        "rich_property": {
          "name": "Name",
          "value": "123",
          "display_value": "123 Example Value",
          "class": "emphasis",
          "css": {
            "color": "#ffffff",
            "font-weight": "bold",
            "text-decoration": "underline"
          }
        },
        "array_property": {
          "name": "Name",
          "value": [
            1,
            2,
            3,
            4
          ],
          "class": "emphasis"
        }
      }
    }
    ```
### **properties**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| properties | `object` | JSON or JSON-LD formated values about the identified *digital content*. Compatible with [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155).                     |

## iscc-technical
Technical ISCC Metadata automaticaly inferred from the *digital content* by an ISCC Processor

??? example

    ```json
    {
      "filename": "the-file.png",
      "filesize": 46356,
      "mediatype": "image/png",
      "width": 640,
      "height": 480,
      "keywords": [
        "hashing",
        "identification"
      ]
    }
    ```
### **filename**
<https://dbpedia.org/ontology/filename>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| filename | `string` | Filename of the referenced **digital content** (automatically used as fallback if the `name` field was not specified for ISCC processing)                     |

### **filesize**
<https://dbpedia.org/ontology/fileSize>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| filesize | `integer` | File size of media asset in number of bytes.                     |

### **mediatype**
<encodingFormat>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| mediatype | `string` | [IANA Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml) (MIME type)                     |

### **duration**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| duration | `integer` | Duration of audio-visual media in secondes.                     |

### **fps**
<https://id.loc.gov/ontologies/bibframe/ProjectionSpeed>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| fps | `number-float` | Frames per second of video assets.                     |

### **width**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| width | `integer-int32` | Width of visual media in number of pixels.                     |

### **height**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| height | `integer-int32` | Height of visual media in number of pixels.                     |

### **characters**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| characters | `integer` | Number of text characters (code points after Unicode normalization)                     |

### **pages**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| pages | `integer` | Number of pages (for paged documents only)                     |

### **language**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| language | `['string', 'array']` | Language(s) of content [BCP 47](https://tools.ietf.org/search/bcp47).                     |

### **keywords**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| keywords | `array` | List of keywords relevant to the identified digital content.                     |

### **parts**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| parts | `array` | Included Content-Codes.                     |

### **features**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| features | `array` | Granular features of the *digital content*.                     |

## iscc-crypto
Cryptography related ISCC Metadata
### **datahash**
<https://purl.org/iscc/context/#datahash>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| datahash | `string` | [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).                     |

### **metahash**
<https://purl.org/iscc/context/#metahash>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| metahash | `string` | [Multihash](https://multiformats.io/multihash/) of the supplied metadata (default blake3). For deterministic results [JSC RFC5452](https://datatracker.ietf.org/doc/html/rfc8785) canonicalization is applied before hashing.                     |

### **tophash**
<https://purl.org/iscc/context/#tophash>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| tophash | `string` | [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).                     |

