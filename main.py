import turtle
import math

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(dart=None):
  dart.penup()
  dart.goto(-360,0)
  dart.pendown()
  for x in range (-360,361):
    y=math.sin(math.radians(x))
    dart.goto(x,y)

def drawCosineCurve(dart=None):
  dart.penup()
  dart.goto(-360,0)
  dart.pendown()
  for x in range (-360,361):
    y=math.cos(math.radians(x))
    dart.goto(x,y)

def drawTangentCurve(dart=None):
  dart.penup()
  dart.goto(-360,0)
  dart.pendown()
  for x in range (-360,361):
    y=math.tan(math.radians(x))
    dart.goto(x,y)

def setupWindow(wn=None):
  wn.setworldcoordinates(-360,-1,360,1)
  wn.bgcolor("blue")

# def setupAxis(dart=None):
#   for x in range(4):
#     dart.penup()
#     dart.goto(0,0)
#     dart.right(90)
#     dart.pendown()
#     dart.forward(1)
    
 
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)
    

    #Part B
    setupWindow(wn)
    # setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()

main()