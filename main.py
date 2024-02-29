import turtle

from myShapes import *
from house import *
from stop import *

#the following function will lift then place the pen at the x,y position
movePen(-130,130)

turtle.pensize(2)
turtle.speed(9)

drwSqr(35)
movePen(10,130)

drwSqr(20,"blue")
movePen(-130,0)

drwHouse(50,"blue")
movePen(10,0)

drwHouse(50)
movePen(-130,-100)

drwOct(25)
movePen(10,-100)

drwOct(20,"blue")

turtle.Screen().exitonclick()
#drwTrngl(100)
