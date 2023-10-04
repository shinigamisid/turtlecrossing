from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'left'
FONT_GAME_OVER = ("Paciencia", 48, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-270, 270)
        self.write(arg="score: 0", move=False, align=ALIGNMENT, font=FONT)

    def score_update(self, updated_score):
        self.clear()
        self.write(arg=f"score: {updated_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg='YOU DIED', move=False, align='center', font=FONT_GAME_OVER)