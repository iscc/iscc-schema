# **ISCC** - Metadata Vocabulary

## iscc

<small><http://purl.org/iscc/terms/#iscc></small>
<small>ISO 24138:2024</small>
!!! term ""
    An **ISCC-CODE** in canonical representation. A valid ISCC Metadata object should include at least one of the `iscc`, `iscc_id`, or `iscc_code` fields.

## name

<small><http://schema.org/name></small>
<small>ISO 24138:2024</small>
!!! term ""
    The title or name of the intangible creation manifested by the identified *digital content*. **Used as input for ISCC Meta-Code generation**.

## description

<small><http://schema.org/disambiguatingDescription></small>
<small>ISO 24138:2024</small>
!!! term ""
    Description of the *digital content* identified by the **ISCC**. **Used as input for ISCC Meta-Code generation**. Any user presentable text string (including Markdown text) indicative of the identity  of the referent may be used.

## meta

<small><http://purl.org/iscc/terms/#meta></small>
<small>ISO 24138:2024</small>
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

<small><http://purl.org/iscc/terms/#media_id></small>
!!! term ""
    Vendor specific (internal) identifier for the source media file.

## iscc_id

<small><http://purl.org/iscc/terms/#iscc_id></small>
!!! term ""
    The **ISCC-ID** of the digital content in canonical representation. A valid ISCC Metadata object should include at least one of the `iscc`, `iscc_id`, or `iscc_code` fields.

## iscc_code

<small><http://purl.org/iscc/terms/#iscc></small>
!!! term ""
    A composite **ISCC-CODE** in canonical representation. Explicit alternative to the more compact `iscc` field. A valid ISCC Metadata object should include at least one of the `iscc`, `iscc_id`, or `iscc_code` fields.

## image

<small><http://schema.org/image></small>
!!! term ""
    URI for a user-presentable image that serves as a preview of the *digital content*. The URI may be a Data-URL [RFC2397](https://datatracker.ietf.org/doc/html/rfc2397). If **ISCC** metadata is used as NFT metadata according to [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) or [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/) the URI should reference the actual digital content represented by the NFT.

## identifier

<small><http://schema.org/identifier></small>
<small>ISO 24138:2024</small>
!!! term ""
    Other identifier(s) referencing the work, product or other abstraction of which the referenced **digital content** is a full or partial manifestation.

## content

<small><http://schema.org/contentUrl></small>
!!! term ""
    URI of the *digital content* that was used to create this ISCC.

## keywords

<small><http://schema.org/keywords></small>
<small>ISO 24138:2024</small>
!!! term ""
    Keywords or tags used to describe this content. Either a list of keywords or a string with comma separated keywords.

## previous

<small><http://purl.org/iscc/terms/#previous></small>
!!! term ""
    ISCC of the preceding version of this item.

## form

<small><http://schema.org/additionalType></small>
!!! term ""
    The form or kind of content identified, using a Schema.org CreativeWork subtype. While `@type` provides a coarse modality classification (text, image, audio, video) and `mode`/`mediatype` describe technical aspects, `form` captures what the content *is* — a book, scholarly article, presentation, report, photograph, etc.

## version

<small><http://schema.org/version></small>
!!! term ""
    The version of the CreativeWork embodied by a specified resource.

## tdm

<small><http://purl.org/iscc/terms/#tdm></small>
!!! term ""
    Machine-readable TDM reservation signals for AI-related content usage categories. Omitted fields indicate that the reservation status has not been determined.

## genai

<small><http://purl.org/iscc/terms/#genai></small>
!!! term ""
    Machine-readable generative AI disclosure signals for content transparency. Omitted fields indicate that the disclosure status has not been determined.

## mode

<small><http://purl.org/iscc/terms/#mode></small>
!!! term ""
    The perceptual mode used to create the ISCC-CODE.

## created

<small><http://schema.org/dateCreated></small>
!!! term ""
    Datetime the ISCC was created for the item.

## filename

<small><http://purl.org/iscc/terms/#filename></small>
<small>ISO 24138:2024</small>
!!! term ""
    Filename of the referenced **digital content** (automatically used as fallback if the `name` field was not specified for ISCC processing)

## filesize

<small><http://schema.org/fileSize></small>
<small>ISO 24138:2024</small>
!!! term ""
    File size of media asset in number of bytes.

## datasize

<small><http://purl.org/iscc/terms/#datasize></small>
!!! term ""
    Size of the data processed for ISCC generation in number of bytes. Use this field when the ISCC is computed over data that is not a standalone file, such as an individual plane within a bioimage, a scene within a multi-scene container, or a data stream extracted from a composite format.

## mediatype

<small><http://schema.org/encodingFormat></small>
<small>ISO 24138:2024</small>
!!! term ""
    An [IANA Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml) (MIME type)

## duration

<small><http://schema.org/duration></small>
<small>ISO 24138:2024</small>
!!! term ""
    Duration of audio-visual media in seconds.

## fps

<small><http://purl.org/iscc/terms/#fps></small>
<small>ISO 24138:2024</small>
!!! term ""
    Frames per second of video assets.

## width

<small><http://purl.org/iscc/terms/#width></small>
<small>ISO 24138:2024</small>
!!! term ""
    Width of visual media in number of pixels.

## height

<small><http://purl.org/iscc/terms/#height></small>
<small>ISO 24138:2024</small>
!!! term ""
    Height of visual media in number of pixels.

## characters

<small><http://purl.org/iscc/terms/#characters></small>
<small>ISO 24138:2024</small>
!!! term ""
    Number of text characters (code points after Unicode normalization)

## pages

<small><http://schema.org/numberOfPages></small>
!!! term ""
    Number of pages (for paged documents only)

## language

<small><http://schema.org/inLanguage></small>
<small>ISO 24138:2024</small>
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

## units

<small><http://purl.org/iscc/terms/#units></small>
!!! term ""
    Individual ISCC-UNITs that make up a composite ISCC-CODE.

## generator

<small><http://purl.org/iscc/terms/#generator></small>
!!! term ""
    Name and version of the software that generated the ISCC

## text

<small><http://purl.org/iscc/terms/#text></small>
!!! term ""
    Extracted plaintext of the *digital content*.

## thumbnail

<small><http://schema.org/thumbnailUrl></small>
<small>ISO 24138:2024</small>
!!! term ""
    URI of an autogenerated user-presentable thumbnail-image that serves as a preview of the digital content. The URI may be a Data-URL RFC2397.

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
<small>ISO 24138:2024</small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).

## metahash

<small><http://purl.org/iscc/terms/#metahash></small>
<small>ISO 24138:2024</small>
!!! term ""
    A [Multiformats](https://multiformats.io) multihash or IPFS CIDv1 of the supplied metadata. The hash is created from `name` and `description` fields or `meta` if supplied.

## datahash

<small><http://purl.org/iscc/terms/#datahash></small>
<small>ISO 24138:2024</small>
!!! term ""
    A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).

## nonce

<small><http://purl.org/iscc/terms/#nonce></small>
!!! term ""
    Cryptographic nonce for replay protection. A 128-bit random value encoded as lowercase hexadecimal.

## signature

<small><http://purl.org/iscc/terms/#signature></small>
!!! term ""
    Cryptographic signature over ISCC metadata, conforming to the [iscc-crypto](https://github.com/iscc/iscc-crypto) signing protocol. Uses EdDSA (Ed25519) with JCS canonicalization.

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
    One or more [Verifiable Credentials](https://www.w3.org/TR/vc-data-model/) or one or more URIs pointing to one or more VCs. A reader of ISCC metadata must interpret the value according to the following rules <ul> <li>If the value is a JSON `string` interpret it as an URI. The expectation is that the URI dereferences to a response with Content-type `application/json` where the data is a VC or an `array` of VCs.</li><li>If the value is a JSON `object` interpret it as a VC according to the [Verifiable Credentials JSON Schema](https://w3c-ccg.github.io/vc-json-schemas/).</li><li>If the value is an `array` and an item in the `array` is a JSON `object` interpret it as a VC.</li><li>If the value is an `array` and an items is a `string` interpret the item as an URI that dereferences to VC(s)</li><li>Credentials should only be taken into account if the [`credentialSubject`](https://www.w3.org/2018/credentials/#property-definitions) matches with the declarer (e.g. [`did:pkh`](https://github.com/w3c-ccg/did-pkh/blob/main/did-pkh-method-draft.md) representation of the declarers address).</li> </ul>

## verifications

<small><http://purl.org/iscc/terms/#verifications></small>
!!! term ""
    A list of self-verifications. Self-verifications are public URLs under the account/authority of the signee. The verification URL must respond to a GET request with text that contains a multihash of the ISCC declaration signees wallet address in the format of `verify:<multihash-of-wallet-address>:verify`.


---

# Seed Metadata Vocabulary

## isbn

<small><http://schema.org/isbn></small>
!!! term ""
    International Standard Book Number in 13-digit format, without spaces or hyphens.

## productform

<small><http://purl.org/iscc/terms/#productform></small>
!!! term ""
    Product form code indicating the medium and format of the publication (ONIX codelist 150).

## title

<small><http://schema.org/name></small>
!!! term ""
    The title of the publication.

## language

<small><http://schema.org/inLanguage></small>
!!! term ""
    ISO 639-2/B three-letter language code.

## imprint

<small><http://schema.org/publisherImprint></small>
!!! term ""
    The brand name under which the publication is published.

## publisher

<small><http://schema.org/publisher></small>
!!! term ""
    The person or organization that owns the imprint at the date of publication.

## country

<small><http://schema.org/countryOfOrigin></small>
!!! term ""
    Country of publication in accordance with ISO 3166-1 alpha-2 country codes.

## pubdate

<small><http://schema.org/datePublished></small>
!!! term ""
    The date of first publication under this ISBN in ISO 8601 basic format (YYYYMMDD).

## isrc

<small><http://schema.org/isrcCode></small>
!!! term ""
    The International Standard Recording Code assigned to this recording.

## main_artist

<small><http://schema.org/byArtist></small>
!!! term ""
    The name of the featured artist or band.

## track_title

<small><http://schema.org/name></small>
!!! term ""
    The title of the recording.

## version_title

<small><http://schema.org/alternativeHeadline></small>
!!! term ""
    Additional information about the recording, such as 'live' or 'remastered'.

## duration

<small><http://schema.org/duration></small>
!!! term ""
    The elapsed playing time of the recording in seconds.


---

# Service Metadata Vocabulary

## train

<small><http://purl.org/iscc/terms/#train></small>
!!! term ""
    TDM reservation status for AI model training. Covers pre-training, fine-tuning, RLHF, distillation, and embedding training.

## inference

<small><http://purl.org/iscc/terms/#inference></small>
!!! term ""
    TDM reservation status for inference-time content retrieval. Covers RAG, grounding, fact-checking, and context augmentation.

## derive

<small><http://purl.org/iscc/terms/#derive></small>
!!! term ""
    TDM reservation status for AI-assisted content transformation. Covers summarization, translation, format adaptation, and content reformulation.

## search

<small><http://purl.org/iscc/terms/#search></small>
!!! term ""
    TDM reservation status for search and discovery indexing. Covers content indexing with title, snippet, and source attribution.

## analyze

<small><http://purl.org/iscc/terms/#analyze></small>
!!! term ""
    TDM reservation status for automated content analysis. Covers classification, sentiment analysis, topic modeling, and metadata extraction.

## involvement

<small><http://purl.org/iscc/terms/#involvement></small>
!!! term ""
    Level of generative AI involvement in content creation. 'human' indicates content created purely by human effort without generative AI. 'ai_assisted' indicates content created by human effort with support from generative AI. 'human_supervised' indicates content created by generative AI but supervised or reviewed by humans. 'ai_generated' indicates content created by generative AI without human supervision.

## ai_system

<small><http://purl.org/iscc/terms/#ai_system></small>
!!! term ""
    Name or identifier of the generative AI system used for content creation. Aligns with IPTC Photo Metadata 2025.1 'AI System Used' property.

## digital_source_type

<small><http://purl.org/iscc/terms/#digital_source_type></small>
!!! term ""
    IPTC Digital Source Type URI for granular content source classification. This optional field bridges to the IPTC controlled vocabulary, an external evolving standard that offers finer-grained source type distinctions than the 'involvement' field. Also used by C2PA Content Credentials. See https://cv.iptc.org/newscodes/digitalsourcetype/

