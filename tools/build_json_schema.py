"""Build JSON Schema file from Pydantic model"""
import iscc_schema
from os.path import dirname, abspath, join


HERE = dirname(abspath(__file__))
PATH_LATEST = join(HERE, f"../docs/schema/iscc.json")
PATH_VERSION = join(HERE, f"../docs/schema/{iscc_schema.__version__}.json")


def build_latest():
    """Build `iscc.json` schema"""

    with open(PATH_LATEST, "wt", encoding="utf-8") as outf:
        outf.write(iscc_schema.ISCC.schema_json(indent=2, ensure_ascii=False))


def build_version():
    """Build `<x.x.x>.json` schema"""

    with open(PATH_VERSION, "wt", encoding="utf-8") as outf:
        outf.write(iscc_schema.ISCC.schema_json(indent=2, ensure_ascii=False))


def build():
    """Build `iscc.json` & `<x.x.x>.json` schema"""
    build_latest()
    build_version()


if __name__ == "__main__":
    build()
