def draw_circle(x,y,color,rad):
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()

import turtle
t = turtle.Turtle()
t.pensize(2)
t.up()
draw_circle(0,-50,"green",50)
draw_circle(0,300,"green",25)
draw_circle(200,200,"orange",50)
draw_circle(0,-300,"orange",25)
draw_circle(-200,200,"blue",50)
draw_circle(300,0,"blue",25)
draw_circle(-200,-200,"red",-50)
draw_circle(-300,0,"red",25)
draw_circle(200,-200,"yellow",-50)








