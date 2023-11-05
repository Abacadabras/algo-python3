
from turtle import *


angle = 80


def draw_line(length, deep):
    if deep == 1:
        forward(length)
        return

    length //= 3
    deep -= 1
    draw_line(length, deep)
    left(angle)
    draw_line(length, deep)
    right(2*angle)
    draw_line(length, deep)
    left(angle)
    draw_line(length, deep)


speed(0)
draw_line(500, 5)
right(120)
draw_line(500, 5)
right(120)
draw_line(500, 5)
mainloop()
