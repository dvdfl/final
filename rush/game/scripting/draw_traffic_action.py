import random
from constants import *
from game.casting.car import Car
from game.casting.image import Image
from game.casting.body import Body
from game.casting.point import Point
from game.scripting.action import Action

class DrawTrafficAction(Action):
    def __init__(self, video_service):
        super().__init__()
        self._video_service = video_service

    def execute(self, cast, script, callback):
        
        cars = cast.get_actors(TRAFFIC_GROUP)
        # Removing off screen cars
        for car in cars:
            body = car.get_body()
            if body.get_position().get_y() > SCREEN_HEIGHT + CAR_HEIGHT:
                cast.remove_actor(TRAFFIC_GROUP, car)

        cars = cast.get_actors(TRAFFIC_GROUP)
        car_count = len(cars)
        new_car_x = random.randint(120,480)
        new_car_y = self._get_fardest_car(cars)
        
        #print(f"fardest car: {new_car_y}")
        # if traffic cars les than 15 and (count = 0 or position of newest car is greater that .25 car's height)
        while len(cast.get_actors(TRAFFIC_GROUP))  < TRAFFIC_CARS and (car_count == 0 or new_car_y > CAR_HEIGHT * .25):
            # new car placed at the top
            new_car_y = 0 - CAR_HEIGHT + 2
            position = Point(new_car_x, new_car_y)
            size = Point(CAR_WIDTH, CAR_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(random.choice(CAR_IMAGES))
            car = Car(body, image, True)
            cast.add_actor(TRAFFIC_GROUP, car)
            
            car_count += 1
            new_car_x = random.randint(110,480)


        cars = cast.get_actors(TRAFFIC_GROUP)
        
        for car in cars:
            body = car.get_body()

            # if ball.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = car.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
            # print(f'car position: {position.get_x()}, {position.get_y()}')


    def _get_fardest_car(self, cars):

        far_car_y = SCREEN_HEIGHT / 2
        for car in cars:
            car_y = car.get_body().get_position().get_y()
            if far_car_y > car_y:
                far_car_y = car_y
        
        # far_car_y = far_car_y - CAR_HEIGHT
        # print(f'far_car_y: {far_car_y}')

        return far_car_y
        