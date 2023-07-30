'''
Turtle Graphics, Tuples and Importing Modules
READING DOCUMENTATION

from turtle import Turtle
keyword module_name keyword thing_in_module
colorgram
매일매일 해야한다. 꾸준하게 해야 한다. 운동이랑 비슷하다
'''
from turtle import Turtle, Screen
import turtle
import random

bbss = Turtle()
##
# bbss_the_tuttle.shape("turtle")
# bbss_the_tuttle.color("red")
# bbss_the_tuttle.forward(100)
# bbss_the_tuttle.right(90)

##
# bbss.forward(100)
# bbss.right(90)
# bbss.forward(100)
# bbss.right(90)
# bbss.forward(100)
# bbss.right(90)
# bbss.forward(100)
# bbss.right(90)

# for _ in range(15):
#     bbss.forward(10)
#     bbss.penup()
#     bbss.forward(10)
#     bbss.pendown()

##
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         bbss.forward(100)
#         bbss.right(angle)
#
#
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)

colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue",
           "LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions = [0,90,180,270]
bbss.pensize(15)
bbss.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


for _ in range(200):
    # bbss.color(random.choice(colours))
    bbss.color(random_color())
    bbss.forward(30)
    bbss.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()