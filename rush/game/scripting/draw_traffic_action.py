from constants import *
from game.casting.car import Car
from game.casting.image import Image
from game.casting.body import Body
from game.casting.point import Point
from game.scripting.action import Action

class DrawTrafficAction(Action):
    def __init__(self, video_service):
        super().__init__()
        self._video_service = video_service

    def execute(self, cast, script, callback):

        cars = cast.get_actors(TRAFFIC_GROUP)
        
        for car in cars:
            body = car.get_body()

            # if ball.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = car.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
