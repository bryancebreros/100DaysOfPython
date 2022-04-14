from mimetypes import init


from turtle import Turtle
ALIGMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score = {self.score}    High Score = {self.high_score}", align=ALIGMENT,
                   font=FONT)
    def hs(self):
        with open("data.txt", "w") as data:
            self.high_score = self.score
            data.write(f"{self.high_score}")
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGMENT,
    #                font=FONT)

    def increase(self):
        self.score += 1
        if self.score > self.high_score:
            self.hs()
        self.clear()
        self.update()
    def again(self):
        self.score = 0
        self.update()