from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import requests

from ..utils.logger import get_logger


class SaveError(Exception):
    """Raised when saving fails."""


@dataclass(frozen=True)
class SaveResult:
    url: str
    saved_to: str
    bytes_written: int


class StorySaver:
    """
    Saves media from a *direct* URL.

    IMPORTANT:
    - This does not discover story media URLs.
    - Provide a direct URL you are permitted to download.
    """

    def __init__(self):
        self._log = get_logger(__name__)

    def save(self, url: str, *, output_dir: str = "downloads", filename: Optional[str] = None, timeout: int = 30) -> SaveResult:
        if not url or not url.strip():
            raise SaveError("url is required")

        parsed = urlparse(url.strip())
        if parsed.scheme not in ("http", "https"):
            raise SaveError("only http/https URLs are supported")

        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        if not filename:
            filename = Path(parsed.path).name or "media.bin"

        target = out_dir / filename

        try:
            with requests.get(url, stream=True, timeout=timeout) as r:
                r.raise_for_status()
                bytes_written = 0
                with open(target, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 64):
                        if not chunk:
                            continue
                        f.write(chunk)
                        bytes_written += len(chunk)

            self._log.info("Saved media to %s (%d bytes)", str(target), bytes_written)
            return SaveResult(url=url, saved_to=str(target), bytes_written=bytes_written)
        except requests.RequestException as e:
            raise SaveError(f"save failed: {e}") from e
