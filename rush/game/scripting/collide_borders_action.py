from constants import *
# from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        # self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        car = cast.get_first_actor(CAR_GROUP)
        car_body = car.get_body()
        # collide_sound = Sound(COLLIDE_SOUND)
        # over_sound = Sound(OVER_SOUND)


        road_walls = cast.get_actors(ROAD_GROUP)
        for wall in road_walls:
            wall_body = wall.get_body()
            if self._physics_service.has_collided(car_body, wall_body):
                callback.on_next(GAME_OVER)
                # self._audio_service.play_sound(collide_sound)
                # self._audio_service.play_sound(over_sound)
                return

