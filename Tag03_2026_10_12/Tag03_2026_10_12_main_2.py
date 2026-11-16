import turtle

# Fenster und Schildkröte einrichten
t = turtle.Turtle()

t.left(90)

i = 1
while i <= 3:
    t.forward(100)
    t.right(90)
    i = i + 1

i = 1
while i <= 2:
    t.forward(90)
    t.right(90)
    i = i + 1



t.forward(80)
t.right(90)

turtle.done()