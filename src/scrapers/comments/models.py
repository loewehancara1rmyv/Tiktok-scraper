from pydantic import BaseModel
from typing import Optional


class CommentData(BaseModel):
    comment_id: str
    text: str
    likes: int = 0
    replies: int = 0
    posted_at: Optional[str] = None
