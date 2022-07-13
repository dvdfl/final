import random
from constants import *
from game.scripting.action import Action
from game.casting.car import Car
from game.casting.image import Image
from game.casting.body import Body
from game.casting.point import Point

class ControlTrafficAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast, script, callback):
        # Removing off screen cars
        self._remove_offscreen_cars(cast)

        #
        self._add_cars(cast)

    def _remove_offscreen_cars(self, cast):
        cars = cast.get_actors(TRAFFIC_GROUP)
        # for each car is offscreen
        for car in cars:
            body = car.get_body()
            if body.get_position().get_y() > SCREEN_HEIGHT + CAR_HEIGHT:
                cast.remove_actor(TRAFFIC_GROUP, car)
                self._add_points(cast)
    
    def _add_cars(self, cast):
        cars = cast.get_actors(TRAFFIC_GROUP)
        car_count = len(cars)

        limit_l = ROAD_IMAGES['left']['width']
        limit_r = SCREEN_WIDTH - ROAD_IMAGES['right']['width'] - CAR_WIDTH
        new_car_x = random.randint(limit_l, limit_r)
        new_car_y = self._get_fardest_car(cars)
        
        # if traffic cars les than 15 and (count = 0 or position of newest car is greater that .25 car's height)
        while len(cast.get_actors(TRAFFIC_GROUP))  < TRAFFIC_CARS and (car_count == 0 or new_car_y > CAR_HEIGHT * .25):
            # new car placed at the top
            new_car_y = 0 - CAR_HEIGHT + 2
            self._add_car(cast, new_car_x, new_car_y)
            
            car_count += 1
            new_car_x = random.randint(limit_l, limit_r)
            
    def _add_car(self, cast, x, y):
            position = Point(x, y)
            size = Point(CAR_WIDTH, CAR_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(random.choice(CAR_IMAGES))
            car = Car(body, image, True)

            cast.add_actor(TRAFFIC_GROUP, car)


    def _get_fardest_car(self, cars):
        far_car_y = SCREEN_HEIGHT / 2
        for car in cars:
            car_y = car.get_body().get_position().get_y()
            if far_car_y > car_y:
                far_car_y = car_y

        return far_car_y

   
    def _add_points(self, cast):
        points = TRAFFIC_POINTS # brick.get_points()
        stats = cast.get_first_actor(STATS_GROUP)
        stats.add_points(points)
