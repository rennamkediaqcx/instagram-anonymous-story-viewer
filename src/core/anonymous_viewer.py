from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .privacy_controls import PrivacyControls
from ..tools.profile_lookup import ProfileLookup
from ..web.online_viewer import OnlineViewer, OnlineViewOptions


class AnonymousViewerError(Exception):
    """Raised for high-level viewer errors."""


@dataclass(frozen=True)
class ViewOptions:
    open_in_browser: bool = True


class AnonymousStoryViewer:
    """
    Orchestrates privacy-oriented viewing workflows.

    IMPORTANT:
    - This template only constructs public profile URLs and can open them.
    - It does not bypass private account restrictions or authentication.
    """

    def __init__(
        self,
        *,
        privacy: PrivacyControls | None = None,
        lookup: ProfileLookup | None = None,
        online: OnlineViewer | None = None,
    ):
        self.privacy = privacy or PrivacyControls()
        self.lookup = lookup or ProfileLookup()
        self.online = online or OnlineViewer()

    def view_profile_anonymously(self, username: str, *, options: Optional[ViewOptions] = None) -> str:
        opts = options or ViewOptions(open_in_browser=True)
        try:
            url = self.lookup.profile_url(username)
            if opts.open_in_browser:
                ov_opts = OnlineViewOptions(
                    open_in_browser=True,
                    prefer_private_mode=True,
                    redact_logs=self.privacy.redact_logs,
                )
                self.online.view_url(url, options=ov_opts)
            return url
        except Exception as e:
            raise AnonymousViewerError(str(e)) from e
