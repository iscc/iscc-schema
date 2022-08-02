# JSON Schema for ISCC Metadata

## iscc-jsonld
The ISCC [JSON-LD](https://json-ld.org/) Context and [JSON Schema](https://json-schema.org/) reference
### **@context**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @context | `string-uri` | http://purl.org/iscc/context/0.4.0.jsonld | The [JSON-LD](https://json-ld.org/) Context URI for ISCC metadata.         |

### **@type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @type | `string` | CreativeWork | The type of digital content according to schema.org classes (TextDigitalDocument, ImageObject, AudioObject, VideoObject).         |

### **$schema**
<http://purl.org/iscc/terms/#$schema>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| $schema | `string-uri` | http://purl.org/iscc/schema/0.4.0.json | The [JSON Schema](https://json-schema.org/) URI for ISCC metadata.         |

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
Basic user presentable ISCC Metadata essential for Meta-Code and Meta-Hash generation.

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
| name | `string` | none | The title or name of the intangible creation manifested by the identified *digital content*. **Used as input for ISCC Meta-Code generation**.<br><br>**Example**: `The Never Ending Story`         |

### **description**
<http://schema.org/disambiguatingDescription>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| description | `string` | none | Description of the *digital content* identified by the **ISCC**. **Used as input for ISCC Meta-Code generation**. Any user presentable text string (including Markdown text) indicative of the identity  of the referent may be used.<br><br>**Example**: `a 1984 fantasy film co-written and directed by *Wolfgang Petersen*`         |

### **meta**
<http://purl.org/iscc/terms/#meta>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| meta | `string` | none | Subject, industry, or use-case specific metadata, encoded as JSON string or Data-URL (used as sole input for Meta-Code and `metahash` generation if supplied).<br><br>**Example**: `data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0=`         |

## iscc-embeddable
Metadata intended to be embedded into the media asset.
### **creator**
<http://schema.org/creator>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| creator | `None` | none | An entity primarily responsible for making the resource.<br><br>**Example**: `Joanne K. Rowling`         |

### **license**
<http://schema.org/license>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| license | `string-uri` | none | URI of license for the identified *digital content*.<br><br>**Example**: `https://example.com/license-terms-for-this-item`         |

### **acquire**
<http://schema.org/acquireLicensePage>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| acquire | `string-uri` | none | This field must contain a valid URL referring to a page showing information about how one can acquire a license for the item. This may be a page of a web shop or NFT marketplace ready for providing a license.<br><br>**Example**: `https://example.com/buy-license-for-item-here`         |

### **credit**
<http://schema.org/creditText>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| credit | `string` | none | A line of text that you expect users of the image (such as Google Images) to display alongside the image.<br><br>**Example**: `Frank Farian - Getty Images`         |

### **rights**
<http://schema.org/copyrightNotice>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| rights | `string` | none | Contains any necessary copyright notice and should identify the current owner of the copyright of this work with associated intellectual property rights.<br><br>**Example**: `© Copyright 2022 ISCC Foundation - www.iscc.codes`         |

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
### **media_id**
<http://schema.org/identifier>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| media_id | `string` | none | Vendor specific (internal) identifier for the source media file.<br><br>**Example**: `05VQ3BGTGFCJA`         |

### **iscc_id**
<http://schema.org/identifier>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| iscc_id | `string` | none | The **ISCC-ID** of the digital content in canonical representation.<br><br>**Example**: `ISCC:MAACAJINXFXA2SQX`         |

### **image**
<http://schema.org/image>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| image | `string-uri` | none | URI for a user-presentable image that serves as a preview of the *digital content*. The URI may be a Data-URL [RFC2397](https://datatracker.ietf.org/doc/html/rfc2397). If **ISCC** metadata is used as NFT metadata according to [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) or [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/) the URI should reference the actual digital content represented by the NFT.<br><br>**Example**: `https://picsum.photos/200/300.jpg`         |

### **identifier**
<http://schema.org/identifier>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| identifier | `None` | none | Other identifier(s) referencing the work, product or other abstraction of which the referenced **digital content** is a full or partial manifestation.         |

### **content**
<http://schema.org/contentUrl>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| content | `string-uri` | none | URI of the *digital content* that was used to create this ISCC.         |

### **keywords**
<http://schema.org/keywords>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| keywords | `None` | none | Keywords or tags used to describe this content. Either a list of keywords or a sting with comma separated keywords.         |

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
### **mode**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| mode | `string` | none | The perceptual mode used to create the ISCC-CODE.<br><br>**Example**: `video`         |

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

### **thumbnail**
<http://schema.org/thumbnailUrl>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| thumbnail | `string-uri` | none | URI an autogenerated user-presentable thumbnail-image that serves as a preview of the digital content. The URI may be a Data-URL RFC2397.<br><br>**Example**: `https://picsum.photos/200/300.jpg`         |

## iscc-nft
Metadata for NFT Marketplaces
### **external_url**
<http://purl.org/iscc/terms/#external_url>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| external_url | `string-uri` | none | This is the URL that will appear below the asset's image on some NFT Marketplaces and will allow users to leave the site and view the item on your site. **Supports URI template `(iscc-id)`**.         |

### **animation_url**
<http://purl.org/iscc/terms/#animation_url>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| animation_url | `string-uri` | none | A URL to a multi-media attachment for the item.         |

### **properties**
<http://purl.org/iscc/terms/#properties>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| properties | `object` | none | Arbitrary properties. Values may be strings, numbers, object or arrays. Properties defined here may show up on NFT marketplaces. See [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155#metadata)<br><br>**Example**: `{'simple_property': 'example value', 'rich_property': {'name': 'Name', 'value': '123', 'display_value': '123 Example Value', 'class': 'emphasis', 'css': {'color': '#ffffff', 'font-weight': 'bold', 'text-decoration': 'underline'}}, 'array_property': {'name': 'Name', 'value': [1, 2, 3, 4], 'class': 'emphasis'}}`         |

### **attributes**
<http://purl.org/iscc/terms/#attributes>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| attributes | `array` | none | Similar to `properties` but as an array of objects. These attributes will show up on some NFT marketplaces.<br><br>**Example**: `[{'trait_type': 'METAL', 'value': 'SILVER'}, {'display_type': 'number', 'trait_type': 'GENERATION', 'value': 1}]`         |

### **nft**
<http://purl.org/iscc/terms/#nft>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| nft | `string-uri` | none | A unique URI for a non-fungible token of the identified content. The URI must contain references to the blockchain, smart-contract and token. The recommended schemes are [CAIP-22](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-22.md) and [CAIP-29](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-29.md).<br><br>**Example**: `eip155:1/erc721:0x06012c8cf97BEaD5deAe237070F9587f8E7A266d/771769`         |

## iscc-crypto
Cryptography related ISCC Metadata
### **tophash**
<http://purl.org/iscc/terms/#tophash>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| tophash | `string` | none | A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).<br><br>**Example**: `bdyqnosmb56tqudeibogyygmf2b25xs7wpg4zux4zcts2v6llqmnj4ja`         |

### **metahash**
<http://purl.org/iscc/terms/#metahash>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| metahash | `string` | none | A [Multiformats](https://multiformats.io) multihash or IPFS CIDv1 of the supplied metadata. The hash is created from `name` and `description` fields or `meta` if supplied.<br><br>**Example**: `f01551220b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9`         |

### **datahash**
<http://purl.org/iscc/terms/#datahash>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| datahash | `string` | none | A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).<br><br>**Example**: `bdyqk6e2jxh27tingubae32rw3teutg6lexe23qisw7gjve6k4qpteyq`         |

## iscc-declaration
Field relevant in context with public ISCC declerations
### **original**
<http://purl.org/iscc/terms/#original>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| original | `boolean` | none | The signee of the declaring transaction claims to be the original creator of the work manifested by the identified digital content.<br><br>**Example**: `True`         |

### **redirect**
<http://purl.org/iscc/terms/#redirect>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| redirect | `string-uri` | none | URL to which an ISCC resolver should redirect the ISCC-ID. **Supports URI template `(iscc-id)`**<br><br>**Example**: `https://example.com/land-here-when-resolving-iscc-id`         |

### **chain**
<http://purl.org/iscc/terms/#chain>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| chain | `string` | none | The blockchain on which an ISCC-CODE is declared.<br><br>**Example**: `ETHEREUM`         |

### **wallet**
<http://purl.org/iscc/terms/#wallet>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| wallet | `string` | none | The wallet-address that signs an ISCC declaration.<br><br>**Example**: `0xb794f5ea0ba39494ce839613fffba74279579268`         |

### **verifications**
<http://purl.org/iscc/terms/#verifications>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| verifications | `array` | none | A list of self-verifications. Self-verifications are public URLs under the account/authority of the signee. The verification URL must respond to a GET request with text that contains a multihash of the ISCC declaration signees wallet address in the format of `verify:<multihash-of-wallet-address>:verify`.<br><br>**Example**: `[{'url': 'https://twitter.com/titusz/status/1490104312051257347'}]`         |

