import turtle


def w_move():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def a_move():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def s_move():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)

def d_move():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(w_move, 'w')
turtle.onkey(a_move, 'a')
turtle.onkey(s_move, 's')
turtle.onkey(d_move, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
