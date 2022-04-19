from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.XCOR = 0
        self.YCOR = 270
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(self.XCOR, self.YCOR)

    def writing_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 20, "normal"))
        # self.write((self.XCOR, self.YCOR), False)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Arial", 20, "normal"))