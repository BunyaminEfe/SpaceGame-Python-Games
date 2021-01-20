##########################################
#
# 
# Contact: 
# https://www.instagram.com/bejo_app/
#
# İletişim:
# https://www.instagram.com/bejo_app/
#
##########################################

import turtle
import math
import random
from tkinter import *

window = turtle.Screen()
window.setup(width=750, height=750)
window.title("Python Basit Uzay Oyunu")
window.bgcolor("black")
window.tracer(0)
vertex = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0) , (18,-5),(18, 5),(15, 0))
window.register_shape("oyuncu", vertex)
asVertex = ((0, 10), (5, 7), (3,3), (10,0), (7, 4), (8, -6), (0, -10), (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
window.register_shape("chattan", asVertex)


class Bejo(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.speed(0)
        self.penup()

def Bejo1(t1, t2):
    x1 = t1.xcor()
    y1 = t1.ycor()
    x2 = t2.xcor()
    y2 = t2.ycor()
    karakter = math.atan2(y1 - y2, x1 - x2)
    karakter = karakter * 180.0 / 3.14159
    return karakter

oyuncu = Bejo()
oyuncu.color("yellow")
oyuncu.shape("oyuncu")
oyuncu.puan = 0
missiles = []

for _ in range(3):
    missile = Bejo()
    missile.color("green")
    missile.shape("circle")
    missile.speed = 2
    missile.state = "hazır"
    missile.hideturtle()
    missiles.append(missile)

pen = Bejo()
pen.color("white")
pen.hideturtle()
pen.goto(0, -250)
pen.write("Ateş Etmek İçin Boşluk Sağ Sol İçin Yön tuşları", align = "center", font = ("Arial", 24, "normal"))
pen.goto(0, 250)
pen.write("Puan: 0", False, align = "center", font = ("Arial", 24, "normal"))


chattans = []
for _ in range(5):   
    chattan = Bejo()
    chattan.color("brown")
    chattan.shape("arrow")
    chattan.speed  = random.randint(2, 3)/50
    chattan.goto(0, 0)
    karakter = random.randint(0, 260)
    distance = random.randint(300, 400)
    chattan.setheading(karakter)
    chattan.fd(distance)
    chattan.setheading(Bejo1(oyuncu, chattan))
    chattans.append(chattan)

def sol():
    oyuncu.lt(20)
    
def sag():
    oyuncu.rt(20)
    
def ates_et():
    for missile in missiles:
        if missile.state == "hazır":
            missile.goto(0, 0)
            missile.showturtle()
            missile.setheading(oyuncu.heading())
            missile.state = "ates"
            break

window.listen()
window.onkey(sol, "Left")
window.onkey(sag, "Right")
window.onkey(ates_et, "space")

sakkyo = False
while True:
    window.update()
    oyuncu.goto(0, 0)

    for missile in missiles:
        if missile.state == "ates":
            missile.fd(missile.speed)

        if missile.xcor() > 300 or missile.xcor() < -300 or missile.ycor() > 300 or missile.ycor() < -300:
            missile.hideturtle()
            missile.state = "hazır"

    for chattan in chattans:    
        chattan.fd(chattan.speed)
        for missile in missiles:
            if chattan.distance(missile) < 20:
                karakter = random.randint(0, 260)
                distance = random.randint(600, 800)
                chattan.setheading(karakter)
                chattan.fd(distance)
                chattan.setheading(Bejo1(oyuncu, chattan))
                chattan.speed += 0.01
                missile.goto(600, 600)
                missile.hideturtle()
                missile.state = "hazır"
                oyuncu.puan += 10
                pen.clear()
                pen.write("puan: {}".format(oyuncu.puan), False, align = "center", font = ("Arial", 24, "normal"))

        if chattan.distance(oyuncu) < 20:
            karakter = random.randint(0, 260)
            distance = random.randint(600, 800)
            chattan.setheading(karakter)
            chattan.fd(distance)
            chattan.setheading(Bejo1(oyuncu, chattan))
            chattan.speed += 0.005
            sakkyo = True
            oyuncu.puan -= 30
            pen.clear()
            pen.write("Puan: {}".format(oyuncu.puan), False, align = "center", font = ("Arial", 24, "normal"))

    if sakkyo == True:
        oyuncu.hideturtle()
        missiles.hideturtle()
        for a in chattans:
            a.hideturtle()
        pen.clear()
        break

window.mainloop()
