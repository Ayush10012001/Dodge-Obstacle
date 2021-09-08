from turtle import Turtle
import random
timerun=10
colors=["red","blue","green","yellow","orange"]
class Car_manage():
    def __init__(self):
        self.cars=[]
        self.movedistance=timerun

    def make_car(self):
        random_move = random.randint(1, 6)
        if random_move == 1:
            new_car=Turtle("square")
            new_car.penup()
            new_car.color(random.choice(colors))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            randomy=random.randint(-250,250)
            new_car.goto(500,randomy)
            self.cars.append(new_car)

    def move_car(self):
        for i in self.cars:
            i.backward(self.movedistance)

    def levelup(self):
        self.movedistance+=5






