import string
import random
from .base_strategy import BaseShorteningStrategy


class RandomShorteningStrategy(BaseShorteningStrategy):
    def __init__(self, length=6):
        self.length = length
        
    def shorten(self, oiginal_url):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(self.length))
    