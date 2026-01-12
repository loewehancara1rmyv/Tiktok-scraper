import pytest
from src.utils.validation import validate_username, validate_hashtag, validate_url


def test_validate_username():
    assert validate_username("hello.world") == "hello.world"
    assert validate_username("@hello") == "hello"
    with pytest.raises(ValueError):
        validate_username("bad username with spaces")


def test_validate_hashtag():
    assert validate_hashtag("#test") == "test"
    with pytest.raises(ValueError):
        validate_hashtag("")


def test_validate_url():
    assert validate_url("https://example.com") == "https://example.com"
    with pytest.raises(ValueError):
        validate_url("example.com")
