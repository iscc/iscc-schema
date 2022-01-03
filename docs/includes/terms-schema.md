### **name**

!!! term "<small><http://schema.org/name></small>"

    The name of the item.

    **Comment**:  The name or title of the intangible creation manifested by the idendified *digital content*.

### **description**

!!! term "<small><http://schema.org/disambiguatingDescription></small>"

    A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.

    **Comment**:  Description of the *digital content* identified by the **ISCC** (used as input for Meta-Code generation). Any user presentable text string (including Markdown text) indicative of the identity  of the referent may be used.

### **image**

!!! term "<small><http://schema.org/image></small>"

    An image of the item. This can be a URL or a fully described ImageObject.

    **Comment**:  URI for a user-presentable image that serves as a preview of the *digital content*. The URI may be a Data-URL [RFC2397](https://datatracker.ietf.org/doc/html/rfc2397). If **ISCC** metadata is used as NFT metadata according to [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) or [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/) the URI should reference the actual digital content represented by the NFT.

### **content**

!!! term "<small><http://schema.org/contentUrl></small>"

    Actual bytes of the media object, for example the image file or video file.

    **Comment**:  URI of the *digital content* that was used to create this ISCC.

### **creator**

!!! term "<small><http://schema.org/creator></small>"

    The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.

    **Comment**:  An entity primarily responsible for making the resource.

### **keywords**

!!! term "<small><http://schema.org/keywords></small>"

    Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.

    **Comment**:  Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.

### **identifier**

!!! term "<small><http://schema.org/identifier></small>"

    The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details.

    **Comment**:  Other identifier(s) referencing the work, product or other abstraction of which the referenced **digital content** is a full or partial manifestation.

### **license**

!!! term "<small><http://schema.org/license></small>"

    A license document that applies to this content, typically indicated by URL.

    **Comment**:  URI of license for the identified *digital content*.

### **version**

!!! term "<small><http://schema.org/version></small>"

    The version of the *digital content* identified by the ISCC.

    **Comment**:  The version of the CreativeWork embodied by a specified resource.

### **created**

!!! term "<small><http://schema.org/dateCreated></small>"

    The date on which the CreativeWork was created or the item was added to a DataFeed.

    **Comment**:  Datetime the ISCC was created for the item.

### **filesize**

!!! term "<small><http://schema.org/fileSize></small>"

    Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.

    **Comment**:  File size of media asset in number of bytes.

### **mediatype**

!!! term "<small><http://schema.org/encodingFormat></small>"

    Media type typically expressed using a MIME format (see IANA site and MDN reference) e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.). In cases where a CreativeWork has several media type representations, encoding can be used to indicate each MediaObject alongside particular encodingFormat information. Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.

    **Comment**:  An [IANA Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml) (MIME type)

### **duration**

!!! term "<small><http://schema.org/duration></small>"

    The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](https://en.wikipedia.org/wiki/ISO_8601).

    **Comment**:  Duration of audio-visual media in secondes.

### **pages**

!!! term "<small><http://schema.org/numberOfPages></small>"

    The number of pages in the book.

    **Comment**:  Number of pages (for paged documents only)

### **language**

!!! term "<small><http://schema.org/inLanguage></small>"

    The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](https://www.rfc-editor.org/info/bcp47). See also [availableLanguage](https://schema.org/availableLanguage).

    **Comment**:  Language(s) of content [BCP 47](https://tools.ietf.org/search/bcp47).

