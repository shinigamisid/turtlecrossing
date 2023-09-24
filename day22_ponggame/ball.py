import turtle

BALL_MOVE_DISTANCE = 20
RIGHT_BOUNDARY = 280
LEFT_BOUNDARY = -280


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1)
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.ball_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
        # if self.xcor() > RIGHT_BOUNDARY:
        #     self.setx(0)
        # elif self.xcor() < LEFT_BOUNDARY:
        #     self.setx(0)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.01
        self.bounce_x()
