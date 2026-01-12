from pydantic import BaseModel
from typing import List


class HashtagResult(BaseModel):
    hashtag: str
    hashtag_url: str
    top_video_ids: List[str] = []
