# -*- coding: utf-8 -*-
import json
import pathlib

import pytest
from pydantic import ValidationError
import iscc_schema
from iscc_schema.seed_stm import STM

ROOT = pathlib.Path(__file__).parent.parent
CONTEXT_URL = f"http://purl.org/iscc/context/{iscc_schema.__version__}.jsonld"
SCHEMA_URL = f"http://purl.org/iscc/schema/stm-{iscc_schema.__version__}.json"

# Worked example from the Elsevier pilot sample S0022314X20301219 (Journal of Number Theory).
VALID_STM_DATA = {
    "doi": "10.1016/j.jnt.2020.04.008",
    "resource_type": "JournalArticle",
    "title": "Twisting moduli for GL(2)",
    "publisher": "Elsevier Inc.",
    "pubyear": 2020,
    "version_type": "VoR",
    "container_title": "Journal of Number Theory",
    "issn": "0022-314X",
}

# Only the five reproducibility-guaranteed fields (no version_type/issn/container_title).
REQUIRED_ONLY_DATA = {
    "doi": "10.1016/j.jnt.2020.04.008",
    "resource_type": "JournalArticle",
    "title": "Twisting moduli for GL(2)",
    "publisher": "Elsevier Inc.",
    "pubyear": 2020,
}


def _load_jsonld_context():
    # type: () -> dict
    path = ROOT / "docs" / "context" / "iscc.jsonld"
    return json.loads(path.read_text(encoding="utf-8"))["@context"]


def test_valid_construction():
    obj = STM(**VALID_STM_DATA)
    assert obj.doi == "10.1016/j.jnt.2020.04.008"
    assert obj.resource_type == "JournalArticle"
    assert obj.title == "Twisting moduli for GL(2)"
    assert obj.publisher == "Elsevier Inc."
    assert obj.pubyear == 2020


def test_defaults():
    obj = STM(**VALID_STM_DATA)
    assert obj.context_ == CONTEXT_URL
    assert obj.type_ == "STM"
    assert obj.schema_ == SCHEMA_URL


def test_dict():
    obj = STM(**VALID_STM_DATA)
    d = obj.dict()
    assert d["doi"] == "10.1016/j.jnt.2020.04.008"
    assert d["resource_type"] == "JournalArticle"
    assert d["pubyear"] == 2020


def test_dict_compact():
    obj = STM(**VALID_STM_DATA)
    d = obj.dict()
    assert "$schema" in d
    assert "@context" not in d
    assert "@type" not in d


def test_dict_ld():
    obj = STM(**VALID_STM_DATA)
    d = obj.dict(exclude_unset=False, ld=True)
    assert d["@context"] == CONTEXT_URL
    assert d["@type"] == "STM"
    assert d["$schema"] == SCHEMA_URL
    assert d["doi"] == "10.1016/j.jnt.2020.04.008"
    assert d["resource_type"] == "JournalArticle"


def test_json_compact():
    obj = STM(**VALID_STM_DATA)
    j = obj.json()
    assert '"$schema"' in j
    assert '"@context"' not in j
    assert '"@type"' not in j
    assert '"doi":"10.1016/j.jnt.2020.04.008"' in j
    assert '"pubyear":2020' in j


def test_json_ld():
    obj = STM(**VALID_STM_DATA)
    j = obj.json(ld=True)
    assert f'"@context":"{CONTEXT_URL}"' in j
    assert '"@type":"STM"' in j
    assert '"doi":"10.1016/j.jnt.2020.04.008"' in j


def test_jcs():
    obj = STM(**VALID_STM_DATA)
    result = obj.jcs()
    assert isinstance(result, bytes)
    assert b'"doi":"10.1016/j.jnt.2020.04.008"' in result
    assert b'"$schema"' in result


def test_resource_type_enum_accepts_research_outputs():
    for value in ("JournalArticle", "Preprint", "Dataset", "Software", "Protocol", "Workflow"):
        obj = STM(**{**VALID_STM_DATA, "resource_type": value})
        assert obj.resource_type == value


def test_resource_type_rejects_crossref_token():
    """The enum uses readable CamelCase tokens, not Crossref kebab-case tokens; the populator
    must map journal-article -> JournalArticle."""
    with pytest.raises(ValidationError):
        STM(**{**VALID_STM_DATA, "resource_type": "journal-article"})


def test_resource_type_rejects_non_member():
    with pytest.raises(ValidationError):
        STM(**{**VALID_STM_DATA, "resource_type": "Movie"})


def test_version_type_enum_accepts_all_jav_values():
    for value in ("AO", "SMUR", "AM", "P", "VoR", "CVoR", "EVoR"):
        obj = STM(**{**VALID_STM_DATA, "version_type": value})
        assert obj.version_type == value


def test_version_type_rejects_non_jav():
    with pytest.raises(ValidationError):
        STM(**{**VALID_STM_DATA, "version_type": "final"})


def test_missing_required_doi():
    data = {k: v for k, v in REQUIRED_ONLY_DATA.items() if k != "doi"}
    with pytest.raises(ValidationError):
        STM(**data)


def test_missing_required_resource_type():
    data = {k: v for k, v in REQUIRED_ONLY_DATA.items() if k != "resource_type"}
    with pytest.raises(ValidationError):
        STM(**data)


def test_missing_required_title():
    data = {k: v for k, v in REQUIRED_ONLY_DATA.items() if k != "title"}
    with pytest.raises(ValidationError):
        STM(**data)


def test_missing_required_publisher():
    data = {k: v for k, v in REQUIRED_ONLY_DATA.items() if k != "publisher"}
    with pytest.raises(ValidationError):
        STM(**data)


def test_missing_required_pubyear():
    data = {k: v for k, v in REQUIRED_ONLY_DATA.items() if k != "pubyear"}
    with pytest.raises(ValidationError):
        STM(**data)


def test_invalid_doi_pattern():
    with pytest.raises(ValidationError):
        STM(**{**VALID_STM_DATA, "doi": "not-a-doi"})


def test_invalid_issn_pattern():
    with pytest.raises(ValidationError):
        STM(**{**VALID_STM_DATA, "issn": "0022314X"})


def test_pubyear_out_of_range_low():
    with pytest.raises(ValidationError):
        STM(**{**VALID_STM_DATA, "pubyear": 99})


def test_pubyear_out_of_range_high():
    with pytest.raises(ValidationError):
        STM(**{**VALID_STM_DATA, "pubyear": 12000})


def test_pubyear_rejects_non_numeric():
    with pytest.raises(ValidationError):
        STM(**{**VALID_STM_DATA, "pubyear": "twenty"})


def test_optional_fields_omittable():
    obj = STM(**REQUIRED_ONLY_DATA)
    d = obj.dict()
    assert "version_type" not in d
    assert "issn" not in d
    assert "container_title" not in d


def test_extra_fields_forbidden():
    with pytest.raises(ValidationError):
        STM(**{**VALID_STM_DATA, "extra": "value"})


def test_import_from_package():
    from iscc_schema import STM as STMFromPkg

    obj = STMFromPkg(**VALID_STM_DATA)
    assert obj.doi == "10.1016/j.jnt.2020.04.008"


def test_schema_has_jsonld_extension():
    """STM serializes compact by default, so its schema documents the JSON-LD upgrade path
    via a top-level x-iscc-jsonld extension pointing at the versioned context."""
    schema = json.loads((ROOT / "docs" / "schema" / "stm.json").read_text(encoding="utf-8"))
    ext = schema["x-iscc-jsonld"]
    assert ext["context"] == CONTEXT_URL
    assert ext["type"] == "STM"
    assert "x-iscc-jsonld" in schema["properties"]["$schema"]["description"]


def test_schema_context_default_is_versioned():
    """The published JSON Schema pins the versioned @context default, matching the value the
    Pydantic model emits with ld=True."""
    schema = json.loads((ROOT / "docs" / "schema" / "stm.json").read_text(encoding="utf-8"))
    assert schema["properties"]["@context"]["default"] == CONTEXT_URL
    assert STM(**VALID_STM_DATA).context_ == CONTEXT_URL


def test_latest_schema_const_is_versioned():
    """The latest schema file pins a version-specific $schema const while keeping an unversioned
    $id: records identify the exact schema version; the file is served at the 'latest' URL."""
    schema = json.loads((ROOT / "docs" / "schema" / "stm.json").read_text(encoding="utf-8"))
    assert schema["properties"]["$schema"]["const"] == SCHEMA_URL
    assert schema["$id"] == "http://purl.org/iscc/schema/stm.json"


def test_versioned_archive_exists():
    """A version-pinned archive is written alongside the latest schema; its $id and its $schema
    const both carry the version."""
    archive = ROOT / "docs" / "schema" / f"stm-{iscc_schema.__version__}.json"
    assert archive.exists()
    data = json.loads(archive.read_text(encoding="utf-8"))
    assert data["$id"] == SCHEMA_URL
    assert data["properties"]["$schema"]["const"] == SCHEMA_URL


def test_resource_type_maps_to_readable_iris():
    """resource_type tokens coerce to IRIs (@type: @id) and resolve to readable schema.org /
    FaBiO class IRIs in the shared context: schema.org for the common types, FaBiO for the gaps
    (Preprint, ConferencePaper). No opaque COAR codes."""
    ctx = _load_jsonld_context()
    assert ctx["resource_type"] == {"@id": "http://schema.org/additionalType", "@type": "@id"}
    # schema.org primary (reuses the IRIs the core `form` field already maps)
    assert ctx["JournalArticle"] == "http://schema.org/ScholarlyArticle"
    assert ctx["Dataset"] == "http://schema.org/Dataset"
    assert ctx["Software"] == "http://schema.org/SoftwareSourceCode"
    # FaBiO fills the schema.org gaps
    assert ctx["Preprint"] == "http://purl.org/spar/fabio/Preprint"
    assert ctx["ConferencePaper"] == "http://purl.org/spar/fabio/ConferencePaper"
    assert ctx["Protocol"] == "http://purl.org/spar/fabio/ExperimentalProtocol"


def test_stm_terms_in_shared_context():
    """STM's distinguishing terms are mapped in the single shared JSON-LD context with their
    expected IRIs."""
    ctx = _load_jsonld_context()
    assert ctx["doi"] == "http://purl.org/ontology/bibo/doi"
    assert ctx["version_type"] == "http://purl.org/iscc/terms/#version_type"
    assert ctx["pubyear"] == "http://schema.org/datePublished"
    assert ctx["issn"] == "http://schema.org/issn"
    assert ctx["container_title"] == "http://prismstandard.org/namespaces/basic/2.0/publicationName"


def test_recover_context_from_stm_schema():
    """A compact STM record recovers the shared context (with STM type) from its $schema."""
    data = {"$schema": SCHEMA_URL, "doi": "10.1016/j.jnt.2020.04.008"}
    result = iscc_schema.recover_context(data)
    assert "STM" in result["@context"]
    assert result["@context"]["doi"] == "http://purl.org/ontology/bibo/doi"
