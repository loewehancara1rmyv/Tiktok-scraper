from __future__ import annotations

from src.scrapers.base import BaseScraper
from src.utils.validation import validate_url
from src.utils.logger import get_logger
from src.scrapers.video.models import VideoData

log = get_logger(__name__)


class VideoScraper(BaseScraper):
    """
    Skeleton tiktok video scraper.

    This intentionally avoids platform-circumvention logic.
    Add your own compliant extraction strategy (e.g., official APIs / permitted sources).
    """

    def scrape(self, video_url: str) -> dict:
        try:
            video_url = validate_url(video_url)

            mock = VideoData(
                video_id="unknown",
                description="Sample video collected using tiktok scrape workflow",
                hashtags=["scrape the bowl tiktok song"],
                likes=0,
                comments=0,
                shares=0,
                views=0,
                posted_at=None,
                video_url=video_url,
            )

            return self.ok({"video": mock.model_dump()})
        except Exception as e:
            log.exception("Video scraping failed")
            return self.fail(str(e), data={"video": {"video_url": video_url}})
