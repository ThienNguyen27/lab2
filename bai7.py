from turtle import *
lt(90)
pencolor('#cf8f03')
x=150
y=60
for h1 in range (10):
    rt(y)
    fd(x)
    rt((180-y)/2)
    fd(x)
    rt(180-y)
    fd(x)
    rt(180-2*y)
    fd(x)
    rt(60) #xong hq1
penup()
lt(90)
bk(100)
rt(90)
pendown()
pencolor('#0b2c3c')
for h2 in range (10):
    rt(y)
    fd(x)
    rt((180-y)/2)
    fd(x)
    rt(180-y)
    fd(x)
    rt(180-2*y)
    fd(x)
    rt(60)
mainloop()