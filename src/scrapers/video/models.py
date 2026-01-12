from pydantic import BaseModel, Field
from typing import List, Optional


class VideoData(BaseModel):
    video_id: str
    description: str = ""
    hashtags: List[str] = Field(default_factory=list)
    likes: int = 0
    comments: int = 0
    shares: int = 0
    views: int = 0
    posted_at: Optional[str] = None
    video_url: str
