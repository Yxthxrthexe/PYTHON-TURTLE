import turtle

indian_flag = turtle.Turtle()

turtle.bgcolor("black")
indian_flag.penup()
indian_flag.goto(-350, 150)
indian_flag.pendown()

indian_flag.color("#FF9933")
indian_flag.begin_fill()
indian_flag.forward(700)
indian_flag.right(90)
indian_flag.forward(100)
indian_flag.right(90)
indian_flag.forward(700)
indian_flag.end_fill()

indian_flag.penup()
indian_flag.left(180)
indian_flag.goto(-350, 50)
indian_flag.pendown()

indian_flag.color("white")
indian_flag.begin_fill()
indian_flag.forward(700)
indian_flag.right(90)
indian_flag.forward(100)
indian_flag.right(90)
indian_flag.forward(700)
indian_flag.end_fill()

indian_flag.penup()
indian_flag.left(180)
indian_flag.goto(-350, -50)
indian_flag.pendown()

indian_flag.color("#138808")
indian_flag.begin_fill()
indian_flag.forward(700)
indian_flag.right(90)
indian_flag.forward(100)
indian_flag.right(90)
indian_flag.forward(700)
indian_flag.end_fill()

indian_flag.penup()
indian_flag.goto(0, 50)
indian_flag.pendown()

indian_flag.pencolor("blue")

indian_flag.circle(50)

indian_flag.penup()
indian_flag.goto(0, 0)
indian_flag.pendown()
for i in range(0, 36):
    indian_flag.penup()
    indian_flag.goto(0, 0)
    indian_flag.pendown()
    indian_flag.left(10)
    indian_flag.forward(50)

indian_flag.pencolor("orange")
indian_flag.penup()
indian_flag.goto(140, -13)
indian_flag.left(180)
indian_flag.pendown()
indian_flag.write("Jai Shree Ram", font=("Calibri", 26, "normal"))
turtle.done()
