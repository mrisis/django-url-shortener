from abc import ABC

class BaseShorteningStrategy(ABC):
    
    @abstractmethod
    def shorten(self, original_url):
        
        """
        method to generate a short version of url.
        """
        
        pass
