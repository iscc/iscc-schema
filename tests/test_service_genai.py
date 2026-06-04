# -*- coding: utf-8 -*-
import json
import pathlib

import iscc_schema as iss
from iscc_schema import GenAI

ROOT = pathlib.Path(__file__).parent.parent


def _load_schema(name):
    # type: (str) -> dict
    return json.loads((ROOT / "docs" / "schema" / name).read_text(encoding="utf-8"))


def test_genai_accepts_optional_iscc_on_standalone_record():
    obj = GenAI(iscc="ISCC:MAACAJINXFXA2SQX", involvement="ai_generated")
    assert obj.iscc == "ISCC:MAACAJINXFXA2SQX"
    assert obj.involvement == "ai_generated"
    assert obj.dict()["iscc"] == "ISCC:MAACAJINXFXA2SQX"


def test_genai_subjectless_records_still_validate():
    obj = GenAI(involvement="human")
    assert obj.iscc is None
    assert "iscc" not in obj.dict()


def test_genai_service_object_allows_extension_fields():
    obj = GenAI(involvement="ai_assisted", vendor_signal="present")
    assert obj.dict()["vendor_signal"] == "present"


def test_genai_service_object_preserves_falsy_extension_fields():
    obj = GenAI(
        involvement="ai_generated",
        confidence=0.0,
        weights=[],
        metadata={},
        empty="",
        verified=False,
    )

    data = obj.dict()
    assert data["confidence"] == 0.0
    assert data["weights"] == []
    assert data["metadata"] == {}
    assert data["empty"] == ""
    assert data["verified"] is False

    canonical = json.loads(obj.jcs())
    assert canonical["confidence"] == 0.0
    assert canonical["weights"] == []
    assert canonical["metadata"] == {}
    assert canonical["empty"] == ""
    assert canonical["verified"] is False


def test_inline_genai_schema_remains_subjectless_but_open():
    schema = _load_schema("iscc.json")
    genai = schema["properties"]["genai"]
    assert genai["additionalProperties"] is True
    assert "iscc" not in genai["properties"]

    meta = iss.IsccMeta(genai={"involvement": "human", "vendor_signal": "present"})
    assert meta.dict()["genai"]["vendor_signal"] == "present"
