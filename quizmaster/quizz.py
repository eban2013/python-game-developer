import pgzrun

HEIGHT=700
WIDTH=800

statments=[]

marquee_box=Rect(0,0,800,70)
question_box=Rect(20,90,550,200)
timer_box=Rect(590,90,190,200)
op1_box=Rect(20,310,265,150)
op2_box=Rect(305,310,265,150)
op3_box=Rect(20,480,265,150)
op4_box=Rect(305,480,265,150)
skip_box=Rect(590,310,190,320)

options=[op1_box,op2_box,op3_box,op4_box]

def draw():
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,'orange')
    screen.draw.filled_rect(question_box,'blue')
    screen.draw.filled_rect(timer_box,'green')
    for option in options:
        screen.draw.filled_rect(option,'cyan')
    screen.draw.filled_rect(skip_box,'purple')
    
def update():
    pass

def read_question_file():
    global statments

    file=open('quizmaster\questions.txt','r')
    content=file.read()
    file.close()
    statments=content.split('\n')


read_question_file()
print(statments)

pgzrun.go()