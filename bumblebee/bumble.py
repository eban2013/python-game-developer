import pgzrun
import random

WIDTH=600
HEIGHT=500

gameover=False 
score=0


bee=Actor("bee")
flower=Actor("flower")

flower.x=random.randint(30,WIDTH-30)
flower.y=random.randint(30,HEIGHT-30)


def draw():
    if not gameover:
        screen.blit("bg",(0,0))

        screen.draw.text(str(score),(10,10))

        flower.draw()
        bee.draw()
    else:
        screen.fill("green")
        screen.draw.text(f"game over youtr final score is {score}",(50,50))
#whith this code you have to stay pressing the key over and over againg you cant hold the key

# def on_key_down(key):
#     print(key)
#     if key==keys.D:
#         bee.x=bee.x+5

def update():
    global score

    if keyboard.d:
        bee.x=bee.x+5

    if keyboard.a:
        bee.x=bee.x-5
    
    if keyboard.w:
        bee.y=bee.y-5

    if keyboard.s:
        bee.y=bee.y+5
    

    if bee.colliderect(flower):
        flower.x=random.randint(30,WIDTH-30)
        flower.y=random.randint(30,HEIGHT-30)
        score=score+10


def timeup ():
    global gameover 

    gameover=True

clock.schedule(timeup,10)
pgzrun.go()   