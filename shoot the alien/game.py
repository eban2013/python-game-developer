import pgzrun
import random

WIDTH=500
HEIGHT=500
TITLE="shoot the alien"
bob=Actor("bob")
bob.x=random.randint(50,WIDTH-50)
bob.y=random.randint(50,HEIGHT-50)
message="hello"
def draw():
    screen.fill('red')
    bob.draw()
    screen.draw.text(message,center=(WIDTH/2,30),fontsize=70,color='black')

def on_mouse_down(pos):
    print(pos)
    global message
    if bob.collidepoint(pos):
        message="WELL DONE!"
        bob.x=random.randint(50,WIDTH-50)
        bob.y=random.randint(50,HEIGHT-50)
    else:
        message="you missed"


pgzrun.go()