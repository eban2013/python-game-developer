import pgzrun

HEIGHT=800
WIDTH=800

marquee_box=Rect(0,0,800,70)
question_box=Rect(20,90,500,200)


def draw():
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,'orange')
    screen.draw.filled_rect(question_box,'blue')

pgzrun.go()