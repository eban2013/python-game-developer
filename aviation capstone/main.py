import pgzrun

WIDTH = 1200
HEIGHT = 800
TITLE = "Plane Spotter Quiz"


easy_btn = Rect((425, 220), (350, 60))
medium_btn = Rect((425, 300), (350, 60))
hard_btn = Rect((425, 380), (350, 60))
instructions_btn = Rect((425, 460), (350, 60))
exit_btn = Rect((425, 540), (350, 60))


def draw_button(rect, text):
    screen.draw.filled_rect(rect, (30, 80, 180))      
    screen.draw.rect(rect, (255, 255, 255))           
    screen.draw.text(
        text,
        center=rect.center,
        fontsize=42,
        color="white"
    )


def draw():
    
    screen.fill((135, 206, 235))  

    
    screen.draw.text(
        "PLANE SPOTTER QUIZ",
        center=(WIDTH // 2, 80),
        fontsize=80,
        color="navy"
    )

    
    screen.draw.text(
        "Guess the Aircraft!",
        center=(WIDTH // 2, 145),
        fontsize=45,
        color="black"
    )

    
    draw_button(easy_btn, "Easy")
    draw_button(medium_btn, "Medium")
    draw_button(hard_btn, "Hard")
    draw_button(instructions_btn, "Instructions")
    draw_button(exit_btn, "Exit")


def on_mouse_down(pos):

    if easy_btn.collidepoint(pos):
        print("Easy selected")

    elif medium_btn.collidepoint(pos):
        print("Medium selected")

    elif hard_btn.collidepoint(pos):
        print("Hard selected")

    elif instructions_btn.collidepoint(pos):
        print("Instructions selected")

    elif exit_btn.collidepoint(pos):
        exit()


pgzrun.go()