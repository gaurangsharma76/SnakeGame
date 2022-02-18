from turtle import Turtle




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", False, align="Center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="Center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align="Center", font=("Arial", 18, "normal"))
