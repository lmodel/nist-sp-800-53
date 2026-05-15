"""Data test."""
import os
import glob
import subprocess
import sys
import pytest
from pathlib import Path

DATA_DIR_VALID = Path(__file__).parent / "data" / "schema-valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "schema-invalid"
SCHEMA = Path(__file__).parent.parent / "src" / "nist_sp_800_53" / "schema" / "nist_sp_800_53.yaml"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


def _target_class(filepath: str) -> str:
    """Derive the LinkML target class name from the filename stem prefix."""
    return Path(filepath).stem.split("-")[0]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Valid data files must pass linkml validate with zero errors."""
    result = subprocess.run(
        [
            sys.executable, "-m", "linkml.cli",
            "validate",
            "-s", str(SCHEMA),
            "-C", _target_class(filepath),
            filepath,
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"linkml validate failed for {filepath}:\n{result.stdout}\n{result.stderr}"
    )


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Invalid data files must be rejected by linkml validate (non-zero exit)."""
    result = subprocess.run(
        [
            sys.executable, "-m", "linkml.cli",
            "validate",
            "-s", str(SCHEMA),
            "-C", _target_class(filepath),
            filepath,
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0, (
        f"linkml validate unexpectedly passed for {filepath}:\n{result.stdout}\n{result.stderr}"
    )


