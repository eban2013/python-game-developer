import pgzrun
import random
WIDTH =500
HEIGHT = 500

def draw():
    s=500
    screen.fill('black')
    for i in range (50):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)

        rec=Rect(0,0,s,s)
        rec.center=WIDTH/2,HEIGHT/2
        screen.draw.rect(rec,(r,g,b))
        s=s-10
        
pgzrun.go()



