from constants import *
from game.scripting.action import Action


class ControlCarAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        car = cast.get_first_actor(CAR_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            car.steer_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            car.steer_right()  
        elif self._keyboard_service.is_key_down(UP): 
            car.accelerate()  
        elif self._keyboard_service.is_key_down(DOWN): 
            car.back_up()  
        else: 
            car.stop_moving()        