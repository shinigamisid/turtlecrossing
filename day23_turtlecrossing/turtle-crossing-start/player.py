import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.turtlesize(1)
        self.setheading(90)
        self.turtle_reset()

    def turtle_up(self):
        if 275 > self.ycor() > -275:
            self.forward(10)

    def turtle_reset(self):
        self.goto(0, -260)