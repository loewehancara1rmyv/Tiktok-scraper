from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from src.config.settings import Settings
from src.utils.http import HttpClient


@dataclass
class ScrapeResult:
    platform: str
    scraper_type: str
    execution_id: str
    status: str
    data: Dict[str, Any]


class BaseScraper:
    platform = "tiktok"
    scraper_type = "tiktok scraper"

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.http = HttpClient(settings)

    def execution_id(self) -> str:
        now = datetime.now(timezone.utc).strftime("%Y_%m_%d_%H%M%S")
        return f"run_{now}"

    def ok(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "platform": self.platform,
            "scraper_type": self.scraper_type,
            "execution_id": self.execution_id(),
            "status": "success",
            **data,
        }

    def fail(self, reason: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
            "platform": self.platform,
            "scraper_type": self.scraper_type,
            "execution_id": self.execution_id(),
            "status": "error",
            "error": {"message": reason},
            **(data or {}),
        }
