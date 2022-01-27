# **ISCC** - Metadata Vocabulary

## name

<small><http://schema.org/name></small>
!!! term ""
    The title or name of the intangible creation manifested by the identified *digital content* (used as input for **ISCC Meta-Code** generation).

## description

<small><http://schema.org/disambiguatingDescription></small>
!!! term ""
    Description of the *digital content* identified by the **ISCC** (used as input for Meta-Code generation). Any user presentable text string (including Markdown text) indicative of the identity  of the referent may be used.

## metadata

<small><http://purl.org/iscc/terms/#metadata></small>
!!! term ""
    Descriptive, industry-sector or use-case specific metadata. Can be any object that is JSON/JCS serializable. If `metadata` is provided it is the sole input for the cryptographic `metahash` calculation. If `metadata` is set to a string it is assumed that it is base64 encoded binary file metadata.

## image

<small><http://schema.org/image></small>
!!! term ""
    URI for a user-presentable image that serves as a preview of the *digital content*. The URI may be a Data-URL [RFC2397](https://datatracker.ietf.org/doc/html/rfc2397). If **ISCC** metadata is used as NFT metadata according to [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) or [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/) the URI should reference the actual digital content represented by the NFT.

## identifier

<small><http://schema.org/identifier></small>
!!! term ""
    Other identifier(s) referencing the work, product or other abstraction of which the referenced **digital content** is a full or partial manifestation.

## content

<small><http://schema.org/contentUrl></small>
!!! term ""
    URI of the *digital content* that was used to create this ISCC.

## creator

<small><http://schema.org/creator></small>
!!! term ""
    An entity primarily responsible for making the resource.

## keywords

<small><http://schema.org/keywords></small>
!!! term ""
    Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.

## license

<small><http://schema.org/license></small>
!!! term ""
    URI of license for the identified *digital content*.

## redirect

<small><http://purl.org/iscc/terms/#redirect></small>
!!! term ""
    URL to which a resolver should redirect an ISCC-ID that has been minted from a declartion that includes the IPFS-hash of this metadata instance.

## previous

<small><http://purl.org/iscc/terms/#previous></small>
!!! term ""
    ISCC of the preceding version of this item.

## version

<small><http://schema.org/version></small>
!!! term ""
    The version of the CreativeWork embodied by a specified resource.

## created

<small><http://schema.org/dateCreated></small>
!!! term ""
    Datetime the ISCC was created for the item.

## filename

<small><http://purl.org/iscc/terms/#filename></small>
!!! term ""
    Filename of the referenced **digital content** (automatically used as fallback if the `name` field was not specified for ISCC processing)

## filesize

<small><http://schema.org/fileSize></small>
!!! term ""
    File size of media asset in number of bytes.

## mediatype

<small><http://schema.org/encodingFormat></small>
!!! term ""
    An [IANA Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml) (MIME type)

## duration

<small><http://schema.org/duration></small>
!!! term ""
    Duration of audio-visual media in secondes.

## fps

<small><http://purl.org/iscc/terms/#fps></small>
!!! term ""
    Frames per second of video assets.

## width

<small><http://purl.org/iscc/terms/#width></small>
!!! term ""
    Width of visual media in number of pixels.

## height

<small><http://purl.org/iscc/terms/#height></small>
!!! term ""
    Height of visual media in number of pixels.

## characters

<small><http://purl.org/iscc/terms/#characters></small>
!!! term ""
    Number of text characters (code points after Unicode normalization)

## pages

<small><http://schema.org/numberOfPages></small>
!!! term ""
    Number of pages (for paged documents only)

## language

<small><http://schema.org/inLanguage></small>
!!! term ""
    Language(s) of content [BCP 47](https://tools.ietf.org/search/bcp47).

## parts

<small><http://purl.org/iscc/terms/#parts></small>
!!! term ""
    Indicates items that are part of this item via Content-Codes (inverse-property belongs).

## part_of

<small><http://purl.org/iscc/terms/#part_of></small>
!!! term ""
    Indicates that this item is part of other items via their Content-Code.

## features

<small><http://purl.org/iscc/terms/#features></small>
!!! term ""
    Granular features of the *digital content*.

## generator

<small><http://purl.org/iscc/terms/#generator></small>
!!! term ""
    Name and version of the software that generated the ISCC

## external_url

<small><http://purl.org/iscc/terms/#external_url></small>
!!! term ""
    This is the URL that will appear below the asset's image on some NFT Marketplaces and will allow users to leave the site and view the item on your site.

## animation_url

<small><http://purl.org/iscc/terms/#animation_url></small>
!!! term ""
    A URL to a multi-media attachment for the item.

## properties

<small><http://purl.org/iscc/terms/#properties></small>
!!! term ""
    Descriptive, industry-sector or use-case specific metadata. Can be any object that is JSON/JCS serializable. If properties are provided they are the sole input for the cryptographic `metahash` calculation. Also compatible with [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155). If properties is set to a string it is assumed that it is base64 encoded binary file metadata.

## tophash

<small><http://purl.org/iscc/terms/#tophash></small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).

## metahash

<small><http://purl.org/iscc/terms/#metahash></small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the supplied metadata (default blake3). The hash is created from `name` and `description` fields or `properties` if supplied. For deterministic results [JSC RFC5452](https://datatracker.ietf.org/doc/html/rfc8785) canonicalization is applied to `properties` before hashing if it is a JSON object.

## datahash

<small><http://purl.org/iscc/terms/#datahash></small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).

