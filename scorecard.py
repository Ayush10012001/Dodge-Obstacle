from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-420, 250)
        self.color("black")
        self.write(f"LEVEL: {self.level}", align="center", font=("courier", 20, "normal"))

    def updatescore(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align="center", font=("courier", 20, "normal"))
    def levelup(self):
        self.level+=1
        self.updatescore()

    def gameover(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0,0)
        self.write(f"GAME OVER \nFinal Score {self.level}", align="center", font=("courier", 20, "normal"))