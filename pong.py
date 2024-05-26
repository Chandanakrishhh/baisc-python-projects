import turtle as t 
playerAscore = 0
playerBscore = 0 
windows = t.Screen()
windows.title("PONG GAME")
windows.bgcolor("black")
windows.setup(width=800,height=600) 
windows.tracer(0) #tracer() function is used to control the animation of turtle graphics
 
 #creating a paddle in the game
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("green")
leftpaddle.shapesize(stretch_wid = 5,stretch_len= 1) # strech_len This argument sets the stretching factor for the turtle's shape in the horizontal direction.
#shrech_width this argument sets the stretching factor for the turtle's shape in the vertical direction. In this case, it's set to 5, meaning the height of the turtle will be stretched by a factor of 5.
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating the rigthpaddle in the game
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("green")
rightpaddle.shapesize(stretch_wid = 5,stretch_len= 1)
rightpaddle.penup()
rightpaddle.goto(350,0) 


#creating the ball 
 
ball = t.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(5,5)
ballxdirection = 0.2
ballydirection = 0.2

#creating pen for scorecard
pen = t.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.ht()
pen.goto(0,260)
pen.write("score", align = "center",font = ('Arial',24,"normal"))


#moving the leftpaddle

def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 90
    leftpaddle.sety(y)
def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 90
    leftpaddle.sety(y)


#moving the leftpaddle

def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 90
    rightpaddle.sety(y)

def rigthpaddledown():
    y = rightpaddle.ycor()
    y = y - 90
    rightpaddle.sety(y)        

    #event handling
windows.listen()
windows.onkeypress(leftpaddleup,"w")
windows.onkeypress(leftpaddledown,"s")
windows.onkeypress(rightpaddleup,"Up")
windows.onkeypress(rigthpaddledown,"Down")

while True:
    windows.update() # update() function is used to manually update the turtle graphics window
    
    # moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)
    
    #setting up border
    
    if ball.ycor() > 290:
        ball.sety(290)   #to prevent the ball from going beyond the top wall.
        ballydirection = ballydirection *-1  #This ensures that the ball will bounce back down.
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection *-1   #The line ballxdirection = ballxdirection * -1 is responsible for changing the horizontal direction of the ball.
    if ball.xcor() > 390:
        ball.goto(0,0)
        ballxdirection = ballxdirection  
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("player A:{}             player B :{} ".format(playerAscore,playerBscore),align = 'center', font = ("Arial",24,"normal"))  
    if ball.xcor() < -390:
        ball.goto(0,0)
        ballxdirection = ballxdirection * -1 
        playerBscore = playerBscore + 1
        pen.clear() #It clears the previous score display (pen.clear()).
        pen.write("player A:{}             player B :{} ".format(playerAscore,playerBscore),align = 'center', font = ("Arial",24,"normal"))  

# handling the collusions
    if(ball.xcor() > 340) and (ball.xcor() < 350) and(ball.ycor()<rightpaddle.ycor() + 40 and ball.ycor()>rightpaddle.ycor() -40):
        ball.setx(340)
        ballxdirection= ballxdirection * -1

    if(ball.xcor() < -340) and (ball.xcor() > -350) and(ball.ycor()<leftpaddle.ycor() + 40 and ball.ycor()>leftpaddle.ycor() - 40): 
        ball.setx(-340)
        ballxdirection= ballxdirection * -1

   #ball.ycor() < rightpaddle.ycor() + 40: This checks if the y-coordinate of the ball is less than rightpaddle.ycor() + 40.
        # The value 40 here is the half-height of the right paddle.