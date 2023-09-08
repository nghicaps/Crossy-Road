from turtle import Turtle

FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.home()
        self.write("Game Over", False, "center", FONT)
