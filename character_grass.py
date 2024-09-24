from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def run_top():
    print('TOP')
    pass
def run_right():
    print('RIGHT')
    pass
def run_bottom():
    pass
def run_left():
    pass

def run_rectangle():
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass    # pass : 아직 생각이 잘 안돼서 일단 비워놓는 키워드

def run_circle():
        #Logic
    r, cx, cy = 300, 800 // 2, 600 // 2
    for degree in range(0, 360):
        x = r * math.cos(math.radians(degree)) + cx
        y = r * math.sin(math.radians(degree)) + cy

        #Rendering
        clear_canvas_now()
        grass.draw_now(400, 30)
        boy.draw_now(x,y)
        delay(0.01)
    pass

while True:
    run_circle()
    run_rectangle()
    break

close_canvas()
