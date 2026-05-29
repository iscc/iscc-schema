"""Tests for version-source consistency and immutability of released schema archives.

These guard the version-protection discipline behind the build pipeline: pyproject.toml and
the package __version__ must agree, and once a version is tagged its published archive files
must never change. The build guard (_check_version_not_released in the build tools) prevents
overwriting released archives; this test is the backstop that catches a mutation even if the
guard is bypassed.
"""

import pathlib
import re
import subprocess

import pytest

import iscc_schema as iss

ROOT = pathlib.Path(__file__).parent.parent


def _pyproject_version():
    # type: () -> str
    """Read the project version from pyproject.toml without a TOML dependency (3.10 has no tomllib)."""
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'(?m)^version = "([^"]+)"', text)
    assert match, "no project version found in pyproject.toml"
    return match.group(1)


def test_version_sources_match():
    """pyproject.toml and iscc_schema.__version__ must declare the same version."""
    assert _pyproject_version() == iss.__version__


def _git(args):
    # type: (list[str]) -> subprocess.CompletedProcess | None
    """Run a git command from the repo root, returning None if git is unavailable."""
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    except OSError:
        return None


def _versioned_archives(version):
    # type: (str) -> list[pathlib.Path]
    """Versioned archive files for a release: the whole-schema/context files plus every
    per-schema standalone archive (e.g. isbn-X.Y.Z.json)."""
    schema_dir = ROOT / "docs" / "schema"
    context_dir = ROOT / "docs" / "context"
    candidates = [
        schema_dir / f"{version}.json",
        context_dir / f"{version}.jsonld",
        *sorted(schema_dir.glob(f"*-{version}.json")),
    ]
    return [p for p in candidates if p.exists()]


def _normalize(raw):
    # type: (bytes) -> str
    """Decode as UTF-8 and normalize newlines so a locale/autocrlf difference is never mistaken
    for a content mutation."""
    return raw.decode("utf-8").replace("\r\n", "\n")


def test_released_archives_immutable():
    """If the current version is tagged, every versioned archive on disk must match the content
    committed at that tag (modulo newline normalization). Unreleased versions skip."""
    version = iss.__version__
    tags = _git(["tag", "-l", f"v{version}"])
    if tags is None:
        pytest.skip("git is not available")
    if not tags.stdout.strip():
        pytest.skip(f"version {version} is not released (no tag v{version})")

    for path in _versioned_archives(version):
        relpath = path.relative_to(ROOT).as_posix()
        shown = _git(["show", f"tags/v{version}:{relpath}"])
        if shown.returncode != 0:
            continue  # file did not exist at that release
        current = _normalize(path.read_bytes())
        tagged = _normalize(shown.stdout)
        assert current == tagged, (
            f"{relpath} differs from tagged release v{version}; "
            "bump the version before modifying released artifacts."
        )
