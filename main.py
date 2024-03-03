import turtle
import random


board = turtle.Screen()
board.bgcolor("mediumpurple")
board.title("Catch the Turtle Game")

FONT = ("arial",19,"normal")
grid_size = 10
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, -10, 0, 10, 20]
gameOver = False
score = 0

#explain the game
game_explain = turtle.Turtle()
game_explain.hideturtle()

#start button
start_button = turtle.Turtle()
start_button.hideturtle()

#score turtle created
score_instance = turtle.Turtle()
score_instance.hideturtle()

#turtle_instance created
turtle_instance = turtle.Turtle()
turtle_instance.hideturtle()

#countdown instance created
countdown_instance = turtle.Turtle()
countdown_instance.hideturtle()

#creat bad turtle
badTurtle= turtle.Turtle()
badTurtle.hideturtle()

board.tracer(0)

def explainingGame():
    top_height = board.window_height() / 2
    y = top_height * 0.7
    game_explain.color("darkorange")
    game_explain.penup()
    game_explain.hideturtle()
    game_explain.clear()
    game_explain.setposition(-200, y)
    game_explain.write(arg="Wellcome to Catch the Turtle Game.", font=("Arial",15))
    game_explain.goto(-200,y-30)
    game_explain.write(arg="You should catch the green turtle in 30seconds.",font=("Arial",15))
    game_explain.goto(-200,y-60)
    game_explain.write(arg="If you click red turtle, you lost.", font=("Arial",15))
    game_explain.setposition(-200, y-90)
    game_explain.write(arg= "Please click on the button allow and start", font=("Arial",15))

explainingGame()

def button_start():

    for i in range(2):
        start_button.forward(75)
        start_button.left(90)
        start_button.forward(60)
        start_button.left(90)
        start_button.forward(75)

    start_button.hideturtle()
    start_button.penup()
    start_button.goto(-60,20)
    start_button.write(arg="Start Game",font=FONT)

button_start()
board.tracer(1)
def click_start(x,y):
    if -75 < x < 75 and 0 < y < 60:
        game()

def setup_turtles():
    turtle_instance.shape("turtle")
    turtle_instance.color("green")
    turtle_instance.turtlesize(1.2,1.2)
    turtle_instance.penup()

    if not gameOver:
        turtle_instance.hideturtle()
        turtle_instance.goto(random.choice(x_coordinates) * grid_size, random.choice(y_coordinates)*grid_size)
        board.ontimer(setup_turtles,700)
        turtle_instance.showturtle()
        turtle_instance.speed(3)

def setup_score_turtle():
    top_height = board.window_height() /2
    y = top_height * 0.9
    score_instance.color("yellow")
    score_instance.penup()
    score_instance.hideturtle()
    score_instance.setposition(0,y) #önce konum ayarlanır sonra yazı yoksa yazı hareket etmez
    score_instance.clear()
    score_instance.write(arg="Score: 0", align="center", font=FONT)

def make_badturtles():
    badTurtle.shape("turtle")
    badTurtle.color("red")
    badTurtle.turtlesize(1.2,1.2)
    badTurtle.penup()
    if not gameOver:
        badTurtle.hideturtle()
        badTurtle.goto(random.choice(x_coordinates) * grid_size, random.choice(y_coordinates)*grid_size)
        board.ontimer(make_badturtles,1500)
        badTurtle.showturtle()
        badTurtle.speed(10)

def countdown(time):
    global gameOver
    if not gameOver:
        top_height = board.window_height() / 2
        y = top_height * 0.8
        countdown_instance.color("red")
        countdown_instance.penup()
        countdown_instance.hideturtle()
        countdown_instance.setposition(0, y)  # önce konum ayarlanır sonra yazı yoksa yazı hareket etmez
        if time>0:
            countdown_instance.clear()
            countdown_instance.write(arg=f"Time: {time} ", align="center", font=FONT)
            board.ontimer(lambda: countdown(time-1),1000)

        else:
            gameOver = True
            turtle_instance.hideturtle()
            badTurtle.hideturtle()
            countdown_instance.clear()
            countdown_instance.write(arg="Game Over!", align="center",font=FONT )

def catch_turtle(x,y):
    global score
    global gameOver
    distance = turtle_instance.distance(x,y)
    distance2 = badTurtle.distance(x,y)
    if distance < 20:
        score += 1
        score_instance.clear()
        score_instance.write(arg=f"Score {score} ",align="center", font=FONT)
    if distance2 >20 :
        gameOver = False
    else:
        gameOver = True
        turtle_instance.hideturtle()
        badTurtle.hideturtle()
        countdown_instance.clear()
        countdown_instance.write(arg="Game Over!", align="center", font=FONT)

def game():
    board.tracer(0)
    game_explain.clear()
    start_button.clear()
    setup_score_turtle()
    setup_turtles()
    countdown(30)
    make_badturtles()
    board.onclick(catch_turtle)
    board.tracer(1)

board.onclick(click_start)

turtle.mainloop()