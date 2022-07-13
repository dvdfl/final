import random
from constants import *
#from game.casting.actor import Actor
from game.casting.point import Point


#class Ball(Actor):
class Road():
    """A solid, rectangle static object in the game."""
    
    def __init__(self, body, image):
        """Constructs a new Road part.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
        """
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the road's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the road's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
