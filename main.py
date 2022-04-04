import turtle
import math
from mpmath import csc
import random

def drawSineCurve(dart=None,startofgraph_x=0,endofgraph_y=0):
  startpoints_sin = (-360,0)
  dart.penup()
  dart.goto(startpoints_sin)
  dart.pendown()
  for x in range (startofgraph_x,endofgraph_y):
    y=math.sin(math.radians(x))
    dart.goto(x,y)

def drawCosineCurve(dart=None,startofgraph_begrange=0, startofgraph_endrange=0):
  startpoints_cos = (-360,1)
  dart.penup()
  dart.goto(startpoints_cos)
  dart.pendown()
  for x in range (startofgraph_begrange,startofgraph_endrange+1):
    y_cos_value = math.cos(math.radians(x))
    dart.goto(x,y_cos_value)

def drawTangentCurve(dart=None,startofgraph_begrange=0, startofgraph_endrange=0):
  startendpoints_tan = (-360,0)
  dart.penup()
  dart.goto(startendpoints_tan)
  dart.pendown()
  for x in range (startofgraph_begrange,startofgraph_endrange+1):
    y_tan_value =math.tan(math.radians(x))
    dart.goto(x,y)

#Additional Function:
def drawCSCCurve(dart=None,startofgraph_begrange=0, startofgraph_endrange=0):
  setupAxis(dart)
  startendpoints_csc = (-360,0)
  dart.penup()
  dart.goto(startendpoints_csc)
  dart.pendown()
  for x in range(startofgraph_begrange,startofgraph_endrange+1):
    if (x==0):
      continue
    y=csc(math.radians(x))
    dart.goto(x,y)   

def setupWindow(wn=None):
  wn.setworldcoordinates(-360,-5,360,5)
  wn.bgcolor("green")

def setupAxis(dart=None):
  dart.setheading(90)
  for i in range(4):
    dart.goto(0,0)
    dart.pendown()
    dart.forward(1)
    dart.right(90)
    dart.goto(0,0)
    dart.forward(360)

#Return Functions:
def ReturnSinFunctionValue():
  x_sin = int(input("type a number between -360 to 360"))
  y_sin_value = math.sin(math.radians(x_sin))
  return y_sin_value

def ReturnCSCFunctionValue():
  x_csc = int(input("type a number between -360 to 360"))
  y_csc_value = csc(math.radians(x_csc))
  return y_csc_value

#Parameters:
def graphswithperiods(dart=None,period=0,yaxis=0,startofgraph_begrange=0, startofgraph_endrange=0):
  for x_period in range(startofgraph_begrange,startofgraph_endrange):
    y_period = period*(math.sin(math.radians(x_period)))+yaxis
    dart.goto(x_period,y_period)

def catchooses():
  cat_random = int(random.randrange(1,3))
  if cat_random == 1:
    print("Cat has chosen the left side")
    return True
  else:
    print("Cat has chosen the right side")
    return False
    
def RedLightGreenLight(dart=None):
  dart.shape("turtle")
  dart.goto(0,0)
  question = str(input("Let's play a game of cat and mouse. Pick either the left or right side of the graph. A cat will only stomp on one side, so you have a 50/50 chance of surviving. Start game? Type yes or no."))
  if question == "yes":
    dart.clear
    direction = str(input("Pick left or right."))
    catstomp = catchooses()
    if direction == "left" and catstomp == False:
      dart.goto(150,150)
      dart.color("red")
      print("You made it out alive!")
    elif direction == "left" and catstomp == True:
      dart.goto(150,-150)
      dart.color("blue")
      print("Nope! You died!")
    elif direction == "right" and catstomp == True:
      dart.goto(-150,-150)
      dart.color("red")
      print("You made it out alive!")
    elif direction == "right" and catstomp == True:
      dart.goto(-150,150)
      print("Nope! You died!")
    print("Done")
  else:
    quit()

def main():
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)

    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    # drawSineCurve(dart,-360,360)
    # drawCosineCurve(dart,-360,360)
    # drawTangentCurve(dart,-360,360)
    # dart.clear()

    # #Return Functions
    # result_sin = ReturnSinFunctionValue()
    # result_csc = ReturnCSCFunctionValue()
    # print("The value you have selected for your x value in a SIN graph is equal to",result_sin)
    # print("The value you have selected for your x value in a CSC graph is equal to",result_csc)

    # #Additional Function
    # print("Let's Draw the Recipocal of Sin and Shift the Graph...")
    # drawCSCCurve(dart,-360,360)

    # #Parameter Function
    # graphswithperiods(dart,10,2,-360,360)
    # dart.clear()
  
    #Feature
    RedLightGreenLight(dart)
    wn.exitonclick()

main()