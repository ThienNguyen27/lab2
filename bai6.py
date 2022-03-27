from turtle import *
penup()
left(180)
forward(80)
right(180)
pendown()
for hcn in range(2):
    forward(150)
    left(90)
    forward(100)
    left(90)

left(90)
pencolor('#de5246')
for m in range(15):
    pencolor('#de5246')
    forward(100)
    right(130)
    forward(100)
    left(81)
    forward(98)
    right(131)
    forward(100)
    penup()
    right(90)
    forward(150)
    right(90)
    pendown()


mainloop()