"""
Check that the git tag matches the current damm32 version.
For use in CD when auto-releasing to PyPI.
Heavily derived from phial: https://github.com/sedders123/phial/blob/develop/setup.py
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parents[1]


def find_version(*file_paths: str) -> str:
    """
    Find the current formatted version of damm32.
    :param file_paths: File path to search in.
    :returns: Formatted damm32 version.
    :raises RuntimeError: Unable to find version string.
    """
    with BASE_DIR.joinpath(*file_paths).open() as fp:
        version_file = fp.read()

    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        raw_version = version_match.group(1)
        return f"v{raw_version}"
    raise RuntimeError("Unable to find version string.")


def run() -> None:
    """Check the git version matches the damm32 version."""
    tag = os.getenv("GITHUB_REF")

    VERSION = find_version("damm32", "__init__.py")

    if tag != f"refs/tags/v{VERSION}":
        info = "Git tag: {0} != damm32 version: {1}".format(tag, VERSION)
        sys.exit(info)


if __name__ == "__main__":
    run()