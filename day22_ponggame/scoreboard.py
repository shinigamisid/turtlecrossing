from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "bold")
FONT_GAME_OVER = ("Paciencia", 48, "bold")

class Score(Turtle):

    def __init__(self, player):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        if player == '1':
            self.goto(-100, 200)
        elif player == '2':
            self.goto(100, 200)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="YOU DIED", move=False, align=ALIGNMENT, font=FONT_GAME_OVER)

    def score_update(self, score):
        self.clear()
        self.write(arg=f"{score}", move=False, align=ALIGNMENT, font=FONT)