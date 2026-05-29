### **isbn**

!!! term "<small><http://schema.org/isbn></small>"

    International Standard Book Number in 13-digit format, without spaces or hyphens.

### **productform**

!!! term "<small><http://purl.org/iscc/terms/#productform></small>"

    Product form code indicating the medium and format of the publication (ONIX codelist 150).

### **title**

!!! term "<small><http://schema.org/name></small>"

    The title of the publication.

### **language**

!!! term "<small><http://schema.org/inLanguage></small>"

    ISO 639-2/B three-letter language code.

### **imprint**

!!! term "<small><http://schema.org/publisherImprint></small>"

    The brand name under which the publication is published.

### **publisher**

!!! term "<small><http://schema.org/publisher></small>"

    The person or organization that owns the imprint at the date of publication.

### **country**

!!! term "<small><http://schema.org/countryOfOrigin></small>"

    Country of publication in accordance with ISO 3166-1 alpha-2 country codes.

### **pubdate**

!!! term "<small><http://schema.org/datePublished></small>"

    The date of first publication under this ISBN in ISO 8601 basic format (YYYYMMDD).

### **isrc**

!!! term "<small><http://schema.org/isrcCode></small>"

    The International Standard Recording Code assigned to this recording.

### **main_artist**

!!! term "<small><http://schema.org/byArtist></small>"

    The name of the featured artist or band.

### **track_title**

!!! term "<small><http://schema.org/name></small>"

    The title of the recording.

### **version_title**

!!! term "<small><http://schema.org/alternativeHeadline></small>"

    Additional information about the recording, such as 'live' or 'remastered'.

### **duration**

!!! term "<small><http://schema.org/duration></small>"

    The elapsed playing time of the recording in seconds.

### **doi**

!!! term "<small><http://purl.org/ontology/bibo/doi></small>"

    Digital Object Identifier of the work, lowercased, in bare prefix form (without the https://doi.org/ resolver prefix).

### **resource_type**

!!! term "<small><http://schema.org/additionalType></small>"

    The kind of research output as a readable token. Tokens follow the DataCite resource-type vocabulary and are populated from the Crossref/DataCite work type (for example, journal-article maps to JournalArticle). Each token is mapped to a resolvable schema.org or FaBiO class IRI in the JSON-LD context (see x-iscc-enum-context). This is the work-kind axis; version_type is the orthogonal version-stage axis.

### **pubyear**

!!! term "<small><http://schema.org/datePublished></small>"

    Year of publication. Crossref guarantees year-level precision only; using an integer avoids the false precision of a full date.

### **version_type**

!!! term "<small><http://purl.org/iscc/terms/#version_type></small>"

    Manifestation version using the NISO JAV (RP-8-2008) vocabulary. Publisher-specific version taxonomies are mapped into these values. Lets a Version-of-Record and an Accepted-Manuscript of the same work produce different Meta-Codes while a shared work-level `doi` links them.

### **version_doi**

!!! term "<small><http://purl.org/ontology/bibo/doi></small>"

    DOI assigned to this specific version, where one exists.

### **container_title**

!!! term "<small><http://prismstandard.org/namespaces/basic/2.0/publicationName></small>"

    Title of the serial or collection the work is part of (journal, proceedings, book). Not guaranteed for standalone works.

### **issn**

!!! term "<small><http://schema.org/issn></small>"

    ISSN of the container serial. Only present for serial publications.

### **creator**

!!! term "<small><http://schema.org/creator></small>"

    Family name of the first listed creator, normalized. Optional; the most stable cross-catalog author token.

