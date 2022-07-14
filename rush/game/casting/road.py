import random
from constants import *
from game.casting.actor import Actor

class Road(Actor):
    """A solid, rectangle static object in the game."""
    
    def __init__(self, body, image):
        """Constructs a new Road part.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
        """
        super().__init__(body)
        self._image = image

    def get_image(self):
        """Gets the road's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
