import random
import pgzrun

WIDTH=800
HEIGHT=600
TITLE='collect the apples'

gameover=False

basket=Actor("basket")
basket.pos=(400, 550)
apple=Actor("apple")
apple.pos=(400, 0)
score=0

def draw():
    screen.fill("white")
    if not gameover:
        basket.draw()
        apple.draw()
        screen.draw.text("Score: " + str(score), (10, 10), color="black")
    else:
        screen.draw.text("youre final score is :" + str(score), center=(WIDTH/2,HEIGHT/2), color="black")
    

def update():
    global score 
    if not gameover:
        apple.y+=5
        if apple.colliderect(basket):
            score+=1
            apple.y=0
            apple.x=random.randint(50, 750)
        if apple.y>HEIGHT:
            score=0
            apple.y=0
            apple.x=random.randint(50, 750)

        if keyboard.left:
            basket.x-=5
        if keyboard.right:
            basket.x+=5

def timeup ():
    global gameover 

    gameover=True

clock.schedule(timeup,60)
pgzrun.go()   

