import turtle

turtle.left(90)
count = 5
while (count >= 0):
    turtle.penup()
    turtle.goto(count * 100, 0)
    turtle.pendown()
    turtle.forward(500)
    count -= 1

turtle.right(90)
count = 5
while (count >= 0):
    turtle.penup()
    turtle.goto(0, count * 100)
    turtle.pendown()
    turtle.forward(500)
    count -= 1

turtle.exitonclick()

    
