import argparse
from pathlib import Path

from src.config.settings import Settings
from src.utils.io import write_json
from src.utils.logger import get_logger
from src.scrapers.profile.scraper import ProfileScraper
from src.scrapers.video.scraper import VideoScraper
from src.scrapers.comments.scraper import CommentsScraper
from src.scrapers.hashtags.scraper import HashtagScraper

log = get_logger(__name__)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="tiktok-scraper",
        description="Self-hosted TikTok scraping skeleton (public data only).",
    )
    p.add_argument("--profile", help="TikTok username (without @).")
    p.add_argument("--video", help="TikTok video URL.")
    p.add_argument("--hashtag", help="Hashtag (without #).")
    p.add_argument("--comments", help="TikTok video URL to fetch comments from.")
    p.add_argument("--out", default="output/result.json", help="Output JSON path.")
    return p


def main() -> int:
    args = build_parser().parse_args()
    settings = Settings()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    result = {"platform": "tiktok", "scraper_type": "tiktok scraper", "status": "no_op"}

    if args.profile:
        log.info("Scraping profile: %s", args.profile)
        result = ProfileScraper(settings).scrape(username=args.profile)

    if args.video:
        log.info("Scraping video: %s", args.video)
        result = VideoScraper(settings).scrape(video_url=args.video)

    if args.hashtag:
        log.info("Scraping hashtag: %s", args.hashtag)
        result = HashtagScraper(settings).scrape(hashtag=args.hashtag)

    if args.comments:
        log.info("Scraping comments: %s", args.comments)
        result = CommentsScraper(settings).scrape(video_url=args.comments)

    write_json(out_path, result)
    log.info("Wrote output to %s", out_path.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
