from turtle import Turtle, Screen
import random

is_racing = False
lst_turtle = []

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make a Guess", prompt="Enter the color of turtle that goes first: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]

for index in range(6):
    race = Turtle(shape="turtle")
    race.color(colors[index])
    race.penup()
    race.goto(x=-230, y=y_pos[index])
    lst_turtle.append(race)

if bet:
    is_racing = True
while is_racing:

    for turtle in lst_turtle:
        if turtle.xcor() > 230:
            is_racing = False
            win_clr = turtle.pencolor()
            if win_clr == bet:
                print("You've won! You guessed it right..")
            else:
                print(f"You loose! {win_clr} won the race.")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()
