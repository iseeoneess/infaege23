from turtle import *

tracer(0)
screensize(10000, 10000)

r = 30

for i in range(11):
    fd(r*4)
    rt(60)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*r,y*r)
        dot(3, 'blue')

update()
exitonclick()