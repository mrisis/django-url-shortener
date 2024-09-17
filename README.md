
# Django URL Shortener

A professional and flexible URL shortener utility for Django projects.

## Features

- **Random or Hash-Based Shortening**: You can choose between random string generation or hash-based shortening for URLs.
- **Easy to Use**: Simple interface for shortening and resolving URLs.
- **Customizable**: Extendable strategy pattern for different URL shortening methods.
- **Validation**: Built-in URL validation before shortening.
- **Tested**: Includes unit tests to ensure functionality.

## Installation

To install the package, you can simply use `pip`:

```bash
pip install django-link-url-shortener
```

# Usage :

- **After installing the package, you can use it in your Django project or any other Python project.**

### Basic Example :

##### Here’s a simple example of how to use the URL shortener:

```python
from shortener.shortener import URLShortener

# Create an instance of the URLShortener
shortener = URLShortener()

# Shorten a URL
original_url = "https://www.google.com"
short_url = shortener.shorten(original_url)
print(f"Shortened URL: {short_url}")

# Resolve the shortened URL back to the original
resolved_url = shortener.resolve(short_url)
print(f"Original URL: {resolved_url}")

```


### Using a Hash-Based Strategy :

##### By default, the shortener uses a random string strategy. However, you can switch to a hash-based strategy as follows:

```python
from shortener.shortener import URLShortener
from shortener.strategies.hash_strategy import HashShorteningStrategy

# Use the hash-based strategy
hash_shortener = URLShortener(strategy=HashShorteningStrategy())

# Shorten a URL
short_url = hash_shortener.shorten("https://www.example.com")
print(f"Shortened URL using hash: {short_url}")

```


### Error Handling :

##### The URLShortener will raise an InvalidURLException if the input URL is not valid:

```python
from shortener.shortener import URLShortener
from shortener.exceptions import InvalidURLException

shortener = URLShortener()

try:
    shortener.shorten("invalid-url")
except InvalidURLException as e:
    print(f"Error: {e}")

```


## Customization :

##### You can create your own URL shortening strategy by subclassing BaseShorteningStrategy:

```python
from shortener.strategies.base_strategy import BaseShorteningStrategy

class CustomShorteningStrategy(BaseShorteningStrategy):
    def shorten(self, original_url):
        return "custom-short-url"

# Use the custom strategy
custom_shortener = URLShortener(strategy=CustomShorteningStrategy())
short_url = custom_shortener.shorten("https://www.example.com")
print(f"Custom Shortened URL: {short_url}")

```


## Running Tests :

##### The package includes unit tests for verifying functionality. To run the tests:

```python
python -m unittest discover tests

```







