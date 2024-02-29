from turtle import * 

def drwSqr(size, col = "red"):
  color(col)
  for i in range(4):
    forward(size)
    left(90)
    
def drwRect(ht, wdth, col = "red"):
  color(col)
  for i in range(2):
    forward(ht)
    left(90)
    forward(wdth)
    left(90)

def drwTrngl(size, col = "red"):
  color(col)
  for i in range(3):
    forward(size)
    left(120)
    
def movePen(x,y):
  penup()
  goto(x,y)
  pendown()
