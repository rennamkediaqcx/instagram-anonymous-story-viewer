from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    log_level: str = os.getenv("ASV_LOG_LEVEL", "INFO")
    chrome_path: str = os.getenv("ASV_CHROME_PATH", "")
