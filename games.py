import turtle
import random

lives=5
game= turtle.Screen()
game.title('Egg Drop')
game.addshape('C:\Game project B\BG.gif') #line6
game.bgpic('C:\Game project B\BG.gif')    #line7
game.setup(width=900, height=700)

#adding basket
#basket
basket= turtle.Turtle()
basket.speed(0)
game.addshape('C:\Game project B\BSS.gif') #line12
basket.shape('C:\Game project B\BSS.gif')  #line13
basket.penup()
basket.goto(0,-200)
basket.direction='stop'

#instructions
egg= turtle.Turtle()
egg.speed(0)
egg.shape('circle')
egg.color('burlywood')
egg.shapesize(outline=14)
egg.penup()
egg.goto(-310,300)

text1=turtle.Turtle()
text1.penup()
text1.goto(-650,280)
style= ('Courier', 20, 'bold')
text1.color('red')
text1.write('Winning target : 15    eggs .',font=style, align='left', move='True')
turtle.hideturtle()
l=turtle.Turtle()
l.write('Lives:{}'.format(lives), font=style)
l.penup()


#falling eggs
eggs= turtle.Turtle()
eggs.speed(0)
eggs.shape('circle')
eggs.color('burlywood')
eggs.shapesize(outline=7)
eggs.penup()
eggs.goto(0,300)
eggs1= turtle.Turtle()
eggs1.speed(0)
eggs1.shape('circle')
eggs1.shapesize(outline=7)
eggs1.color('sienna')
eggs1.penup()
eggs1.goto(-140,255)
eggs2= turtle.Turtle()
eggs2.speed(0)
eggs2.shape('circle')
eggs2.color('sienna')
eggs2.shapesize(outline=7)
eggs2.penup()
eggs2.goto(180,245)
stop=turtle.Turtle()

def go_left():
    basket.direction='left'
def go_right():
    basket.direction='right'
#keyboard binding
game.listen()
game.onkeypress(go_left,'Left')#keyboard keys
game.onkeypress(go_right,'Right')

#main game loop
while lives>0:
    #move basket
    x=basket.xcor()
    if basket.direction=='left':
        x-=20
        basket.setx(x)
    elif x>650:
        basket.direction=('stop')    
    if basket.direction=='right':
        x+=20
        basket.setx(x)
    elif x<-650:
        basket.direction=('stop')
    
    
    #falling eggs
    y= eggs.ycor()
    y-=7
    eggs.sety(y)
    #check if off the screen
    if y<-300:
        x= random.randint(-650,650)
        y= random.randint(300,400)
        eggs.goto(x,y)
    # check for the collision with basket
    if eggs.distance(basket) < 30:
        x= random.randint(-650,650)
        y= random.randint(300,400)
        eggs.goto(x,y)
        lives+=1
    if (eggs1.distance(basket) < 30):
        x= random.randint(-650,650)
        y= random.randint(300,400)
        eggs1.goto(x,y)
        lives-=1
        
    if (eggs2.distance(basket) < 30):
        x= random.randint(-650,650)
        y= random.randint(300,400)
        eggs2.goto(x,y)
        lives-=1
    
        
    
    #falling eggs1
    y= eggs1.ycor()
    y-=7
    eggs1.sety(y)
    #check if off the screen
    if y<-300:
        x= random.randint(-650,650)
        y= random.randint(300,400)
        eggs1.goto(x,y)
    #falling eggs2
    y= eggs2.ycor()
    y-=7
    eggs2.sety(y)
    #check if off the screen
    if y<-300:
        x= random.randint(-650,650)
        y= random.randint(300,400)
        eggs2.goto(x,y)

   #printing lives
    style= ('Courier', 24, 'bold')
    l.goto(250,300)
    l.clear()
    l.write('Lives:{}'.format(lives), font=style)
    l.penup()

    if lives==15:
        style=('Algerian', 64, 'bold')
        turtle.hideturtle()
        stop.color('red')
        stop.penup()
        stop.goto(-250,-300)
        stop.write('!!!YOU WON!!!', font=style)
        break
else:
    style= ('Casteller', 54, 'bold')
    turtle.hideturtle()
    stop.color('blue')
    stop.penup()
    stop.goto(-400,-300)
    stop.write('YOU ARE OUT OF LIVES \n        GAME OVER', font=style)
game.mainloop()
