
import turtle

def sq(a):
     for i in range(4):
         joe.color(colors[i%4])
         joe.forward(a)
         joe.left(90)

colors =['red','brown','green','blue']


joe= turtle.Turtle()
joe.speed(100)

dlina= 30
for i in range (36):
    sq(dlina)
    joe.right(10)
    dlina=dlina+4