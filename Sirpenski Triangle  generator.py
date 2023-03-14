import turtle 
import math 
ddOriginal = 150
dd = 150
sc=turtle.Screen()
turtle = turtle.Turtle()

screenx, screeny = 800, 900
sc.tracer(2,1000)
def resetTurtle():
  turtle.penup()
  turtle.goto(0,(0.86602540378*ddOriginal))
  turtle.pendown()
  
def equilaterialTriangle():
  turtle.begin_fill() 
  for _ in range(3):
    turtle.forward(-dd)
    turtle.left(120)
  turtle.end_fill()

turtle.goto(-dd/2,0)
for _ in range(3):
    turtle.forward(dd)
    turtle.left(120)
#determines number of iterations of the fractal 
n = 1
iterateColumnsBy = 0
#if you change the range up here then it changes the number of times this thing iterates by 
for p in range(5):
  resetTurtle()
  dd = ddOriginal/2**n
  i = 0 
  iterateColumnsBy = int(2**n/2)
  for _ in range (iterateColumnsBy):
    resetTurtle()
    turtle.right(60)
    turtle.forward(dd+(i*dd*2))
    turtle.left(60)
    equilaterialTriangle()
    for _ in range (1+(i*2)-1):
        turtle.penup()
        turtle.forward(-dd)
        turtle.pendown()
        equilaterialTriangle()
    i += 1 
  n += 1 
  print(n)
