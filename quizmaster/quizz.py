import pgzrun

HEIGHT=700
WIDTH=800

q_no=0
current_question=" "
tot_q=0
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
    screen.draw.filled_rect(marquee_box,'black')
    screen.draw.filled_rect(question_box,'blue')
    screen.draw.filled_rect(timer_box,'green')
    for option in options:
        screen.draw.filled_rect(option,'cyan')
    screen.draw.filled_rect(skip_box,'purple')
    screen.draw.textbox(current_question[0].strip(),question_box)
    screen.draw.textbox(current_question[1].strip(),op1_box)
    screen.draw.textbox(current_question[2].strip(),op2_box)
    screen.draw.textbox(current_question[3].strip(),op3_box)
    screen.draw.textbox(current_question[4].strip(),op4_box)
    screen.draw.textbox("s\nk\ni\np",skip_box)
    screen.draw.textbox(f"welcome to the quiz master.\n this is question {q_no} out of {tot_q}",marquee_box)

def update():
    marquee_box.x=marquee_box.x-3
    if marquee_box.right<0:
        marquee_box.left=WIDTH

def read_question_file():
    global statments,tot_q

    file=open('quizmaster\questions.txt','r')
    content=file.read()
    file.close()
    statments=content.split('\n')
    tot_q=len(statments)

def read_next_question():
    global current_question,q_no

    current_question=statments.pop(0).split('|')
    q_no=q_no+1

def on_mouse_down(pos):
    if skip_box.collidepoint(pos):
        read_next_question()

    for option in options:
        if option.collidepoint(pos):
            if options.index(option)+1==int(current_question[5]):
                print("correct")





read_question_file()
print(statments)
read_next_question()

pgzrun.go()
