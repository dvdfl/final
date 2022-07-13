from constants import *
# from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        # self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        car = cast.get_first_actor(CAR_GROUP)
        body = car.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        # collide_sound = Sound(COLLIDE_SOUND)
        # over_sound = Sound(OVER_SOUND)

        left_wall_width = ROAD_IMAGES['left']['width'] 
        right_wall_width = ROAD_IMAGES['right']['width'] 
        # collides if car's X position less than left walls width 
        #   OR X greater than Screen width - right wall width - car's width
        if x < left_wall_width or x > SCREEN_WIDTH - right_wall_width - CAR_WIDTH:
            callback.on_next(GAME_OVER)
            # self._audio_service.play_sound(collide_sound)
            # self._audio_service.play_sound(over_sound)
        return
    
