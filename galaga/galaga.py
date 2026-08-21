import pgzrun

HEIGHT=600
WIDTH=800

galaga=Actor('galaga')
galaga.pos=(WIDTH/2,HEIGHT-50)
bullets=[]

direction=1
gameover=False
gom=" "

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
    if not gameover:
        galaga.draw()

        for bullet in bullets:
            bullet.draw()

        for row in enemies:
            for enemy in row :
                enemy.draw()
    else:
        screen.draw.text(gom,(0,0))



def update():
    global direction,gom,gameover

    movedown=False

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
                    sounds.eep.play()

    if any(enemies):
        if enemies[0][-1].x>=WIDTH or enemies[0][0].x <= 0 :
           direction=direction*-1 
           movedown=True

        for i in range (3):
            for enemy in enemies[i]:
                for bullet in bullets:
                    if enemy.colliderect(bullet):
                        enemies[i].remove(enemy)
                        bullets.remove(bullet)
                        sounds.eep.play()
    





    else:
        gameover=True
        gom="you won the game well done" 
    
        
    for row in enemies:
        for enemy in row:
            if enemy.colliderect(galaga):
                gameover=True
                gom="you lost try again "

    

    
    for row in enemies :
        for enemy in row :
            enemy.x=enemy.x+2*direction
            if movedown:
                enemy.y=enemy.y+100
        
    

def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor('bullet')
        bullet.pos=galaga.pos
        bullets.append(bullet)

    print(bullets)


pgzrun.go()