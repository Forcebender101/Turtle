import turtle as t
import random
#setup color list
Color = []
#Functions
def Star():
  for i in range(5):
    t.color(Color[i])
    t.fd(Size)
    t.rt(144)
def Polygon():
  for i in range(n):
    t.color(Color[i])
    t.fd(Size)
    t.lt(g)
def Circle():
  t.color(color)
  t.circle(Size)
#Get measurements and choice
Size = int(input("How big do you want each side to be?\n"))
shape = input("Do you want to draw a polygon, a circle or a star\n (P/C/S)\n").lower()
#What to do for each shape
if shape == "p":
  n = int(input("How many sides does the shape have?\n"))
  colorB = input("Should the shape have colors\n     (y/n)\n").lower()
  if colorB == "y" or colorB == "yes":
    for i in range(n):
      Color.append(input("What should color number " + str(i+1) + " be.\n").lower()) 
  else:
    for i in range(n):
      Color.append("black")
  AngleTotal = (n-2)*180
  AngleEach = AngleTotal/n
  g = 180-AngleEach
  Polygon()
elif shape == "s":
  colorB = input("Should the shape have colors\n     (y/n)\n").lower()
  if colorB == "y" or colorB == "yes":
    for i in range(5):
      Color.append(input("What should color number " + str(i+1) + " be.\n").lower())
  else:
    Color = ["black","black","black","black","black"]
  Star()
elif shape == "c":
  color = input("What color should it be?").lower()
  Circle()