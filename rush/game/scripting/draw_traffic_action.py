from constants import *
from game.scripting.action import Action

class DrawTrafficAction(Action):
    def __init__(self, video_service):
        super().__init__()
        self._video_service = video_service

    def execute(self, cast, script, callback):

        cars = cast.get_actors(TRAFFIC_GROUP)
        
        for car in cars:
            body = car.get_body()

            image = car.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
