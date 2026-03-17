"""Schema-driven JSON-LD context recovery for ISCC metadata."""

from iscc_schema.contexts import SCHEMA_CONTEXTS, SCHEMA_ISCC, TYPE_SCHEMAS

# Canonical standalone schema names (last path segment -> schema URL)
_STANDALONE_NAMES = {}
for url in SCHEMA_CONTEXTS:
    if url != SCHEMA_ISCC:
        name = url.rsplit("/", 1)[-1]
        _STANDALONE_NAMES[name] = url
        _STANDALONE_NAMES[name.replace(".json", "")] = url


_ISCC_SCHEMA_BASE = "http://purl.org/iscc/schema"


def _normalize_schema_url(url):
    # type: (str) -> str
    """Normalize a $schema URL to its canonical form for lookup."""
    segment = url.rsplit("/", 1)[-1] if "/" in url else ""
    if segment in _STANDALONE_NAMES:
        return _STANDALONE_NAMES[segment]
    if url == SCHEMA_ISCC or url.startswith(_ISCC_SCHEMA_BASE):
        return SCHEMA_ISCC
    return url


def recover_context(data, schema=None):
    # type: (dict, str|None) -> dict
    """Recover JSON-LD context for plain ISCC JSON data.

    Uses schema-driven context recovery: looks up the @context from the
    bundled context mappings based on the data's $schema or @type field.
    """
    if "@context" in data:
        return data

    if schema is not None:
        if schema in _STANDALONE_NAMES:
            schema_url = _STANDALONE_NAMES[schema]
        elif schema in SCHEMA_CONTEXTS:
            schema_url = schema
        else:
            schema_url = _normalize_schema_url(schema)
    elif "$schema" in data:
        schema_url = _normalize_schema_url(data["$schema"])
    elif "@type" in data:
        type_val = data["@type"]
        if type_val not in TYPE_SCHEMAS:
            raise ValueError(f"Unknown @type: {type_val}")
        schema_url = TYPE_SCHEMAS[type_val]
    else:
        schema_url = SCHEMA_ISCC

    if schema_url not in SCHEMA_CONTEXTS:
        raise ValueError(f"Unknown schema: {schema_url}")

    return {"@context": SCHEMA_CONTEXTS[schema_url], **data}
