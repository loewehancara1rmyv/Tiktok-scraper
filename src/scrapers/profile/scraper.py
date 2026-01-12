from __future__ import annotations

from src.scrapers.base import BaseScraper
from src.utils.validation import validate_username
from src.utils.logger import get_logger
from src.scrapers.profile.models import ProfileData

log = get_logger(__name__)


class ProfileScraper(BaseScraper):
    """
    Skeleton tiktok profile scraper.
    """

    def scrape(self, username: str) -> dict:
        try:
            username = validate_username(username)
            profile_url = f"https://www.tiktok.com/@{username}"

            mock = ProfileData(
                username=username,
                profile_url=profile_url,
                followers_count=0,
                following_count=0,
                total_likes=0,
                is_verified=False,
            )

            return self.ok({"profile": mock.model_dump()})
        except Exception as e:
            log.exception("Profile scraping failed")
            return self.fail(str(e), data={"profile": {"username": username}})
