import turtle
import time
import paddle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("shini's Pong Game")
screen.tracer(0)
game_paddle = paddle.Paddle()

screen.listen()
screen.onkey(game_paddle.player2_up, 'Up')
screen.onkey(game_paddle.player2_down, 'Down')
screen.onkey(game_paddle.player1_up, 'w')
screen.onkey(game_paddle.player1_down, 's')

is_game_on = True

while is_game_on:
    screen.update()
    screen.tracer(1)




screen.exitonclick()
