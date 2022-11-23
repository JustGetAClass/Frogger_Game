from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.level = 0
        self.hideturtle()
        self.goto(0, 270)
        self.update_level()

    def update_level(self):
        self.write(f"level : {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def add_level(self):
        self.clear()
        self.level += 1
        self.update_level()
