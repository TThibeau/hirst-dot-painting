from extract_colors import color_list
import turtle as t
from random import choice

def random_color():
    selected = choice(color_list)
    mypen.color(selected)

def update_pos(nr_of_dots):
    width = 600
    step_size = int(width/nr_of_dots)
    print(step_size)
    for j in range(nr_of_dots):
        for i in range(0,nr_of_dots):
            mypen.penup()
            mypen.setposition(-300+i*step_size,-300+j*step_size)
            mypen.pendown()
            random_color()
            mypen.dot()
        
            
t.colormode(255)
mypen = t.Turtle()
mypen.speed("fastest")
mypen.pensize(15)
mypen.hideturtle()
update_pos(20)
