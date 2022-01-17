import turtle as tr
import random


tr.hideturtle()
tr.speed(50)
tr.penup()
tr.goto(210, -210)
tr.pendown()
tr.goto(210, 210)
tr.goto(-210, 210)
tr.goto(-210, -210)
tr.goto(210, -210)

number_of_molecules = 10

vessel = [tr.Turtle(shape='circle') for i in range(number_of_molecules)]

for molecule in vessel:
    molecule.shapesize(0.7, 0.7, 1)
    molecule.color('blue')
    molecule.penup()
    molecule.speed(100)
    molecule.seth(random.randint(0, 360))
    molecule.goto(random.randint(-200, 200), random.randint(-200, 200))

for i in range(500):
    for g in range(len(vessel)):
        x1, y1 = vessel[g].pos()
        angle1 = vessel[g].heading()
        for h in range(len(vessel)):
            if g != h:
                x2, y2 = vessel[h].pos()
                angle2 = vessel[h].heading()
                dx = abs(x1 - x2)
                dy = abs(y1 - y2)
                if dx <= 20 and dy <= 20:
                    vessel[h].seth(-angle2)
                    vessel[g].seth(-angle1)
                    vessel[h].fd(5)
                    vessel[g].fd(5)

        if x1 < -200 or x1 > 200:
            vessel[g].seth(180 - angle1)
        elif y1 < -200 or y1 > 200:
            vessel[g].seth(-angle1)
        vessel[g].fd(5)


tr.exitonclick()
