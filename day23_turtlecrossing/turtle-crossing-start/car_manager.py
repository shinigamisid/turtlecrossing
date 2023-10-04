import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self, x_user_input, y_user_input):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.goto(x_user_input, y_user_input)
        self.zip(STARTING_MOVE_DISTANCE)

    def zip(self, move_distance):
        self.backward(move_distance)

    def speed_increase(self):
        x = self.speed()
        x += MOVE_INCREMENT
        self.zip(x)