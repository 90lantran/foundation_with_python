import turtle

def init():
    window = turtle.Screen()
    window.bgcolor("blue")

def draw_square():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.speed(2)
    for i in range(0,4):
        angie.forward(100)
        angie.right(90)
    
 

def draw_circle():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(2)
    brad.stamp()
    brad.circle(50)

def draw_rectangle():
    t = turtle.Turtle()
    t.speed(1)
    t.color("red")
    for i in range(0,3):
        t.forward(200)
        t.left(120)

def draw_art_cirle():
    art_turtle = turtle.Turtle()
    art_turtle.speed(2)
    art_turtle.shape("turtle")
    art_turtle.color("yellow")
    angle = -90
    for i in range(0,360,10):
        art_turtle.setheading(angle - i);
        for i in range(0,4):
            art_turtle.forward(100)
            art_turtle.right(90)
    
def draw_art_flower():
    art_turtle = turtle.Turtle()
    art_turtle.speed(2)
    art_turtle.shape("turtle")
    art_turtle.color("yellow")
    angle = -60
    for i in range(0,360,25):
        art_turtle.setheading(angle - i);
        art_turtle.forward(80)
        art_turtle.right(60)
        art_turtle.forward(80)
        art_turtle.right(120)
        art_turtle.forward(80)
        art_turtle.right(60)
        art_turtle.forward(80)
        
    
    
#draw_square()
#draw_circle()
#draw_rectangle()
init()    
#draw_art_cirle()
draw_art_flower()

