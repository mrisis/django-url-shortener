import unittest
from shortener.shortener import URLShortener
from shortener.exceptions import InvalidURLException
from shortener.strategies.hash_strategy import HashShorteningStrategy


class TestURLShortener(unittest.TestCase):
    
    def setUp(self):
        self.shortener = URLShortener()
        self.hash_shotener = URLShortener(strategy=HashShorteningStrategy())
    
    def test_shorten_url(self):
        original_url = "https://www.google.com"
        short_url = self.shortener.shorten(original_url=original_url)
        self.assertIsNotNone(short_url)
    
    def test_invalid_url(self):
        invalid_url = "htp://invalid-url"
        with self.assertRaises(InvalidURLException):
            self.shortener.shorten(invalid_url)
            
    def test_resolve_url(self):
        original_url = "https://www.google.com"
        short_url = self.shortener.shorten(original_url=original_url)
        resolved_url = self.shortener.resolve(short_url=short_url)
        self.assertEqual(resolved_url, original_url)
        
    def test_hash_strategy(self):
        original_url = "https://www.google.com"
        short_url = self.hash_shotener(original_url)
        self.assertEqual(len(short_url), 6)
        

if __name__ == '__main__':
    unittest.main()
        
    
        
    