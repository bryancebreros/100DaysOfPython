from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for pos in START_POS:
            self.add(pos)

    def add(self, pos):
        new_squ = Turtle("square")
        new_squ.color("white")
        new_squ.penup()
        new_squ.goto(pos)
        self.squares.append(new_squ)

    def extend(self):
        self.add(self.squares[-1].position())
    def refresh(self):
        self.squares.clear()
        self.head.goto(1000, 1000)
        self.__init__()
    def move(self):
        for squ in range(len(self.squares) - 1, 0, -1):
            newx = self.squares[squ - 1].xcor()
            newy = self.squares[squ - 1].ycor()
            self.squares[squ].goto(newx, newy)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
