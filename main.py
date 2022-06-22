import time
from turtle import Screen, Turtle
from car_manager import CarManager
from scoreboard import Scoreboard


starting_position = (0, -280)
move_distance = 10
finish_line_y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.penup()
        self.goto(0, -280)
        self.speed = move_distance
        self.left(90)


player = Player()
limit = Turtle()
limit.hideturtle()
limit.penup()
limit.goto(0, 280)


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


def move():
    player.forward(10)


screen.onkey(move, "w")
screen.listen()
my_car = CarManager()


def check_if_win():
    if player.distance(limit) < 1:
        return True
    else:
        return False


scoreboard = Scoreboard()
scoreboard.WriteScore()
game_is_on = True
while game_is_on:
    if check_if_win():
        player.goto(0, -280)
        scoreboard.IncrementScore()
        my_car.IncrementSpeed()
    time.sleep(0.1)
    screen.update()
    my_car.create_car()
    my_car.move_cars()
    for i in my_car.all_cars:
        if player.distance(i) < 18:
            scoreboard.GameOver()
            game_is_on = False


screen.exitonclick()
