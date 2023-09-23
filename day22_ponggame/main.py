import turtle
import time
import paddle
import ball
import scoreboard

STARTING_POSITION = [(-270, 10), (260, 10)]
DIVIDER_SIZE = ((5, 20), (5, -20), (-5, -20), (-5, 20))

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("shini's Pong Game")
screen.tracer(0)
screen.register_shape('divider_rectangle', DIVIDER_SIZE)

for i in range(350, -350, -70):
    divider_line = turtle.Turtle()
    divider_line.setheading(90)
    divider_line.goto(0, i)
    divider_line.shape('divider_rectangle')
    divider_line.color('white')

paddle_1 = paddle.Paddle(STARTING_POSITION[0])
paddle_2 = paddle.Paddle(STARTING_POSITION[1])
game_score_p1 = scoreboard.Score("1")
game_score_p2 = scoreboard.Score("2")
game_ball = ball.Ball()

def bounce():
    if game_ball.distance(paddle_1) < 25 or game_ball.distance(paddle_2) < 25:
        game_ball.setheading(-game_ball.heading())

screen.listen()
screen.onkey(paddle_1.paddle_up, 'w')
screen.onkey(paddle_1.paddle_down, 's')
screen.onkey(paddle_2.paddle_up, 'Up')
screen.onkey(paddle_2.paddle_down, 'Down')

is_game_on = True

player1_score = 0
player2_score = 0

while is_game_on:
    screen.update()
    game_score_p1.score_update(player1_score)
    game_score_p2.score_update(player2_score)
    bounce()
    game_ball.move()
    if game_ball.xcor() > 275:
        player1_score += 1
    elif game_ball.xcor() < -275:
        player2_score += 1
    if player1_score > 10 or player2_score > 10:
        game_score_p1.game_over()
        break




screen.exitonclick()
