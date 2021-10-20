import turtle

win = turtle.Screen()
win.bgcolor("light blue")
win.title("Turtle Inisial Rihan Hidayat")
win.setup(width=600, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.pensize(5)

#Lingkaran
t.penup()
t.goto(0,-250)
t.pendown()
t.circle(250)

#R
t.penup()
t.goto(-90,60)
t.pendown()
t.goto(-90,-60)
t.penup()
t.goto(-90,60)
t.pendown()
t.circle(-30,180)
t.goto(-60,-60)

#H
t.penup()
t.goto(30,60)
t.pendown()
t.goto(30,-60)
t.penup()
t.goto(30,0)
t.pendown()
t.goto(100,0)
t.penup()
t.goto(100,60)
t.pendown()
t.goto(100,-60)

turtle.mainloop()