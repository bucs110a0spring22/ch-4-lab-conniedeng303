import turtle
import math

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(dart=None,startofgraph_x=0,startofgraph_y=0):
  dart.penup()
  dart.goto(startofgraph_x,startofgraph_y)
  dart.pendown()
  for x in range (-360,361):
    y=math.sin(math.radians(x))
    dart.goto(x,y)

def drawCosineCurve(dart=None):
  dart.penup()
  dart.goto(-360,1)
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
  wn.bgcolor("green")

def setupAxis(dart=None):
  dart.setheading(90)
  for i in range(4):
    dart.goto(0,0)
    dart.pendown()
    dart.forward(360)
    dart.right(180)
    dart.goto(0,0)
    dart.forward(1)
    dart.right(90)


    # dart.right(180)
    # dart.goto(0,0)
    # dart.pendown()
    # dart.forward(360)
    # dart.goto(0,0)
    # dart.right(90)
    # dart.forward(1)
    # dart.goto(0,0)
    # dart.right(90)
    # dart.forward(360)
    # dart.goto(0,0)
    # dart.right(90)
    # dart.forward(1)


#Additional Functions:
  # -inverse graphs
#Parameters:
  #
#Return a Value:
  

  
#FEATURES
#4 quadrants, change color, if turtle ends up on the right color then it traces a heart  

# def RedLightGreenLight(dart=None,orange=None):
#   question = str(input("Start game? Type Yes or No?"))
#   if question == "yes":
#     dart.clear()
#     x_value = int(input("Pick your x value"))
#     y_value = int(input("Pick your x value"))
#     dart.goto(x_value,y_value)
#     orange_x_value = random.uniform(-1,1)

#     if 
    
#     print("Done")
#   else:
#     quit()


    

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    # orange = turtle.Turtle()
    # orange = speed(0)
    dart.speed(0)
    # drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    # drawSineCurve(dart,-360,0)
    # drawCosineCurve(dart)
    # drawTangentCurve(dart)
    # RedLightGreenLight(dart)
    wn.exitonclick()

main()