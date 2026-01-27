"""Constants for __integration_name__."""

import json
from logging import Logger, getLogger
from pathlib import Path

LOGGER: Logger = getLogger(__package__)

DOMAIN = "__integration_name__"

# Load version from manifest.json once at module load
MANIFEST_PATH = Path(__file__).parent / "manifest.json"
VERSION = json.loads(MANIFEST_PATH.read_text())["version"]
