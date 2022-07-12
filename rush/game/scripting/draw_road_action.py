from constants import *
from game.scripting.action import Action

class DrawRoadAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        road_wall = cast.get_actors(ROAD_GROUP)
        
        for wall in road_wall:
            body = wall.get_body()

            #if wall.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
                
            # animation = wall.get_animation()
            # image = animation.next_image()
            image = wall.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)