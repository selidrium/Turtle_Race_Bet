from turtle import Turtle, Screen
import random

is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race?").lower()

turtle_colors = ["red", "blue", "black", "orange", "purple", "yellow"]
y_ranges = [90, 60, 30, 0, -30, -60]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(x=-240, y=y_ranges[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won! {winning_turtle} has won the race!")
            else:
                print(f"You lost! {winning_turtle} has won the race!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
