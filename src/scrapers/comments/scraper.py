from __future__ import annotations

from src.scrapers.base import BaseScraper
from src.utils.validation import validate_url
from src.utils.logger import get_logger
from src.scrapers.comments.models import CommentData

log = get_logger(__name__)


class CommentsScraper(BaseScraper):
    """
    Skeleton tiktok comments scraper / tiktok comment scraper module.
    """

    def scrape(self, video_url: str, limit: int = 20) -> dict:
        try:
            video_url = validate_url(video_url)
            limit = max(1, min(int(limit), 200))

            comments = [
                CommentData(
                    comment_id="cmt_001",
                    text="This data was captured using a tiktok comments scraper",
                    likes=0,
                    replies=0,
                    posted_at=None,
                ).model_dump()
            ]

            return self.ok({"video_url": video_url, "comments": comments[:limit]})
        except Exception as e:
            log.exception("Comments scraping failed")
            return self.fail(str(e), data={"video_url": video_url, "comments": []})
