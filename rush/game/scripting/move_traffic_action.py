from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class MoveTrafficAction(Action):
    def __init__(self):
        super().__init__()
        

    def execute(self, cast, script, callback):
        velocity = Point(0, TRAFFIC_VELOCITY)
        # self._body.set_velocity(velocity)

        cars = cast.get_actors(TRAFFIC_GROUP)
        for car in cars:
            body = car.get_body()
            body.set_velocity(velocity)
            car.move_next()