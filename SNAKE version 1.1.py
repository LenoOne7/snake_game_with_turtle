

import turtle
import math
import random
import time

# Game flow control variable
running = True

def enterKeyOff():
    pass


def enterKeyOn():
    return "Return"


#window title and background
turtle.title("Snake v1.1 by CIT115")
window = turtle.Screen()
window.bgcolor('black')
window.setup(600,600)
window.tracer(0, 0)

#Global variables for set up
fGameSpeed = float()

startGame = True
while startGame == True:
    # Start screen title and title animation
    gameName = turtle.Turtle()
    gameName.hideturtle()
    gameName.penup()
    gameName.color("green")
    gameName.shape("turtle")
    gameName.setposition(-140, 200)
    gameName.pendown()
    gameName.write("~~~~SNAKE v1.1~~~~", False, align="left", font=("Verdana", 18, "bold"))
    # TODO make a cool geometric drawing. import math

    # Start screen game control message
    sMOVEMENT_MSG = '''Control the snake with\nthe up, down, left, and right\nkeys on your keyboard.
                    \nYou can not turn back into\nyour direction of travel
                    \nObjective:\nEats as many apples as possible!\n\n    Enjoy!     \n\nPress Enter to continue'''
    gameCntrlMsg = turtle.Turtle()
    gameCntrlMsg.hideturtle()
    gameCntrlMsg.penup()
    gameCntrlMsg.color("green")
    gameCntrlMsg.setposition(-140, -100)
    gameCntrlMsg.pendown()
    gameCntrlMsg.write(sMOVEMENT_MSG, False, align="left", font=("Verdana", 14, "normal"))

    #pause before prompt
    #turtle.ontimer(None, 1500)

    #pause to wait for enter button to be pressed
    if running:                                     # same thing as running == True
        turtle.listen()
        turtle.onkeypress(enterKeyOff, "Return")
        running = False



    #user set up
    userName = turtle.textinput("User name", "Enter your name:")

    #game speed control
    fSetGameSpeed = turtle.numinput("Game speed", "Enter 1 for slow\nEnter 2 for medium\nEnter 3 for fast")
    if int(fSetGameSpeed) == 1:
        fGameSpeed = 0.13
    elif int(fSetGameSpeed) == 2:
        fGameSpeed = 0.1
    else:
        fGameSpeed = 0.075

    #pause before game start
    turtle.ontimer(None, 1000)
    #clean up text
    turtle.clearscreen()
    startGame = False


#creating the play area
window = turtle.Screen()
window.bgcolor('black')
window.setup(600,600)
window.tracer(0, 0)

#creating a border representing the play area

border = turtle.Turtle()
border.penup()
border.setposition(-285,-285)
border.pendown()
border.speed(0)
border.pencolor('white')
border.pensize(3)
for side in range(4):
    border.forward(570)
    border.left(90)
border.hideturtle()




#creating the head of the snake

head = turtle.Turtle()
head.shape('square')
head.color('green')
head.speed(0)
head.penup()
head.goto(-250,0)




#If snake head position is touching the border, end the game
def borderTouched():
    iBORDER_POS = 273
    iBORDER_NEG = -273
    xPosHead = int(head.xcor())
    yPosHead = int(head.ycor())
    if xPosHead >= iBORDER_POS or xPosHead <= iBORDER_NEG:        #Left or right out of bounds
        turtle.done()
    elif yPosHead >= iBORDER_POS or yPosHead <= iBORDER_NEG:        #Top or bottom out of bounds
        turtle.done()





    
        


#defining movement functions to be called by direction checker function
iMOVEMENT_AMOUNT = 20

def moveUp():
    if head.heading() != 270:
        head.seth(90)
      

def moveLeft():
    if head.heading() != 0:
        head.seth(180)
   
    
      
def moveDown():
    if head.heading() != 90:
        head.seth(270)
    
   
def moveRight():
    if head.heading() != 180:
        head.seth(0)
   
  

#direction checker function that calls the movement function associated with it
def movement():
    if head.heading() == 90:
        head.sety(head.ycor() + iMOVEMENT_AMOUNT )
    if head.heading() == 180:
        head.setx(head.xcor() - iMOVEMENT_AMOUNT )
    if head.heading() == 270:
        head.sety(head.ycor() - iMOVEMENT_AMOUNT )
    if head.heading() == 0:
        head.setx(head.xcor() + iMOVEMENT_AMOUNT )


#calling movement functions with user input
turtle.listen()
turtle.onkeypress(moveUp, "Up")
turtle.onkeypress(moveLeft, "Left")
turtle.onkeypress(moveDown, "Down")
turtle.onkeypress(moveRight, "Right")



#body array that will have turtles appended to it

snakeArray = []




#apple object to be randomly generated later on
apple = turtle.Turtle()
apple.hideturtle()
apple.shape('square')
apple.penup()
apple.color('red')
apple.speed(0)
apple.goto(-90,-100)
apple.showturtle()



#updates the length of the snake body, and appends it to the snakeArray

def lengthUpdater():
    templateTurtle = turtle.Turtle()
    templateTurtle.setposition(-400,-200)
    templateTurtle.shape('square')
    templateTurtle.color('blue')
    templateTurtle.speed(0)
    templateTurtle.penup()
    snakeArray.append(templateTurtle)

#detect collision with snake head and apple and generates a new apple
def appleTouched():
    if head.distance(apple) < 20:
        applex = random.randrange(-270, 270, 20)
        appley = random.randrange(-270, 270, 20)
        for i in range(len(snakeArray)):
            if head.distance(applex, appley) < 60 or snakeArray[i].distance(applex, appley) < 60:
                appleTouched()
            
        else:                                                                               
            apple.goto(applex, appley)
            lengthUpdater()




        
#iterates through the snakeArray and tracks the snake head for each block
def headFollow():
    if len(snakeArray) > 1:
        for i in range(-1, len(snakeArray) - 1, 1):
            snakeArray[i].goto(snakeArray[i + 1].xcor(), snakeArray[i + 1].ycor())
        snakeArray[0].goto(head.xcor(), head.ycor())
        
            
    elif len(snakeArray) != 0:
        snakeArray[0].goto(head.xcor(), head.ycor())
    

#self collision checker
def selfCollision():
    for j in range(len(snakeArray)):
        if head.distance(snakeArray[j]) < 20:
            turtle.done()
        


# TODO make running = true if user hits enter at the prompt which is spearated from the control flow
running = True      # TODO change to False once this loop is seperated by a control flow
while running:
    borderTouched()
    appleTouched()
    headFollow()
    movement()
    selfCollision()
    window.update()
    time.sleep(fGameSpeed)
    
 
   


    







    

    



