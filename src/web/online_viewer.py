from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .anonymous_browser import AnonymousBrowser


@dataclass(frozen=True)
class OnlineViewOptions:
    open_in_browser: bool = True
    prefer_private_mode: bool = True
    redact_logs: bool = True


class OnlineViewer:
    """Opens public URLs using best-effort private/incognito mode when requested."""

    def __init__(self, *, browser: AnonymousBrowser | None = None):
        self.browser = browser or AnonymousBrowser()

    def view_url(self, url: str, *, options: Optional[OnlineViewOptions] = None) -> str:
        opts = options or OnlineViewOptions()
        if opts.open_in_browser:
            self.browser.open(url, prefer_private_mode=opts.prefer_private_mode, redact_logs=opts.redact_logs)
        return url
