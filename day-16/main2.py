# from turtle import Turtle, Screen

# tom = Turtle()
# tom.shape("turtle")
# tom.color("yellow")
# my_screen = Screen()
# print()
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name", ["Pika", "Squirt"])
table.add_column("Type:", ["fire", "elec"])
print(table)
