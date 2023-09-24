import turtle

BORDER = [250, -250]
MOVE_DISTANCE = 25



class Paddle(turtle.Turtle):

    def __init__(self, paddle_position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
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
