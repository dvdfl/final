from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class MoveTrafficAction(Action):
    def __init__(self):
        super().__init__()
        

    def execute(self, cast, script, callback):
        #speed set based on the current level + base_speed
        stats = cast.get_first_actor(STATS_GROUP)
        speed = TRAFFIC_VELOCITY + stats.get_level()
        velocity = Point(0, speed)
        # self._body.set_velocity(velocity)

        cars = cast.get_actors(TRAFFIC_GROUP)
        for car in cars:
            body = car.get_body()
            body.set_velocity(velocity)
            car.move_next()