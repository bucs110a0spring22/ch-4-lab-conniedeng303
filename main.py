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
    y_sin_value = math.sin(math.radians(x))
    dart.goto(x,y_sin_value)

def drawCosineCurve(dart=None,startofgraph_begrange=0, startofgraph_endrange=0):
  startpoints_cos = (-360,1)
  dart.penup()
  dart.goto(startpoints_cos)
  dart.pendown()
  for x in range (startofgraph_begrange,startofgraph_endrange+1):
    y_cos_value = math.cos(math.radians(x))
    dart.goto(x,y_cos_value)

def drawTangentCurve(dart=None,startofgraph_begrange=0, startofgraph_endrange=0):
  startpoints_tan = (-360,0)
  dart.penup()
  dart.goto(startpoints_tan)
  dart.pendown()
  for x in range (startofgraph_begrange,startofgraph_endrange+1):
    y_tan_value = math.tan(math.radians(x))
    dart.goto(x,y_tan_value)

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
    y_value_csc = csc(math.radians(x))
    dart.goto(x,y_value_csc)   

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
  for x_period in range(startofgraph_begrange,startofgraph_endrange+1):
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

# def rectangle_left(dart=None):
#   dart.begin_fill()
#   dart.turtlesize(2)
#   dart.goto(0,-5)
#   dart.color("red")
#   for i in range(3):
#     dart.forward(10)
#     dart.left(90)
#     dart.forward(360)
#     dart.left(90)
#   dart.end_fill()

# def rectangle_right(dart=None):
#   dart.begin_fill()
#   dart.turtlesize(2)
#   dart.goto(0,-5)
#   dart.color("red")
#   for i in range(3):
#     dart.forward(10)
#     dart.right(90)
#     dart.forward(360)
#     dart.right(90)
#   dart.end_fill()

def CatandMouse(dart=None):
  setupAxis(dart)
  dart.shape("turtle")
  dart.goto(0,0)
  dart.goto(300,300)
  question = str(input("Let's play a game of cat and mouse. Pick either the left or right side of the graph. A cat will only stomp on one side, so you have a 50/50 chance of surviving. Start game? Type yes or no."))
  if question == "yes":
    dart.clear()
    direction = str(input("Pick left or right."))
    catstomp = catchooses()
    if direction == "left" and catstomp == False:
      print("You made it out alive!")
    elif direction == "left" and catstomp == True:
      print("Nope, you got squashed!But you are still alive!")
    elif direction == "right" and catstomp == True:
      print("You made it out alive!")
    elif direction == "right" and catstomp == False:
      print("Nope, you got squashed!But you are still alive!")
  else:
    quit()

def toxicfood(dart=None):
  dart.penup()
  dart.clear()
  dart.goto(0,0)
  food_random = int(random.randrange(1,3))
  dart.pendown()
  if food_random == 1:
    dart.color("purple")
    dart.begin_fill()
    dart.circle(60)
    dart.end_fill()
    return False
  else:
    dart.fillcolor('orange')
    dart.begin_fill()
    dart.circle(60)
    dart.end_fill()
    return True

def StoryLine(dart=None):
  toxicfood_var = toxicfood(dart)
  print("The cat exclaims,""For surviving my wrath, I'll allow you to eat a single orange.""The cat presents you with an orange.Are oranges supposed to be that color?")
  answer = str(input("Do you eat this orange? yes or no?"))
  if toxicfood_var == True and answer == "yes":
    print("Hazzah! The cat was a true ally all along.")
  elif toxicfood_var == True and answer == "no":
    print("The cat feels hurt. That orange wasn't poisoned.")
  elif toxicfood_var == False and answer == "no":
    print("You dodged a bullet. That orange was packed with poison.")
  else:
    print("Oranges are not that color. You have been betrayed by the most obvious enemy.")
  

def main():
  wn = turtle.Screen()
  wn.tracer(5)
  dart = turtle.Turtle()
  dart.speed(0)
  
  setupWindow(wn)
  setupAxis(dart)
  dart.speed(0)
  drawSineCurve(dart,-360,360)
  drawCosineCurve(dart,-360,360)
  drawTangentCurve(dart,-360,360)
  dart.clear()
  
  # #Return Functions
  result_sin = ReturnSinFunctionValue()
  result_csc = ReturnCSCFunctionValue()
  print("The value you have selected for your x value in a SIN graph is equal to",result_sin)
  print("The value you have selected for your x value in a CSC graph is equal to",result_csc)
  
  # #Additional Function
  print("Let's Draw the Recipocal of Sin and Shift the Graph...")
  drawCSCCurve(dart,-360,360)
  
  # #Parameter Function
  graphswithperiods(dart,10,2,-360,360)
  dart.clear()
  
  #Feature
  wn.setworldcoordinates(-360,-360,360,360)
  CatandMouse(dart)
  StoryLine(dart)
  wn.exitonclick()

main()