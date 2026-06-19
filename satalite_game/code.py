import pgzrun
import random 
import time 

WIDTH=800
HIGHT=600

sat_order=0
satellite_no=8

current_sat=0

lines=[]

satellites=[]
for i in range(satellite_no):



    satellite=Actor("satellite")

    satellite.x=random.randint(50,WIDTH-50)
    satellite.y=random.randint(50,HIGHT-50)

    satellites.append(satellite)

starttime=time.time()
timelaps=0


def draw():
    sat_order=1

    screen.blit("space",(0,0))
    for sat in satellites:
        sat.draw()
        screen.draw.text (str(sat_order),(sat.x-30,sat.y-30))
        sat_order=sat_order+1

    for line in lines:
        screen.draw.line(line[0],line[1],'white')

    screen.draw.text (str(timelaps),(50,50))

def update():
    global timelaps
    if current_sat<satellite_no:
        timelaps=round(time.time()-starttime,2)

def on_mouse_down(pos):
    global current_sat,lines
    if satellites[current_sat].collidepoint(pos):
        if current_sat>0 :
            start=satellites[current_sat].pos
            end=satellites[current_sat-1].pos
            lines.append([start,end])
    
        current_sat=current_sat+1
    else:
        current_sat=0
        lines=[]
    




pgzrun.go()