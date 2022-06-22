from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()  # to not show the turtle on screen
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # method of turtle to write some text on screen

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)  # method of turtle to write some text on screen

    def increase_score(self):
        self.score += 1
        self.clear()  # So everytime score gets updated, it do not overwrites on the previous score
        self.update_scoreboard()

        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)




