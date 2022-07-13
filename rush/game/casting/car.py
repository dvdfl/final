import random
from constants import *
#from game.casting.actor import Actor
from game.casting.point import Point


#class Ball(Actor):
class Car():
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        # super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the ball's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def steer_left(self):
        """Steers the bat to the left."""
        velocity = Point(-CAR_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def steer_right(self):
        """Steers the bat to the right."""
        velocity = Point(CAR_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
    
    def accelerate(self):
        """Moves car forward"""
        position = self._body.get_position()
        if position.get_y() > CAR_HEIGHT:
            velocity = Point(0, -CAR_VELOCITY)
            self._body.set_velocity(velocity)
        else:
            self.stop_moving()

    def back_up(self):
        """Moves car backwards"""
        position = self._body.get_position()
        if position.get_y() < (SCREEN_HEIGHT - CAR_HEIGHT):
            velocity = Point(0, CAR_VELOCITY)
            self._body.set_velocity(velocity)
        else:
            self.stop_moving()