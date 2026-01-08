from __future__ import annotations

import os
import subprocess
import webbrowser
from dataclasses import dataclass
from urllib.parse import urlparse

from ..utils.logger import get_logger


@dataclass(frozen=True)
class BrowserOpenResult:
    method: str
    url: str


class AnonymousBrowser:
    """
    Best-effort browser opener with optional private/incognito preference.

    This does NOT guarantee anonymity; it only attempts to open a browser in a
    privacy-oriented mode when possible. Users should manage their own browser
    profiles/settings for strict privacy requirements.
    """

    def __init__(self):
        self._log = get_logger(__name__)

    def open(self, url: str, *, prefer_private_mode: bool = True, redact_logs: bool = True) -> BrowserOpenResult:
        if not url or not url.strip():
            raise ValueError("url is required")

        parsed = urlparse(url.strip())
        if parsed.scheme not in ("http", "https"):
            raise ValueError("only http/https URLs are supported")

        display_url = "<redacted>" if redact_logs else url
        self._log.info("Opening URL: %s", display_url)

        if prefer_private_mode:
            try:
                return self._open_chrome_incognito(url)
            except Exception:
                pass

        webbrowser.open(url)
        return BrowserOpenResult(method="webbrowser", url=url)

    def _open_chrome_incognito(self, url: str) -> BrowserOpenResult:
        candidates = [
            os.getenv("ASV_CHROME_PATH", ""),
            "google-chrome",
            "google-chrome-stable",
            "chromium",
            "chromium-browser",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        ]
        for cmd in [c for c in candidates if c]:
            try:
                subprocess.Popen([cmd, "--incognito", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return BrowserOpenResult(method=f"chrome-incognito:{cmd}", url=url)
            except Exception:
                continue
        raise FileNotFoundError("Chrome/Chromium not found for incognito open")
