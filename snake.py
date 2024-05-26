import turtle
import time
import random 
delay = 0.1 
score = 0
highestscore = 0
bodies = []   #snake body
s = turtle.Screen()   #screen of the game
s.title("Snakegame")
s.bgcolor("white")
s.setup(width = 600 , height = 600)
head = turtle.Turtle() #creating head of the snake
head.speed(0)  #means that the turtle will move at the fastest speed 
head.shape("circle")
head.color("black")
head.fillcolor("black")
head.penup()
head.goto(0,0) #goto() method is used to move the turtle to a specified position on the screen.
head.direction = "stop" #stop" (without spaces), and it is used to represent the initial direction of the snake's head.
food = turtle.Turtle() # creating the food 
food.speed(0)
food.shape("circle")
food.color("red")
food.fillcolor("red")
food.penup()
food.ht()  #This hides the turtle (makes it invisible). It's often done when you want to set up the initial state of the turtle without showing it on the screen.
food.goto(0,200)
food.st() #this shows the turtle (makes it visible). It's called after positioning the turtle to make it visible at the specified location.
sb = turtle.Turtle() #creating the score board
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score = 0  |  heigthestscore = 0")
def moveup():
    if head.direction != "down":
        head.direction = "up"
def movedown():        
    if head.direction != "up":
        head.direction = "down"
def moveleft():       
    if head.direction != "rigth":
        head.direction = "left"
def moveright():        
    if head.direction != "left":
        head.direction ="rigth"
def movestop():
    head.direction = "stop"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20) 
    if head.direction == "rigth":
        x = head.xcor()
        head.setx(x + 20)  
s.listen() #event handling 
s.onkey(moveup,"Up")   
s.onkey(movedown,"Down")               
s.onkey(moveleft,"Left")  
s.onkey(moveright,"Right")  
s.onkey(movestop,"space") 
while True:
    s.update()  # this is to update the screen
    #to check if theres no collision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)            
    #to check if theres no collision with food
    if head.distance(food) < 20:  #distance between the food and the head
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)               #move the food to the new random place


    #to check if theres no collision with its own body
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("grey")
        body.fillcolor('grey')
        bodies.append(body) #appendin the new body/block at the end
         
        #increse the score 
        score += 10 
        #change delay
        delay -= 0.001 

        #update the highestscore 
        if score >  highestscore:
           highestscore = score
        sb.clear()
        sb.write("Score : {} highestscore :{}".format(score,highestscore))  
        # to move the snake body
    for index in range(len(bodies)-1,0,-1):
            x = bodies[index - 1].xcor()
            y = bodies[index - 1].ycor()
            bodies[index].goto(x,y)
    if len(bodies) > 0:
            x = head.xcor()
            y = head.ycor()
            bodies[0].goto(x,y)
    move()
    for body in bodies:
            if body.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                for body in bodies:
                    body.ht()
                bodies.clear()
                score = 0
                delay = 0.1
                sb.clear()
                sb.write("Score : {} highestscore :{}".format(score,highestscore)) 
    time.sleep(delay)
s.mainloop()

                







        






       



