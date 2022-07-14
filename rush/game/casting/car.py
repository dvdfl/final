from constants import *
from game.casting.point import Point

class Car():
    """A car representation, it can be player's car or part of the traffic in the game."""
    
    def __init__(self, body, image):
        """Constructs a new Car object.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
        """
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the car's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the car's image.
        
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
        """Steers the car to the left."""
        velocity = Point(-CAR_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def steer_right(self):
        """Steers the car to the right."""
        velocity = Point(CAR_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the car from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
    
    def accelerate(self):
        """Moves car forward"""
        position = self._body.get_position()
        if position.get_y() > ROAD_TOP:
            velocity = Point(0, -CAR_VELOCITY)
            self._body.set_velocity(velocity)
        else:
            self.stop_moving()

    def back_up(self):
        """Moves car backwards"""
        position = self._body.get_position()
        if position.get_y() < ROAD_BOTTOM:
            velocity = Point(0, CAR_VELOCITY)
            self._body.set_velocity(velocity)
        else:
            self.stop_moving()