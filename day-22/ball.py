from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def bounce(self):
        self.ymove *= - 1
        self.move_speed *= 0.9

    def collision(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.xmove *= -1
