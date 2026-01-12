from __future__ import annotations

import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from src.config.settings import Settings


class HttpClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": settings.user_agent})

    @retry(
        reraise=True,
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=0.8, min=1, max=8),
        retry=retry_if_exception_type(requests.RequestException),
    )
    def get_text(self, url: str) -> str:
        resp = self.session.get(
            url,
            timeout=self.settings.timeout_s,
            proxies=self.settings.proxies,
        )
        resp.raise_for_status()
        return resp.text

    @retry(
        reraise=True,
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=0.8, min=1, max=8),
        retry=retry_if_exception_type(requests.RequestException),
    )
    def get_json(self, url: str) -> dict:
        resp = self.session.get(
            url,
            timeout=self.settings.timeout_s,
            proxies=self.settings.proxies,
        )
        resp.raise_for_status()
        return resp.json()
