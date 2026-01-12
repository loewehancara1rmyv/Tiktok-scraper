from pydantic import BaseModel


class ProfileData(BaseModel):
    username: str
    profile_url: str
    followers_count: int = 0
    following_count: int = 0
    total_likes: int = 0
    is_verified: bool = False
