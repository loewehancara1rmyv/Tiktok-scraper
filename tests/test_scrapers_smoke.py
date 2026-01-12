from src.config.settings import Settings
from src.scrapers.profile.scraper import ProfileScraper
from src.scrapers.video.scraper import VideoScraper
from src.scrapers.comments.scraper import CommentsScraper
from src.scrapers.hashtags.scraper import HashtagScraper


def test_smoke_profile():
    out = ProfileScraper(Settings()).scrape("example_creator")
    assert out["platform"] == "tiktok"
    assert out["status"] in ("success", "error")


def test_smoke_video():
    out = VideoScraper(Settings()).scrape("https://www.tiktok.com/@x/video/123")
    assert out["platform"] == "tiktok"
    assert out["status"] in ("success", "error")


def test_smoke_comments():
    out = CommentsScraper(Settings()).scrape("https://www.tiktok.com/@x/video/123")
    assert out["platform"] == "tiktok"
    assert out["status"] in ("success", "error")


def test_smoke_hashtag():
    out = HashtagScraper(Settings()).scrape("test")
    assert out["platform"] == "tiktok"
    assert out["status"] in ("success", "error")
