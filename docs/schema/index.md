# JSON Schema for ISCC Metadata

## iscc-minimal
Minimal ISCC Metadata

!!! example

    ```json
    {
      "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"
    }
    ```
### **iscc**

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| iscc | `string` | An **ISCC-CODE** in canonical representation. This is the minimal required field for a valid ISCC Metadata object.                     |

## iscc-basic
Basic user presentable ISCC Metadata conformant with [ERC721](https://eips.ethereum.org/EIPS/eip-721)

!!! example

    ```json
    {
      "name": "The Never Ending Story",
      "description": "a 1984 fantasy film co-written and directed by *Wolfgang Petersen*",
      "image": "https://picsum.photos/200/300.jpg"
    }
    ```
### **name**
<http://schema.org/name>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| name | `string` | The title or name of the intangible creation manifested by the identified *digital content* (used as input for **ISCC Meta-Code** generation).                     |

### **description**
<http://schema.org/disambiguatingDescription>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| description | `string` | Description of the *digital content* identified by the **ISCC** (used as input for Meta-Code generation). Any user presentable text string (including Markdown text) indicative of the identity  of the referent may be used.                     |

### **image**
<http://schema.org/image>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| image | `string-uri` | URI for a user-presentable image that serves as a preview of the *digital content*. The URI may be a Data-URL [RFC2397](https://datatracker.ietf.org/doc/html/rfc2397). If **ISCC** metadata is used as NFT metadata according to [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) or [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/) the URI should reference the actual digital content represented by the NFT.                     |

## iscc-extended
Extended ISCC Metadata

!!! example

    ```json
    {
      "content": "https://example.com/the-asset.epub",
      "identifier": "urn:isbn:3-8273-7019-1",
      "creator": "Frank Fancy",
      "license": "https://example.com/license.txt",
      "redirect": "https://example.com/about-the-asset"
    }
    ```
### **content**
<http://schema.org/contentUrl>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| content | `string-uri` | URI of the *digital content* that was used to create this ISCC.                     |

### **creator**
<http://schema.org/creator>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| creator | `['string', 'array']` | An entity primarily responsible for making the resource.                     |

### **keywords**
<http://schema.org/keywords>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| keywords | `string` | Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.                     |

### **identifier**
<http://schema.org/identifier>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| identifier | `['string', 'array']` | Other identifier(s) referencing the work, product or other abstraction of which the referenced **digital content** is a full or partial manifestation.                     |

### **license**
<http://schema.org/license>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| license | `string-uri` | URI of license for the identified *digital content*.                     |

### **redirect**
<http://purl.org/iscc/terms/#redirect>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| redirect | `string-uri` | URL to which a resolver should redirect an ISCC-ID that has been minted from a declartion that includes the IPFS-hash of this metadata instance.                     |

### **previous**
<http://purl.org/iscc/terms/#previous>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| previous | `string` | ISCC of the preceding version of this item.                     |

### **version**
<http://schema.org/version>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| version | `['integer', 'string']` | The version of the CreativeWork embodied by a specified resource.                     |

## iscc-properties
Arbitrary properties. Values may be strings, numbers, object or arrays. Should be used for industry specific structured metadata.

!!! example

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
<http://purl.org/iscc/terms/#properties>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| properties | `object` | Descriptive, industry-sector or use-case specific metadata in JSON or JSON-LD format. If properties are provided they are the sole inpute for `metahash` calculation. Also compatible with [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155).                     |

## iscc-technical
Technical ISCC Metadata automaticaly inferred from the *digital content* by an ISCC Processor

!!! example

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
### **created**
<http://schema.org/dateCreated>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| created | `string-date-time` | Datetime the ISCC was created for the item.                     |

### **filename**
<http://purl.org/iscc/terms/#filename>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| filename | `string` | Filename of the referenced **digital content** (automatically used as fallback if the `name` field was not specified for ISCC processing)                     |

### **filesize**
<http://schema.org/fileSize>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| filesize | `integer` | File size of media asset in number of bytes.                     |

### **mediatype**
<http://schema.org/encodingFormat>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| mediatype | `string` | An [IANA Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml) (MIME type)                     |

### **duration**
<http://schema.org/duration>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| duration | `integer` | Duration of audio-visual media in secondes.                     |

### **fps**
<http://purl.org/iscc/terms/#fps>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| fps | `number-float` | Frames per second of video assets.                     |

### **width**
<http://purl.org/iscc/terms/#width>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| width | `integer-int32` | Width of visual media in number of pixels.                     |

### **height**
<http://purl.org/iscc/terms/#height>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| height | `integer-int32` | Height of visual media in number of pixels.                     |

### **characters**
<http://purl.org/iscc/terms/#characters>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| characters | `integer` | Number of text characters (code points after Unicode normalization)                     |

### **pages**
<http://schema.org/numberOfPages>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| pages | `integer` | Number of pages (for paged documents only)                     |

### **language**
<http://schema.org/inLanguage>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| language | `None` | Language(s) of content [BCP 47](https://tools.ietf.org/search/bcp47).                     |

### **parts**
<http://purl.org/iscc/terms/#parts>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| parts | `array` | Indicates items that are part of this item via Content-Codes (inverse-property belongs).                     |

### **part_of**
<http://purl.org/iscc/terms/#part_of>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| part_of | `array` | Indicates that this item is part of other items via their Content-Code.                     |

### **features**
<http://purl.org/iscc/terms/#features>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| features | `array` | Granular features of the *digital content*.                     |

### **generator**
<http://purl.org/iscc/terms/#generator>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| generator | `string` | Name and version of the software that generated the ISCC                     |

## iscc-crypto
Cryptography related ISCC Metadata
### **datahash**
<http://purl.org/iscc/terms/#datahash>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| datahash | `string` | A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).                     |

### **metahash**
<http://purl.org/iscc/terms/#metahash>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| metahash | `string` | A [Multihash](https://multiformats.io/multihash/) of the supplied metadata (default blake3). For deterministic results [JSC RFC5452](https://datatracker.ietf.org/doc/html/rfc8785) canonicalization is applied before hashing.                     |

### **tophash**
<http://purl.org/iscc/terms/#tophash>

| Name | Type | Definition                               |
| ---- | ---- | -----------------------------------------|
| tophash | `string` | A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).                     |

