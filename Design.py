def design(t,dist,sides):
    angle = 360/sides
    for times in range(sides):
        t.forward(dist)
        t.left(angle)
        
def planet(t,size,angle):
    t.begin_fill()
    t.circle(size,angle)
    t.end_fill()

def outline(t,size,angle):
    t.color(255,255,255)
    t.circle(size,angle)

def star(t,size,angle):
    t.color(255,255,255)
    t.begin_fill()
    t.circle(size,angle)
    t.end_fill()


    
                
'''

bob.penup()
bob.goto(470,356) #star
bob.pendown()
star(bob,2,360)

bob.penup()
bob.goto(645,356) #star
bob.pendown()
star(bob,2,360)

bob.penup()
bob.goto(369,213) #star
bob.pendown()
star(bob,2,360)

bob.penup()
bob.goto(621,456) #star
bob.pendown()
star(bob,2,360)

bob.penup()
bob.goto(145,-565) #star
bob.pendown()
star(bob,2,360)


bob.penup()
bob.goto(-369,254) #star
bob.pendown()
star(bob,2,360)

bob.penup()
bob.goto(300,-345) #star
bob.pendown()
star(bob,2,360)

bob.penup()
bob.goto(-300,376) #star
bob.pendown()
star(bob,2,360)

bob.penup()
bob.goto(-426,216) #star
bob.pendown()
star(bob,2,360)

bob.penup()
bob.goto(-489,379) #star
bob.pendown()
star(bob,2,360)

bob.penup()
bob.goto(-489,210) #star
bob.pendown()
star(bob,2,360)
bob.penup()

'''
