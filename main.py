from turtle import Turtle,Screen
from player import Player
from cars import Car_manage
from scorecard import Score
import time
screen=Screen()
screen.bgcolor("white")
screen.setup(width=1000, height=600)
screen.tracer(0)

car=Car_manage()
run=Player()
score=Score()
screen.listen()
screen.onkey(run.move,"Up")
runspeed=0.1
gameison=True
while gameison:
    time.sleep(runspeed)
    screen.update()
    car.make_car()
    car.move_car()
    if run.ycor() > 280:
        run.goto(0,-280)
        car.levelup()
        score.levelup()

    for i in car.cars:
        if i.distance(run) < 20:
            gameison=False
            score.gameover()


screen.exitonclick()

