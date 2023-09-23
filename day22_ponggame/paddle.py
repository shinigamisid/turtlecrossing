import turtle

STARTING_POSITION = [(-270, 10), (260, 10)]
BORDER = [250, -235]
MOVE_DISTANCE = 25

class Paddle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.screen.register_shape('rectangle', ((5, 20), (5, -20), (-5, -20), (-5, 20)))
        self.paddles = []
        for position in STARTING_POSITION:
            self.paddle_set_position(position)
        self.player_1 = self.paddles[0]
        self.player_2 = self.paddles[1]

    def paddle_set_position(self, paddle_position):
            paddle = turtle.Turtle(shape='rectangle')
            paddle.color('white')
            paddle.penup()
            paddle.goto(paddle_position)
            paddle.setheading(90)
            self.paddles.append(paddle)

    def player1_up(self):
        if self.player_1.ycor() < BORDER[0]:
            self.player_1.forward(MOVE_DISTANCE)

    def player1_down(self):
        if self.player_1.ycor() > BORDER[1]:
            self.player_1.backward(MOVE_DISTANCE)

    def player2_up(self):
        if self.player_2.ycor() < BORDER[0]:
            self.player_2.forward(MOVE_DISTANCE)

    def player2_down(self):
        if self.player_2.ycor() > BORDER[1]:
            self.player_2.backward(MOVE_DISTANCE)