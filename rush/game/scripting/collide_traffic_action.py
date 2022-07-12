from constants import *
from game.scripting.action import Action
class CollideTrafficAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
    
    def execute(self, cast, script, callback):
        car = cast.get_first_actor(CAR_GROUP)
        traffic_cars = cast.get_actors(TRAFFIC_GROUP)

        if len(traffic_cars) > 0:
            car_body = car.get_body()

            for t_car in traffic_cars:
                traffic_body = t_car.get_body()
                
                if self._physics_service.has_collided(car_body, traffic_body):
                    callback.on_next(GAME_OVER)
                    # sound = Sound(BOUNCE_SOUND)
                    # self._audio_service.play_sound(sound)    

