from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle you bet would win?: ")


# Finish Line
def finish_line():
    dec = Turtle()
    dec.hideturtle()
    dec.penup()
    dec.goto(x=210, y=130)
    dec.pendown()
    dec.goto(x=240, y=130)
    dec.goto(x=225, y=130)
    dec.goto(x=225, y=-130)
    dec.goto(x=210, y=-130)
    dec.goto(x=240, y=-130)
    dec.penup()


colors = ["red", "yellow", "orange", "green", "blue", "aquamarine", "purple"]
turtles = []
y_pos = -90
i = 0

for name in range(0, 7):
    name = Turtle(shape="turtle")
    name.penup()
    name.color(colors[i])
    i += 1
    name.goto(x=-230, y=-y_pos)
    y_pos += 30
    turtles.append(name)

finish_line()

winning_distance = 225
if user_bet:
    is_race_on = True
    while is_race_on:
        random_distance = random.randint(0, 10)
        move_turtle = random.choice(turtles)
        move_turtle.forward(random_distance)
        moved_distance = move_turtle.xcor()
        turtle_racing = turtles.index(move_turtle)
        if moved_distance >= 225:
            is_race_on = False
            user_bet = colors.index(user_bet)
            if user_bet == turtle_racing:
                print("You have won the race!")
            else:
                print(f"You have lost the race. {colors[turtle_racing]} turtle has won the race!")

screen.exitonclick()
