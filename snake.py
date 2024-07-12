import turtle
import random


#initializing the window
window = turtle.Screen()
window.tracer(0)
window.setup(1000, 1000)
window.bgcolor(0, 0, 0)
window.title("Snake")
instance = 0

#borders
left = -window.window_width() / 2
right = window.window_width() / 2
top = window.window_height() / 2
bottom = -window.window_height() / 2
gutter = window.window_width() * 0.025


#initilizing the snake
snake = turtle.Turtle()
snake.penup()
snake.color(1, 1, 1)
snake.shape("square")
snake.turtlesize(1, 1)
snakeposx = 10
snakeposy = 10
snakespeed = 20
snake.setposition(snakeposx, snakeposy)
score = 0
snakebody = []




#initializing the grid
pen = turtle.Turtle()
pen.shape("square")
pen.color(1, 1, 1) #makes square black and smaller than 1 so that an outline can be made
pen.penup()
pen.turtlesize(1.1, 1.1)
pen.setposition(left + gutter + 5, bottom + gutter + 5)
pen.turtlesize(0.9, 0.9)
pen.fillcolor(0, 0, 0)
print(pen.xcor(), pen.ycor())


#create the grid
for i in range(int(left), int(right), 20):
   if pen.xcor() < right - gutter-10:
       pen.stamp()
       pen.setposition(i + gutter + 5, bottom + gutter + 5)
       for j in range(0, ((int(top) - 15) * 2), 20):
           if pen.ycor() < top - gutter - 10:
               pen.stamp()
               pen.sety(bottom + gutter + 5 + j)
pen.stamp()
pen.hideturtle()
pen.penup()


#creating the apple
apple = turtle.Turtle()
apple.shape("square")
apple.penup()
apple.setposition(left + gutter + 5, bottom + gutter + 5)
apple.turtlesize(0.9, 0.9)
apple.fillcolor(1, 0, 0)
print(apple.xcor(), apple.ycor())


#random
def generaterandpos():
   x = random.choice(range(int(left + gutter + 5), int(right - gutter - 5), 20))
   y = random.choice(range(int(bottom + gutter + 5), int(top - gutter - 5), 20))
   return x, y


#random apple generation
random.seed()
randompos = generaterandpos()
apple.setposition(randompos[0], randompos[1])
print(apple.xcor(), apple.ycor())


#delete sprite
def remove_sprite(sprite):
   sprite.clear()
   sprite.hideturtle()
   window.update()


#add segment
def addsegment():
   segment = turtle.Turtle()
   segment.penup()
   segment.color("gray")
   segment.shape("square")
   segment.turtlesize(1, 1)
   segment.hideturtle()
   snakebody.append(segment)
   segment.setposition(10, 10)


def collision():
   #checks for snake hitting its own body
   headposition = snakebody[0].position()
   #an attempt to optimize collision recog
   if (headposition[0] <= int(left + gutter + 15) or headposition[0] <= int(right - gutter - 15) or headposition[1] <= int(top - gutter - 15) or headposition[1] <= int(bottom + gutter + 15)):
       # logic for hitting borders
       if ((headposition[0] == int(left + gutter + 5)) and currentdir == "Left"):
           snake.setx(int(right - gutter - 5))
       elif ((headposition[0] == int(right - gutter - 5)) and currentdir == "Right"):
           snake.setx(int(left + gutter + 5))
       elif ((headposition[1] == int(top - gutter - 5)) and currentdir == "Up"):
           snake.sety(int(bottom + gutter + 5))
       elif ((headposition[1] == int(bottom + gutter + 5)) and currentdir == "Down"):
           snake.sety(int(top - gutter - 5))
   for segment in snakebody[1:]:
       if segment.distance(headposition) < 1:
           return True
   return False


#creating the initial snake body
def draw_snake():
   snake.clear()
   updatesnakebody()
   window.update()


#update snake body length
def updatesnakebody():
   for index in range(len(snakebody) - 1, 0, -1):
       x = snakebody[index - 1].xcor()
       y = snakebody[index - 1].ycor()
       snakebody[index].setposition(x, y)
       snakebody[index].showturtle()
   if snakebody:  # Ensure snakebody is not empty
       snakebody[0].setposition(snake.xcor(), snake.ycor())
       # Show the first segment if snakebody has more than one segment
       if len(snakebody) > 1:
           snakebody[0].showturtle()
       else:
           snakebody[0].color("white")


def resetgame():
   global score
   score = 0
   snake.setposition(snakeposx, snakeposy)
   for segment in snakebody:
       segment.hideturtle()
   snakebody.clear()
   remove_sprite(apple)
   apple.setposition(randompos[0], randompos[1])
   apple.showturtle()
   addsegment()
   gameloop()




currentdir = "Up"
futuredir = ""
#movement
def leftdir():
   global futuredir
   futuredir = "Left"


def rightdir():
   global futuredir
   futuredir = "Right"


def updir():
   global futuredir
   futuredir = "Up"


def downdir():
   global futuredir
   futuredir = "Down"






def movesnake():
   #check for illegal movements
   global currentdir
   global futuredir
   if futuredir:
       if (currentdir == "Up" and futuredir != "Down") or (currentdir == "Down" and futuredir != "Up") or (currentdir == "Left" and futuredir != "Right") or (currentdir == "Right" and futuredir != "Left"):
           currentdir = futuredir
       futuredir = ""
   #update the movement
   if currentdir == "Left":
       new_x = snake.xcor() - snakespeed
       if new_x >= left + gutter:
           snake.setx(new_x)
           draw_snake()
   elif currentdir == "Right":
       new_x = snake.xcor() + snakespeed
       if new_x <= right - gutter:
           snake.setx(new_x)
           draw_snake()
   elif currentdir == "Up":
       new_y = snake.ycor() + snakespeed
       if new_y <= top - gutter:
           snake.sety(new_y)
           draw_snake()
   elif currentdir == "Down":
       new_y = snake.ycor() - snakespeed
       if new_y >= bottom + gutter:
           snake.sety(new_y)
           draw_snake()
   window.ontimer(movesnake, 100)


# key bindings for direction changes
window.onkeypress(leftdir, "Left")
window.onkeypress(rightdir, "Right")
window.onkeypress(updir, "Up")
window.onkeypress(downdir, "Down")
window.listen()




draw_snake()


# Game loop
def gameloop():
   global instance
   if instance == 0:
       movesnake()
       instance = 1
   while True:
       window.update()
       if collision():
           print("Game Over")
           resetgame()
       #apple score update & grow tail
       if snake.distance(apple) < 20:
           remove_sprite(apple)
           global score
           score += 1
           print("Your score: " + str(score))
           display = ">:"
           for i in range(len(snakebody)):
               display += "-"
           print("Snake: " + "\n" + display)
           randompos = generaterandpos()
           apple.setposition(randompos[0], randompos[1])
           apple.showturtle()
           addsegment()


addsegment()
gameloop()


turtle.done()

