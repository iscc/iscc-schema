import json

import jcs
from pydantic import BaseModel as OriginalBaseModel, model_validator


class BaseModel(OriginalBaseModel):

    model_config = {
        "validate_assignment": True,
        "extra": "forbid",
        "use_enum_values": True,
        "from_attributes": True,
    }

    @model_validator(mode="before")
    @classmethod
    def empty_string_to_none(cls, data):
        if isinstance(data, dict):
            return {k: v if v != "" else None for k, v in data.items()}
        return data

    def dict(self, *args, exclude_none=True, exclude_unset=True, by_alias=True, **kwargs):
        # type: (...) -> dict
        """
        Override defaults to exclude `None` and unset values and translate aliases.

        Maintains backwards compatibility with dict() method name while using
        Pydantic v2's model_dump() internally.

        !!! note
            This overrides the default BaseModel.dict()
        """
        return self.model_dump(
            *args,
            exclude_none=exclude_none,
            exclude_unset=exclude_unset,
            by_alias=by_alias,
            **kwargs,
        )

    def json(self, *args, exclude_none=True, by_alias=True, **kwargs):
        # type: (...) -> str
        """
        Override defaults to exclude empty fields and use aliases.

        The by_alias=True allows us to generate valid JSON-LD by default. It translates
        our python "_context" property to @context

        Maintains backwards compatibility with json() method name while using
        Pydantic v2's model_dump_json() internally.

        !!! note
            This overrides the default BaseModel.json()
        """
        return self.model_dump_json(
            *args,
            exclude_none=exclude_none,
            by_alias=by_alias,
            **kwargs,
        )

    def jcs(self):
        # type: () -> bytes
        """
        Create JCS canonicalized JSON bytestring
        """
        data = self.dict(exclude_unset=False)
        ser = jcs.canonicalize(data)
        des = json.loads(ser)
        if des != data:
            raise ValueError(f"Not canonicalizable {data} round-trips to {des}")
        return ser

    @property
    def iscc_obj(self):
        # type: () -> "iscc_core.Code"
        """
        Convenience method that wraps an ISCC string in an iscc_core.Code object

        :return: `iscc_core.Code` object if the iscc-core package is installed
        :rtype: iscc_core.Code
        :raise: `ImportError` if iscc-core package is not instlled.
        """
        try:
            from iscc_core import Code
        except ImportError:
            raise ImportError("IsccMeta.iscc_obj requires iscc-core package.")
        return Code(self.iscc)
