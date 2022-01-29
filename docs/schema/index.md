# JSON Schema for ISCC Metadata

## iscc-jsonld
The ISCC [JSON-LD](https://json-ld.org/) Context and [JSON Schema](https://json-schema.org/) reference
### **@context**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @context | `string-uri` | http://purl.org/iscc/context | The [JSON-LD](https://json-ld.org/) Context URI for ISCC metadata.         |

### **@type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @type | `string` | CreativeWork | The type of digital content according to schema.org classes (TextDigitalDocument, ImageObject, AudioObject, VideoObject).         |

### **$schema**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| $schema | `string-uri` | http://purl.org/iscc/schema | The [JSON Schema](https://json-schema.org/) URI for ISCC metadata.         |

## iscc-minimal
Minimal required ISCC Metadata

!!! example

    ```json
    {
      "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"
    }
    ```
### **iscc**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| iscc | `string` | none | An **ISCC-CODE** in canonical representation. This is the minimal required field for a valid ISCC Metadata object.<br><br>**Example**: `ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY`         |

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

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| name | `string` | none | The title or name of the intangible creation manifested by the identified *digital content* (used as input for **ISCC Meta-Code** generation).<br><br>**Example**: `The Never Ending Story`         |

### **description**
<http://schema.org/disambiguatingDescription>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| description | `string` | none | Description of the *digital content* identified by the **ISCC** (used as input for Meta-Code generation). Any user presentable text string (including Markdown text) indicative of the identity  of the referent may be used.<br><br>**Example**: `a 1984 fantasy film co-written and directed by *Wolfgang Petersen*`         |

### **metadata**
<http://purl.org/iscc/terms/#metadata>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| metadata | `None` | none | Descriptive, industry-sector or use-case specific metadata. Can be any object that is JSON/JCS serializable. If `metadata` is provided it is used as an input for Meta-Code generation and as the sole input for the cryptographic `metahash` calculation. If `metadata` is set to a string it is assumed that it is base64 encoded binary file metadata.         |

### **image**
<http://schema.org/image>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| image | `string-uri` | none | URI for a user-presentable image that serves as a preview of the *digital content*. The URI may be a Data-URL [RFC2397](https://datatracker.ietf.org/doc/html/rfc2397). If **ISCC** metadata is used as NFT metadata according to [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) or [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/) the URI should reference the actual digital content represented by the NFT.<br><br>**Example**: `https://picsum.photos/200/300.jpg`         |

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
### **identifier**
<http://schema.org/identifier>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| identifier | `['string', 'array']` | none | Other identifier(s) referencing the work, product or other abstraction of which the referenced **digital content** is a full or partial manifestation.         |

### **content**
<http://schema.org/contentUrl>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| content | `string-uri` | none | URI of the *digital content* that was used to create this ISCC.         |

### **creator**
<http://schema.org/creator>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| creator | `['string', 'array']` | none | An entity primarily responsible for making the resource.<br><br>**Example**: `Joanne K. Rowling`         |

### **acquire**
<http://schema.org/acquireLicensePage>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| acquire | `string-uri` | none | This field must contain a valid URL referring to a page showing information about how one can acquire a license for the item. This may be a page of a web shop or NFT marketplace ready for providing a license.<br><br>**Example**: `https://example.com/buy-license-for-item-here`         |

### **credit**
<http://schema.org/creditText>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| credit | `string` | none | A line of text that the supplier expects users of the image (such as Google Images) to display to users alongside the image.<br><br>**Example**: `Frank Farian - Getty Images`         |

### **rights**
<http://schema.org/copyrightNotice>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| rights | `string` | none | Contains any necessary copyright notice and should identify the current owner of the copyright of this work with associated intellectual property rights.<br><br>**Example**: `© Copyright 2022 ISCC Foundation - www.iscc.codes`         |

### **keywords**
<http://schema.org/keywords>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| keywords | `string` | none | Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.         |

### **license**
<http://schema.org/license>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| license | `string-uri` | none | URI of license for the identified *digital content*.<br><br>**Example**: `https://example.com/license-terms-for-this-item`         |

### **redirect**
<http://purl.org/iscc/terms/#redirect>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| redirect | `string-uri` | none | URL to which a resolver should redirect an ISCC-ID that has been minted from a declartion that includes the IPFS-hash of this metadata instance.<br><br>**Example**: `https://example.com/land-here-when-resolving-iscc-id`         |

### **previous**
<http://purl.org/iscc/terms/#previous>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| previous | `string` | none | ISCC of the preceding version of this item.         |

### **version**
<http://schema.org/version>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| version | `['integer', 'string']` | none | The version of the CreativeWork embodied by a specified resource.         |

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

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| created | `string-date-time` | none | Datetime the ISCC was created for the item.         |

### **filename**
<http://purl.org/iscc/terms/#filename>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| filename | `string` | none | Filename of the referenced **digital content** (automatically used as fallback if the `name` field was not specified for ISCC processing)         |

### **filesize**
<http://schema.org/fileSize>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| filesize | `integer` | none | File size of media asset in number of bytes.         |

### **mediatype**
<http://schema.org/encodingFormat>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| mediatype | `string` | none | An [IANA Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml) (MIME type)<br><br>**Example**: `image/png`         |

### **duration**
<http://schema.org/duration>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| duration | `integer` | none | Duration of audio-visual media in secondes.         |

### **fps**
<http://purl.org/iscc/terms/#fps>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| fps | `number-float` | none | Frames per second of video assets.<br><br>**Example**: `24`         |

### **width**
<http://purl.org/iscc/terms/#width>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| width | `integer-int32` | none | Width of visual media in number of pixels.<br><br>**Example**: `640`         |

### **height**
<http://purl.org/iscc/terms/#height>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| height | `integer-int32` | none | Height of visual media in number of pixels.<br><br>**Example**: `480`         |

### **characters**
<http://purl.org/iscc/terms/#characters>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| characters | `integer` | none | Number of text characters (code points after Unicode normalization)<br><br>**Example**: `55689`         |

### **pages**
<http://schema.org/numberOfPages>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| pages | `integer` | none | Number of pages (for paged documents only)<br><br>**Example**: `77`         |

### **language**
<http://schema.org/inLanguage>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| language | `None` | none | Language(s) of content [BCP 47](https://tools.ietf.org/search/bcp47).<br><br>**Example**: `en-US`         |

### **parts**
<http://purl.org/iscc/terms/#parts>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| parts | `array` | none | Indicates items that are part of this item via Content-Codes (inverse-property belongs).         |

### **part_of**
<http://purl.org/iscc/terms/#part_of>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| part_of | `array` | none | Indicates that this item is part of other items via their Content-Code.         |

### **features**
<http://purl.org/iscc/terms/#features>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| features | `array` | none | Granular features of the *digital content*.         |

### **generator**
<http://purl.org/iscc/terms/#generator>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| generator | `string` | none | Name and version of the software that generated the ISCC         |

## iscc-nft
Metadata for NFT Marketplaces
### **external_url**
<http://purl.org/iscc/terms/#external_url>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| external_url | `string-uri` | none | This is the URL that will appear below the asset's image on some NFT Marketplaces and will allow users to leave the site and view the item on your site.         |

### **animation_url**
<http://purl.org/iscc/terms/#animation_url>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| animation_url | `string-uri` | none | A URL to a multi-media attachment for the item.         |

### **properties**
<http://purl.org/iscc/terms/#properties>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| properties | `None` | none | Descriptive, industry-sector or use-case specific metadata. Can be any object that is JSON/JCS serializable. If properties are provided they are the sole input for the cryptographic `metahash` calculation. Also compatible with [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155). If properties is set to a string it is assumed that it is base64 encoded binary file metadata.         |

## iscc-crypto
Cryptography related ISCC Metadata
### **tophash**
<http://purl.org/iscc/terms/#tophash>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| tophash | `string` | none | A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).         |

### **metahash**
<http://purl.org/iscc/terms/#metahash>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| metahash | `string` | none | A [Multihash](https://multiformats.io/multihash/) of the supplied metadata (default blake3). The hash is created from `name` and `description` fields or `properties` if supplied. For deterministic results [JSC RFC5452](https://datatracker.ietf.org/doc/html/rfc8785) canonicalization is applied to `properties` before hashing if it is a JSON object.         |

### **datahash**
<http://purl.org/iscc/terms/#datahash>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| datahash | `string` | none | A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).         |

## iscc-chains
Chains that support ISCC Declarations
### **chain_id**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| chain_id | `number` | none | Unique identifier of supported chain         |

