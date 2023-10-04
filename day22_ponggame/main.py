import turtle
import time
import paddle
import ball
import random
import scoreboard

STARTING_POSITION = [(-365, 0), (360, 0)]
DIVIDER_SIZE = ((5, 20), (5, -20), (-5, -20), (-5, 20))

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("shini's Pong Game")
screen.tracer(0)

for i in range(350, -350, -70):
    divider_line = turtle.Turtle()
    divider_line.setheading(90)
    divider_line.goto(0, i)
    divider_line.shape('square')
    divider_line.shapesize(stretch_len=2, stretch_wid=0.5)
    divider_line.color('white')

paddle_1 = paddle.Paddle(STARTING_POSITION[0])
paddle_2 = paddle.Paddle(STARTING_POSITION[1])
game_score_p1 = scoreboard.Score("1")
game_score_p2 = scoreboard.Score("2")

game_ball = ball.Ball()

screen.listen()
screen.onkey(paddle_1.paddle_up, 'w')
screen.onkey(paddle_1.paddle_down, 's')
screen.onkey(paddle_2.paddle_up, 'Up')
screen.onkey(paddle_2.paddle_down, 'Down')

is_game_on = True

player1_score = 0
player2_score = 0
ball_position = 0
ball_direction = 0

while is_game_on:
    time.sleep(game_ball.ball_speed)
    screen.update()
    if player1_score >= 10:
        game_score_p1.score_update(player1_score)
        game_score_p1.game_over()
        break
    elif player2_score >= 10:
        game_score_p2.score_update(player2_score)
        game_score_p2.game_over()
        break
    game_score_p1.score_update(player1_score)
    game_score_p2.score_update(player2_score)
    game_ball.move()
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()
    if game_ball.distance(paddle_2) < 50 and game_ball.xcor() > 320:
        game_ball.bounce_x()
    if game_ball.distance(paddle_1) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()

    if game_ball.xcor() >= 400:
        player1_score += 1
        ball_position = random.randint(-200, 200)
        game_ball.reset_position()
    elif game_ball.xcor() <= -400:
        player2_score += 1
        ball_position = random.randint(-200, 200)
        game_ball.reset_position()



screen.exitonclick()
