# **ISCC** - Metadata Vocabulary

## iscc

<small><http://purl.org/iscc/terms/#iscc></small>
!!! term ""
    An **ISCC-CODE** in canonical representation. This is the minimal required field for a valid ISCC Metadata object.

## name

<small><http://schema.org/name></small>
!!! term ""
    The name or title of the intangible creation manifested by the idendified *digital content*.

## description

<small><http://schema.org/disambiguatingDescription></small>
!!! term ""
    Description of the *digital content* identified by the **ISCC** (used as input for Meta-Code generation). Any user presentable text string (including Markdown text) indicative of the identity  of the referent may be used.

## image

<small><http://schema.org/image></small>
!!! term ""
    URI for a user-presentable image that serves as a preview of the *digital content*. The URI may be a Data-URL [RFC2397](https://datatracker.ietf.org/doc/html/rfc2397). If **ISCC** metadata is used as NFT metadata according to [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) or [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/) the URI should reference the actual digital content represented by the NFT.

## version

<small><http://schema.org/version></small>
!!! term ""
    The version of the CreativeWork embodied by a specified resource.

## content

<small><http://schema.org/contentUrl></small>
!!! term ""
    URI of the *digital content* that was used to create this ISCC.

## identifier

<small><http://schema.org/identifier></small>
!!! term ""
    Other identifier(s) referencing the work, product or other abstraction of which the referenced **digital content** is a full or partial manifestation.


## creator

<small><http://schema.org/creator></small>
!!! term ""
    An entity primarily responsible for making the resource.

## license

<small><http://schema.org/license></small>
!!! term ""
    URI of license for the identified *digital content*.

## redirect

<small><http://purl.org/iscc/terms/#redirect></small>
!!! term ""
    URL to which a resolver should redirect an ISCC-ID that has been minted from a declartion that includes the IPFS-hash of this metadata instance.


## properties

<small><http://purl.org/iscc/terms/#properties></small>
!!! term ""
    JSON or JSON-LD formated values about the identified *digital content*. Compatible with [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155).

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

## keywords

<small><http://schema.org/keywords></small>
!!! term ""
    Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.

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

## datahash

<small><http://purl.org/iscc/terms/#datahash></small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).

## metahash

<small><http://purl.org/iscc/terms/#metahash></small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the supplied metadata (default blake3). For deterministic results [JSC RFC5452](https://datatracker.ietf.org/doc/html/rfc8785) canonicalization is applied before hashing.

## tophash

<small><http://purl.org/iscc/terms/#tophash></small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).

