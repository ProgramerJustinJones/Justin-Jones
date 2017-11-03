import turtle
from random import *
from Design import *
turtle.colormode(255)
turtle.bgcolor("black")

bob = turtle.Turtle()
turtle.tracer(0)
bob.speed(0)




for times in range(100):
    x = randint(-800,800)
    y = randint(-800,800)
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    star(bob,2,360)


cj = 150 #a color jump
g = 0 #gradient
bob.penup()                 #All this code is the first planet
bob.color(0,119,190)
bob.goto(-600,-1000)
bob.pendown()
bob.begin_fill()
bob.circle(500,360)
bob.end_fill()
bob.penup()
bob.goto(-600,-1000)
bob.color(255,255,255)
bob.pendown()
bob.width(5)
bob.circle(500,360)

                 
bob.color(51,51,255)
bob.begin_fill()
bob.circle(450,360)
bob.end_fill()
bob.width(5)
bob.circle(450,360)

bob.color(0,0,255)
bob.begin_fill()
bob.circle(400,360)
bob.end_fill()
bob.width(5)
bob.circle(400,360)

bob.color(0,119,190)
bob.begin_fill()
bob.circle(350,360)
bob.end_fill()
bob.width(5)
bob.circle(350,360)

bob.penup()                 #Planet
bob.goto(200,200)
bob.pendown()
planet(bob,100,360)
bob.penup()
bob.goto(200,200)
bob.pendown()
outline(bob,100,360)
bob.color(51,51,255)
planet(bob,85,360)
bob.color(0,0,255)
planet(bob,70,360)

bob.penup()                 #sun
bob.goto(-700,200)
bob.pendown()
bob.color(240,0,0)
planet(bob,400,360)
outline(bob,400,360)
bob.color(255,69,0)                      
planet(bob,350,360)
bob.color(255,128,0)
planet(bob,300,360)
bob.color(240,128,0)
planet(bob,250,360)






bob.color(0,119,190)
bob.penup()                 #Planet
bob.goto(500,-500)
bob.pendown()
planet(bob,175,360)
bob.penup()
bob.goto(500,-500)
bob.pendown()
outline(bob,175,360)
bob.color(51,51,255)
planet(bob,175-15,360)
bob.color(0,0,255)
planet(bob,175-30,360)
bob.color(0,0,153)
planet(bob,175-45,360)




bob.penup()
bob.goto(200,200)
bob.pendown()


bob.width(0)
for times in range(18):
    bob.begin_fill()
    bob.color(times*g+cj,0,0) #The color red
    design(bob,50,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(times*g+cj,0,0) #The color red
    design(bob,60,4)
    bob.left(20)



bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(255,69,0) #The color orange
    design(bob,25,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(255,69,0) #The color orange
    design(bob,35,4)
    bob.left(20)

bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(255,128,0) #The color yellow
    design(bob,10,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(255,128,0) #The color yellow
    design(bob,20,4)
    bob.left(20)









"""
DIFFERENT CIRCLE
"""


bob.goto(100,100)



"""
DIFFERENT CIRCLE
"""


bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(times*g+cj,0,0) #The color red
    design(bob,75,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(times*g+cj,0,0) #The color red
    design(bob,85,4)
    bob.left(20)



bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(255,69,0) #The color orange
    design(bob,50,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(255,69,0) #The color orange
    design(bob,60,4)
    bob.left(20)

bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(255,128,0) #The color yellow
    design(bob,25,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(255,128,0) #The color yellow
    design(bob,35,4)
    bob.left(20)
    
    
    
    
'''
DIFFERENT CIRCLE
'''
    
    


    

bob.goto(0,0) # Starting the secound circle




'''
DIFFERENT CIRCLE
'''

bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(times*g+cj,0,0) #The color red
    design(bob,100,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(times*g+cj,0,0) #The color red
    design(bob,110,4)
    bob.left(20)



bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(255,69,0) #The color orange
    design(bob,75,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(255,69,0) #The color orange
    design(bob,85,4)
    bob.left(20)

bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(255,128,0) #The color yellow
    design(bob,50,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(255,128,0) #The color yellow
    design(bob,60,4)
    bob.left(20)


    
"""
DIFFERENT CRICLE
"""

bob.goto(-100,-100)

"""
DIFFERENT CIRCLE
"""



bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(times*g+cj,0,0) #The color red
    design(bob,125,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(times*g+cj,0,0) #The color red
    design(bob,135,4)
    bob.left(20)



bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(255,69,0) #The color orange
    design(bob,100,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(255,69,0) #The color orange
    design(bob,110,4)
    bob.left(20)

bob.width(0)

for times in range(18):
    bob.begin_fill()
    bob.color(255,128,0) #The color yellow
    design(bob,75,4)
    bob.left(20)
    bob.end_fill()

bob.width(3)

for times in range(18):
    bob.color(255,128,0) #The color yellow
    design(bob,85,4)
    bob.left(20)








    



