### **tdm_reservation**

!!! term "<small><http://www.w3.org/ns/tdmrep#reservation></small>"

    Blanket TDM reservation flag, semantically equivalent to W3C TDMRep tdm-reservation. 1 = rights reserved (EU DSM Art. 4 opt-out), 0 = not reserved, absent = undeclared.

### **tdm_policy**

!!! term "<small><http://www.w3.org/ns/tdmrep#policy></small>"

    URL of a TDM Policy document (typically a JSON-LD ODRL Offer profiling TDMRep). Semantically equivalent to W3C TDMRep tdm-policy.

### **involvement**

!!! term "<small><http://purl.org/iscc/terms/#involvement></small>"

    Level of generative AI involvement in content creation. 'human' indicates content created purely by human effort without generative AI. 'ai_assisted' indicates content created by human effort with support from generative AI. 'human_supervised' indicates content created by generative AI but supervised or reviewed by humans. 'ai_generated' indicates content created by generative AI without human supervision.

### **ai_system**

!!! term "<small><http://purl.org/iscc/terms/#ai_system></small>"

    Name or identifier of the generative AI system used for content creation. Aligns with IPTC Photo Metadata 2025.1 'AI System Used' property.

### **digital_source_type**

!!! term "<small><http://purl.org/iscc/terms/#digital_source_type></small>"

    IPTC Digital Source Type URI for granular content source classification. This optional field bridges to the IPTC controlled vocabulary, an external evolving standard that offers finer-grained source type distinctions than the 'involvement' field. Also used by C2PA Content Credentials. See https://cv.iptc.org/newscodes/digitalsourcetype/

