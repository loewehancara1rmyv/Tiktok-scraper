import re

_USERNAME_RE = re.compile(r"^[A-Za-z0-9._]{2,64}$")


def validate_username(username: str) -> str:
    if username.startswith("@"):
        username = username[1:]
    if not _USERNAME_RE.match(username):
        raise ValueError("Invalid username format.")
    return username


def validate_hashtag(hashtag: str) -> str:
    hashtag = hashtag.strip()
    if hashtag.startswith("#"):
        hashtag = hashtag[1:]
    if not hashtag or len(hashtag) > 80:
        raise ValueError("Invalid hashtag.")
    return hashtag


def validate_url(url: str) -> str:
    url = url.strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError("URL must start with http:// or https://")
    return url
