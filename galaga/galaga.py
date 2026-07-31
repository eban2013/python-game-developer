import pgzrun

HEIGHT=600
WIDTH=800

galaga=Actor('galaga')
galaga.pos=(WIDTH/2,HEIGHT-50)
bullets=[]


def draw ():
    screen.blit('space',(0,0))
    galaga.draw()


def update():
    if keyboard.a :
        galaga.x=galaga.x-3

    if keyboard.d :
        galaga.x=galaga.x+3
    
def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor('bullet')
        bullets.append(bullet)

    print(bullets)


pgzrun.go()