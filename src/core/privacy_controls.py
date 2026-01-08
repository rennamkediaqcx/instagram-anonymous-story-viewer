from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class PrivacyPolicy(str, Enum):
    STANDARD = "standard"
    INCOGNITO = "incognito"
    HIDDEN = "hidden"


@dataclass(frozen=True)
class PrivacyControls:
    policy: PrivacyPolicy = PrivacyPolicy.INCOGNITO
    persist_history: bool = False
    redact_logs: bool = True
    user_agent: Optional[str] = None

    def safe_user_agent(self) -> Optional[str]:
        return self.user_agent
