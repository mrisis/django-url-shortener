import re
from .exceptions import InvalidURLException
from .strategies.random_strategy import RandomShorteningStrategy

class URLShortener:
    
    URL_REGEX = re.compile(
        r'^(http|https)://[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+([/?].*)?$'
    )
    
    def __init__(self, strategy=None):
        
        self.strategy = strategy or RandomShorteningStrategy
        self.url_map = {}
        
    
    def shorten(self, original_url):
        if not self._is_valid_url(original_url):
            raise InvalidURLException(f"Invalid URL: {original_url}")
    
    
    def resolve(self,short_url):
        
        return self.url_map.get(short_url, None)
    
    
    def _is_valid_url(self,url):
        
        return bool(self.URL_REGEX.match(url))
    
    