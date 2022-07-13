from constants import *
from game.scripting.action import Action

class CollideBordersAction(Action):

    def __init__(self, physics_service):
        self._physics_service = physics_service
        
    def execute(self, cast, script, callback):
        car = cast.get_first_actor(CAR_GROUP)
        car_body = car.get_body()

        road_walls = cast.get_actors(ROAD_GROUP)
        for wall in road_walls:
            wall_body = wall.get_body()
            if self._physics_service.has_collided(car_body, wall_body):
                callback.on_next(GAME_OVER)
                return

