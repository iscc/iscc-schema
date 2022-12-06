# **ISCC** - Metadata Vocabulary

## name

<small><http://schema.org/name></small>
!!! term ""
    The title or name of the intangible creation manifested by the identified *digital content*. **Used as input for ISCC Meta-Code generation**.

## description

<small><http://schema.org/disambiguatingDescription></small>
!!! term ""
    Description of the *digital content* identified by the **ISCC**. **Used as input for ISCC Meta-Code generation**. Any user presentable text string (including Markdown text) indicative of the identity  of the referent may be used.

## meta

<small><http://purl.org/iscc/terms/#meta></small>
!!! term ""
    Subject, industry, or use-case specific metadata encoded as Data-URL.

## creator

<small><http://schema.org/creator></small>
!!! term ""
    An entity primarily responsible for making the resource.

## license

<small><http://schema.org/license></small>
!!! term ""
    URI of license for the identified *digital content*.

## acquire

<small><http://schema.org/acquireLicensePage></small>
!!! term ""
    This field must contain a valid URL referring to a page showing information about how one can acquire a license for the item. This may be a page of a web shop or NFT marketplace ready for providing a license.

## credit

<small><http://schema.org/creditText></small>
!!! term ""
    A line of text that you expect users of the image (such as Google Images) to display alongside the image.

## rights

<small><http://schema.org/copyrightNotice></small>
!!! term ""
    Contains any necessary copyright notice and should identify the current owner of the copyright of this work with associated intellectual property rights.

## media_id

<small><http://schema.org/identifier></small>
!!! term ""
    Vendor specific (internal) identifier for the source media file.

## iscc_id

<small><http://schema.org/identifier></small>
!!! term ""
    The **ISCC-ID** of the digital content in canonical representation.

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

## keywords

<small><http://schema.org/keywords></small>
!!! term ""
    Keywords or tags used to describe this content. Either a list of keywords or a sting with comma separated keywords.

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

## thumbnail

<small><http://schema.org/thumbnailUrl></small>
!!! term ""
    URI an autogenerated user-presentable thumbnail-image that serves as a preview of the digital content. The URI may be a Data-URL RFC2397.

## external_url

<small><http://purl.org/iscc/terms/#external_url></small>
!!! term ""
    This is the URL that will appear below the asset's image on some NFT Marketplaces and will allow users to leave the site and view the item on your site. **Supports URI template `(iscc-id)`**.

## animation_url

<small><http://purl.org/iscc/terms/#animation_url></small>
!!! term ""
    A URL to a multi-media attachment for the item.

## properties

<small><http://purl.org/iscc/terms/#properties></small>
!!! term ""
    Arbitrary properties. Values may be strings, numbers, object or arrays. Properties defined here may show up on NFT marketplaces. See [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155#metadata)

## attributes

<small><http://purl.org/iscc/terms/#attributes></small>
!!! term ""
    Similar to `properties` but as an array of objects. These attributes will show up on some NFT marketplaces.

## nft

<small><http://purl.org/iscc/terms/#nft></small>
!!! term ""
    A unique URI for a non-fungible token of the identified content. The URI must contain references to the blockchain, smart-contract and token. The recommended schemes are [CAIP-22](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-22.md) and [CAIP-29](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-29.md).

## tophash

<small><http://purl.org/iscc/terms/#tophash></small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).

## metahash

<small><http://purl.org/iscc/terms/#metahash></small>
!!! term ""
    A [Multiformats](https://multiformats.io) multihash or IPFS CIDv1 of the supplied metadata. The hash is created from `name` and `description` fields or `meta` if supplied.

## datahash

<small><http://purl.org/iscc/terms/#datahash></small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).

## original

<small><http://purl.org/iscc/terms/#original></small>
!!! term ""
    The signee of the declaring transaction claims to be the original creator of the work manifested by the identified digital content.

## redirect

<small><http://purl.org/iscc/terms/#redirect></small>
!!! term ""
    URL to which an ISCC resolver should redirect the ISCC-ID. **Supports URI template `(iscc-id)`**

## chain

<small><http://purl.org/iscc/terms/#chain></small>
!!! term ""
    The blockchain on which an ISCC-CODE is declared.

## wallet

<small><http://purl.org/iscc/terms/#wallet></small>
!!! term ""
    The wallet-address that signs an ISCC declaration.

## credentials

<small><https://www.w3.org/2018/credentials#VerifiableCredential></small>
!!! term ""
    One or more [Verifiable Credentials](https://www.w3.org/TR/vc-data-model/) or one ore more URIs pointing to one or more VCs. A reader of ISCC metadata must interpret the value according to the following rules <ul> <li>If the value is a JSON `string` interpret it as an URI. The expectation is that the URI dereferences to a response with Content-type `application/json` where the data is a VC or an `array` of VCs.</li><li>If the value is a JSON `object` interpret it as a VC according to the [Verifiable Credentials JSON Schema](https://w3c-ccg.github.io/vc-json-schemas/).</li><li>If the value is an `array` and an item in the `array` is a JSON `object` interpret it as a VC.</li><li>If the value is an `array` and an items is a `string` interpret the item as an URI that dereferences to VC(s)</li><li>Credentials should only taken into account if the [`credentialSubject`](https://www.w3.org/2018/credentials/#property-definitions) matches with the declarer (e.g. [`did:pkh`](https://github.com/w3c-ccg/did-pkh/blob/main/did-pkh-method-draft.md) representation of the declarers address).</li> </ul>

## verifications

<small><http://purl.org/iscc/terms/#verifications></small>
!!! term ""
    A list of self-verifications. Self-verifications are public URLs under the account/authority of the signee. The verification URL must respond to a GET request with text that contains a multihash of the ISCC declaration signees wallet address in the format of `verify:<multihash-of-wallet-address>:verify`.

