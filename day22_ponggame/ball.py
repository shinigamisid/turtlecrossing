import turtle
import random
import paddle

BALL_DIRECTIONS = random.choice([0, 180])
BALL_POSITION = random.randint(-200, 200)
BALL_MOVE_DISTANCE = 20


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(1)
        self.penup()
        self.sety(BALL_POSITION)

    def move(self):
        self.setheading(BALL_DIRECTIONS)
        self.forward(BALL_MOVE_DISTANCE)
