import turtle
import random
import paddle

BALL_MOVE_DISTANCE = 20
RIGHT_BOUNDARY = 280
LEFT_BOUNDARY = -280


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(1)
        self.penup()

    def move(self, direction, position):
        self.setheading(direction)
        self.sety(position)
        self.forward(BALL_MOVE_DISTANCE)
        if self.xcor() > RIGHT_BOUNDARY:
            self.setx(0)
        elif self.xcor() < LEFT_BOUNDARY:
            self.setx(0)
