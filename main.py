import turtle as tortue

tortue.ht()
tortue.degrees(fullcircle=360.0)
tortue.speed(0)
tortue.tracer(0,0)
tortue.mode("standard")

def action() :
    tortue.up()
    tortue.goto(0,0)
    tortue.seth(0)
    tortue.forward(250)
    tortue.left(90)
    tortue.down()
    tortue.circle(250)
    tortue.up()
    tortue.left(90)
    tortue.forward(250)
    tortue.right(90)
    nbpoints = 0.1
    while not nbpoints == int(nbpoints) :
        nbpoints = int(input("Nombre de points : "))
    nbpoints = abs(nbpoints)
    liste_points = []
    for i in range (nbpoints) :
        tortue.forward(250)
        liste_points += [tortue.xcor(),tortue.ycor()]
        tortue.backward(250)
        tortue.right(360/nbpoints)

    table = 0.1
    while not table == int(table) :
        table = int(input("Table de : "))
    table = abs(table)
    tortue.goto(liste_points[2],liste_points[3])
    for i in range (1,nbpoints,1) :
        tortue.down()
        tortue.goto(liste_points[((i*table)%nbpoints)*2],liste_points[((i*table)%nbpoints)*2+1])
        tortue.up()
        if i <= nbpoints-2 :
            tortue.goto(liste_points[i*2+2],liste_points[i*2+3])
        elif i == nbpoints-1 :
            tortue.goto(liste_points[0],liste_points[1])

action()
b = 1
while b == 1 :
    a = 3
    while not a == 1 and not a == 2 :
        a = int(input("1) Recommencer avec d'autres valeurs 2) Quitter "))
    if a == 1 :
        print()
        tortue.clear()
        action()
    else :
        b = 0

tortue.bye()