# bitte eine python turtle die ein n * m gitter zeichnet

# https://projecteuler.net/

import turtle


def zeichne_gitter(n, m, seitenlaenge=30):
    """Zechnet ein Gitter mit n Zeilen und m Spalten."""
    t = turtle.Turtle()
    t.speed(100)  # Schnellste Zeichengeschwindigkeit

    # Berechne Startposition, um das Gitter grob zu zentrieren
    start_x = -(m * seitenlaenge) / 2
    start_y = (n * seitenlaenge) / 2

    # Horizontale Linien zeichnen
    for i in range(n + 1):
        t.penup()
        t.goto(start_x, start_y - i * seitenlaenge)
        t.pendown()
        t.forward(m * seitenlaenge)

    # Vertikale Linien zeichnen
    t.right(90)  # Drehung nach unten für die vertikalen Linien
    for j in range(m + 1):
        t.penup()
        t.goto(start_x + j * seitenlaenge, start_y)
        t.pendown()
        t.forward(n * seitenlaenge)

    t.hideturtle()


# Fenster einrichten
screen = turtle.Screen()
screen.title("N * M Gitter")

# Beispiel: 5 Zeilen (n) und 8 Spalten (m)
zeichne_gitter(n=2, m=2, seitenlaenge=40)

# Hält das Fenster offen
screen.mainloop()