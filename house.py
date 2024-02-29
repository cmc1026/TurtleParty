from turtle import * 

def drwSqrr(size, col = "red"):
  color(col)
  for i in range(4):
    forward(size)
    left(90)

def drwTrngle(size, col = "red"):
  color(col)
  for i in range(3):
    forward(size)
    left(120)
    
def drwHouse(size, col = "red"):
  drwSqrr(size,col)
  penup()
  left(90)
  forward(size)
  pendown()
  right(90)
  drwTrngle(size,col)
  right(90)
  forward(size)
  left(90)
