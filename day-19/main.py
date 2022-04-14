from turtle import Turtle, Screen
import random
tom1 = Turtle()
tom1.shape("turtle")
tom2 = Turtle()
tom2.shape("turtle")
tom3 = Turtle()
tom3.shape("turtle")
tom4 = Turtle()
tom4.shape("turtle")
tom5 = Turtle()
tom5.shape("turtle")
screen = Screen()
screen.setup(500, 500)
tom2.color("blue")

tom3.color("red")
tom4.color("purple")
tom5.color("yellow")
tom1.color("green")
tom1.penup()
tom2.penup()
tom3.penup()
tom4.penup()
tom5.penup()
tom1.goto(-240, 96)
tom2.goto(-240, 46)
tom3.goto(-240, 0)
tom4.goto(-240, -46)
tom5.goto(-240, -96)
turtles = [tom1, tom2, tom3, tom4, tom5]
bet = screen.textinput("Make bet: ", "Which will win: ")
if bet:
    race = True
while race:
    for i in turtles:
        move = random.randint(0, 10)
        i.forward(move)
        if i.xcor() > 250:
            wincol = i.pencolor()
            if bet == wincol:
                print("GANASTE")
            else:
                print("PERDISTE")
            race = False
screen.exitonclick()
