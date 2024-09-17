import hashlib
from .base_strategy import BaseShorteningStrategy


class HashShorteningStrategy(BaseShorteningStrategy):
    def shorten(self, original_url):
        return hashlib.md5(original_url.encode()).hexdigest()[:6]