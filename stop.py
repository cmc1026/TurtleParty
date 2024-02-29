from turtle import * 

def drwRect(ht, wdth, col = "red"):
  color(col)
  for i in range(2):
    forward(ht)
    left(90)
    forward(wdth)
    left(90)

def drwOct(size, col = "red"):
  color(col)
  for i in range(8):
    forward(size)
    left(45)
  forward((size/8)*3)
  right(90)
  drwRect(size*2,(size/8)*2,col)
  right(90)
  forward((size/8)*3)
  right(180)
