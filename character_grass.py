from pico2d import *

def run_rectangle():
    print('RECTANGLE')
    pass    # pass : 아직 생각이 잘 안돼서 일단 비워놓는 키워드

def run_circle():
    print('CIRCLE')
    pass

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

while True:
    run_circle()
    run_rectangle()

close_canvas()
