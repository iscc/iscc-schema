"""Build JSON Schema file from Pydantic model"""
import json
import yaml
from os.path import dirname, abspath, join
import iscc_schema


HERE = dirname(abspath(__file__))
PATH_YAML = join(HERE, f"../iscc_schema/models/iscc-collection.yaml")
PATH_LATEST = join(HERE, f"../docs/schema/iscc.json")
PATH_VERSION = join(HERE, f"../docs/schema/{iscc_schema.__version__}.json")


def build_latest():
    """Build `iscc.json` schema"""
    with open(PATH_YAML) as infile:
        data = yaml.safe_load(infile)

    with open(PATH_LATEST, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(json.dumps(data, indent=2, ensure_ascii=False))
        json.dump(data, outf, indent=2)


def build_version():
    """Build `<x.x.x>.json` schema"""
    with open(PATH_YAML) as infile:
        data = yaml.safe_load(infile)

    with open(PATH_VERSION, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(json.dumps(data, indent=2, ensure_ascii=False))
        json.dump(data, outf, indent=2)


def build():
    """Build `iscc.json` & `<x.x.x>.json` schema"""
    build_latest()
    build_version()


if __name__ == "__main__":
    build()
