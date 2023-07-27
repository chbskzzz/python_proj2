'''
함수를 인자로 사용하여 전달하기
Higher Order Functions
다른 함수와 함께 작동하는 함수를 고차함수라고 한다
def calculator(n1, n2, func):
    return func(n1, n2)
이벤트 리스너 활용
더 많이 실수하고 더 많이 고생을 하면 많이 배운다
'''

# turtle1


'''
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# screen.onkey(key="space", fun=move_forwards)
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
'''

# turtle2
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400) # positional argument
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    print(new_turtle)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winnder!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winnder!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()