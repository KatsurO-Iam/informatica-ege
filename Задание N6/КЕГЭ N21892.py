from turtle import *

screensize(5000,5000)
k = 40

right(90)
tracer(0)
pendown()
for i in range(7):
    right(45)
    fd(11 * k)
    right(45)
penup()
for x in range(-20, 50):
    for y in range(-20, 100):
        goto(x * k, y * k)
        dot(5, "red")

done()