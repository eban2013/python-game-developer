import pgzrun
import random 

WIDTH=800
HIGHT=600

satellite_no=8

satellites=[]
for i in range(satellite_no):
    satellite=Actor("satellite")

    satellite.x=random.randint(50,WIDTH-50)
    satellite.y=random.randint(50,HIGHT-50)

    satellites.append(satellite)
    
print(satellites)



def draw():

    screen.blit("space",(0,0))
    for sat in satellites:
        sat.draw()





pgzrun.go()