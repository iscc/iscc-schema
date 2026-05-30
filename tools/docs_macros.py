"""Zensical macros environment — exposes the package version to docs templates.

Read at site-build time by `zensical.extensions.macros` (configured in `zensical.toml` via
`module_name = "tools/docs_macros"`). `define_env` registers `{{ version }}` so hand-written docs
derive the version from the single source of truth (`iscc_schema.__version__`) instead of
hardcoding it. Zensical loads this module by file path, so `tools/` need not be an importable package.
"""

import iscc_schema


def define_env(env):
    # type: (object) -> None
    """Register template variables for the docs (zensical macros / mkdocs-macros API)."""
    env.variables["version"] = iscc_schema.__version__
