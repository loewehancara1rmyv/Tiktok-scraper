from __future__ import annotations

from src.scrapers.base import BaseScraper
from src.utils.validation import validate_hashtag
from src.utils.logger import get_logger
from src.scrapers.hashtags.models import HashtagResult

log = get_logger(__name__)


class HashtagScraper(BaseScraper):
    """
    Skeleton hashtag module aligned with tiktok hashtag scraper patterns.
    """

    def scrape(self, hashtag: str) -> dict:
        try:
            hashtag = validate_hashtag(hashtag)
            hashtag_url = f"https://www.tiktok.com/tag/{hashtag}"

            mock = HashtagResult(
                hashtag=hashtag,
                hashtag_url=hashtag_url,
                top_video_ids=[],
            )

            return self.ok({"hashtag": mock.model_dump()})
        except Exception as e:
            log.exception("Hashtag scraping failed")
            return self.fail(str(e), data={"hashtag": {"hashtag": hashtag}})
