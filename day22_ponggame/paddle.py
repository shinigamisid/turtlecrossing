import turtle

BORDER = [240, -235]
MOVE_DISTANCE = 25
PADDLE_SIZE = ((10, 35), (10, -35), (-10, -35), (-10, 35))


class Paddle(turtle.Turtle):

    def __init__(self, paddle_position):
        super().__init__()
        self.screen.register_shape('rectangle', PADDLE_SIZE)
        self.shape('rectangle')
        self.color('white')
        self.penup()
        self.goto(paddle_position)
        self.setheading(90)

    def paddle_up(self):
        if self.ycor() < BORDER[0]:
            self.forward(MOVE_DISTANCE)

    def paddle_down(self):
        if self.ycor() > BORDER[1]:
            self.backward(MOVE_DISTANCE)
