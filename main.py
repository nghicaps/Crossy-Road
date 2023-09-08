import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        if car.xcor() < -320:
            car.clear()
            car.hideturtle()
            car_manager.all_cars.remove(car)

    if player.ycor() > 280:
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.level_up()

screen.exitonclick()
