import turtle

# Fenster und Schildkröte einrichten
t = turtle.Turtle()
'''
#t.forward(100)
t.left(90)

#t.forward(100)
t.left(90)

#t.forward(100)
t.left(90)

#t.forward(100)
t.left(90)
'''
#kreis

t.forward(10)
t.left(5)

t.forward(10)
t.left(5)

t.forward(10)
t.left(5)

i = 1
while i < 360//5:
    t.forward(10)
    t.left(5)
    i += 1


turtle.done()