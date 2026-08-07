import pgzrun

HEIGHT=600
WIDTH=800

galaga=Actor('galaga')
galaga.pos=(WIDTH/2,HEIGHT-50)
bullets=[]



enemies=[]
y=50
for i in range (3):
    row=[]
    x=50
    for q in range(4):
        enemy=Actor('enemy')
        enemy.x=x
        enemy.y=y
        row.append(enemy)
        x=x+60
    enemies.append(row)
    y=y+60

def draw ():
    screen.blit('space',(0,0))
    galaga.draw()

    for bullet in bullets:
        bullet.draw()

    for row in enemies:
        for enemy in row :
            enemy.draw()


def update():
    if keyboard.a :
        galaga.x=galaga.x-3

    if keyboard.d :
        galaga.x=galaga.x+3

    for bullet in bullets:
        bullet.y=bullet.y-5
        if bullet.y<0:
            bullets.remove(bullet)

    for i in range (3):
        for enemy in enemies[i]:
            for bullet in bullets:
                if enemy.colliderect(bullet):
                    enemies[i].remove(enemy)
                    bullets.remove(bullet)



def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor('bullet')
        bullet.pos=galaga.pos
        bullets.append(bullet)

    print(bullets)


pgzrun.go()