from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def run_rectangle():
    pass    # pass : 아직 생각이 잘 안돼서 일단 비워놓는 키워드

def run_circle():
    boy.draw_now(400,90)
    delay(1)
    pass

while True:
    run_circle()
    run_rectangle()
    break

close_canvas()
