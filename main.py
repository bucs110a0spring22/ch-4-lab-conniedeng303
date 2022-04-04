import turtle
import math
from mpmath import csc
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

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
    y=math.cos(math.radians(x))
    dart.goto(x,y)

def drawTangentCurve(dart=None):
  startendpoints_tan = (-360,0)
  dart.penup()
  dart.goto(startendpoints_tan)
  dart.pendown()
  for x in range (-360,361):
    y=math.tan(math.radians(x))
    dart.goto(x,y)

def drawCSCCurve(dart=None):
  startendpoints_csc = (-360,0)
  dart.penup()
  dart.goto(startendpoints_csc)
  dart.pendown()
  for x in range(-360,361):
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

#Parameters:
  #   
#Return a Value:

# def ReturnSinFunctionValue(x=0,y=0):
#   x = int(input("type a number between -360 to 360")
#   y = math.tan(math.radians(x))
#   return y
  
  
#FEATURES
#4 quadrants, change color, if turtle ends up on the right color then it traces a heart  


# def RedLightGreenLight(dart=None,orange=None):
#   question = str(input("Pick quadrant, and make sure that it isn't touching Start game? Type Yes or No?"))
#   if question == "yes":
#     dart.clear()
#     x_value = int(input("Pick your x value"))
#     y_value = int(input("Pick your x value"))
#     dart.goto(x_value,y_value)
#     orange_x_value = random.uniform(-360,360)
#     orange_y_value = random.uniform(-1,1)
#     for i in range(100):
      

#     if orange_x_value < 0 and 
#       print("Congrats! Here is a heart for your troubles!")

#     else:
#       print("L")
      
    
#     print("Done")
#   else:
#     quit()


  
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    orange = turtle.Turtle()
    orange = speed(0)
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    # setupWindow(wn)
    # setupAxis(dart)
    # dart.speed(0)
    # drawSineCurve(dart,-360,360)
    # drawCosineCurve(dart,-360,360)
    # drawTangentCurve(dart)
    # dart.clear()
    # print("Recip Time...")
    # setupAxis(dart)
    # drawCSCCurve(dart)
    # RedLightGreenLight(dart)
    # returnCOSfunction(-360,360)
    # wn.exitonclick()

main()