### **TDM**

!!! term "<small><http://purl.org/iscc/terms/#TDM></small>"

    Machine-readable TDM rights signals conformant with W3C TDMRep, providing content-addressed delivery of tdm-reservation and tdm-policy properties via ISCC. Designed for content identification and discovery where identity, provenance, and trust context complement the reservation signal.

### **tdm_reservation**

!!! term "<small><http://www.w3.org/ns/tdmrep#reservation></small>"

    Blanket TDM reservation flag, semantically equivalent to W3C TDMRep tdm-reservation. 1 = rights reserved (EU DSM Art. 4 opt-out), 0 = not reserved, absent = undeclared.

    **Status**:  stable

### **tdm_policy**

!!! term "<small><http://www.w3.org/ns/tdmrep#policy></small>"

    URL of a TDM Policy document (typically a JSON-LD ODRL Offer profiling TDMRep). Semantically equivalent to W3C TDMRep tdm-policy.

### **GenAI**

!!! term "<small><http://purl.org/iscc/terms/#GenAI></small>"

    Machine-readable generative AI disclosure signals for content transparency. Designed for AI providers to declare the level of AI involvement in content creation, supporting compliance with transparency regulations (e.g., EU AI Act Art. 50) and enabling end users to verify AI-generated content. These signals are designed for use within content identification and discovery protocols that provide additional identity, provenance, and trust context.

### **involvement**

!!! term "<small><http://purl.org/iscc/terms/#involvement></small>"

    Level of generative AI involvement in content creation. 'human' indicates content created purely by human effort without generative AI. 'ai_assisted' indicates content created by human effort with support from generative AI. 'human_supervised' indicates content created by generative AI but supervised or reviewed by humans. 'ai_generated' indicates content created by generative AI without human supervision.

### **ai_system**

!!! term "<small><http://purl.org/iscc/terms/#ai_system></small>"

    Name or identifier of the generative AI system used for content creation. Aligns with IPTC Photo Metadata 2025.1 'AI System Used' property.

### **digital_source_type**

!!! term "<small><http://purl.org/iscc/terms/#digital_source_type></small>"

    IPTC Digital Source Type URI for granular content source classification. This optional field bridges to the IPTC controlled vocabulary, an external evolving standard that offers finer-grained source type distinctions than the 'involvement' field. Also used by C2PA Content Credentials. See https://cv.iptc.org/newscodes/digitalsourcetype/

### **Identifiers**

!!! term "<small><http://purl.org/iscc/terms/#Identifiers></small>"

    Set of typed external identifiers served for an asset identified by an ISCC.

### **scheme**

!!! term "<small><http://schema.org/propertyID></small>"

    Lowercase token naming the identifier namespace, such as doi, isrc, iswc, isbn, issn, ror, or orcid.

    **Status**:  draft

### **code**

!!! term "<small><http://schema.org/value></small>"

    Identifier value within the declared scheme, normalized by the producer according to the scheme's conventions.

    **Status**:  draft

### **scope**

!!! term "<small><http://purl.org/iscc/terms/#scope></small>"

    Optional lowercase token naming the level the identifier applies to, such as work, series, manifestation, asset, organization, or person.

    **Status**:  draft

### **primary**

!!! term "<small><http://purl.org/iscc/terms/#primary></small>"

    Preferred identifier flag within the same scope. True means preferred; false is equivalent to omission and is normalized away by the model construction path.

    **Status**:  draft

