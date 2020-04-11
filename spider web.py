#Python program to draw spider web in turtle programming
import turtle

t = turtle.Turtle()
t.speed(0)

#Code for building radical thread
for i in range(6):
  t.forward(150)
  t.backward(150)
  t.right(60)

#Code for building spiral thread
side = 150
for i in range(15):
  t.penup()
  t.goto(0,0)
  t.pendown()
  t.setheading(0)
  t.forward(side)
  t.right(120)
  for j in range(6):
    t.forward(side)
    t.right(60)
  side = side - 10
