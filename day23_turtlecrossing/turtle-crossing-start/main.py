import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
player = Player()
score = Scoreboard()
screen.tracer(0)
car_list = []

for _ in range(15):
    car = CarManager(x_user_input=random.randint(-200, 400), y_user_input=random.randint(-220, 250))
    car_list.append(car)

current_score = 0
car_speed = 1

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    screen.listen()
    screen.onkey(player.turtle_up, 'w')
    if player.ycor() > 273:
        current_score += 1
        car_speed += 1
        score.score_update(current_score)
        player.turtle_reset()
    for single_car in car_list:
        if player.distance(single_car) < 25:
            score.game_over()
            game_is_on = False
        single_car.zip(car_speed * 5)
        if single_car.xcor() < -310:
            single_car.setx(random.randint(305,340))
            screen.tracer(0)

screen.exitonclick()