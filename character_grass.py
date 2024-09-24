from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)

def run_top():
    for x in range(0,800,10):
        draw_boy(x, 550)
    pass
def run_right():
    for y in range(550, -10, -10):
        draw_boy(790, y)
    pass
def run_bottom():
    for x in range(790, -10, -10):
        draw_boy(x, 0)
    pass
def run_left():
    for y in range(0, 560, 10):
        draw_boy(0, y)
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
        draw_boy(x,y)
    pass

def run_triangle():
    pass

while True:
    run_circle()
    run_rectangle()
    run_triangle()

close_canvas()

# 첫 줄 시작을 잘해야 한다. 곧바로 디테일하게 들어가지 말고 먼저 뼈대부터 잡는다. 함수를 먼저 호출하고 정의는 나중에 한다.

# 커밋은 그때그때 실행가능한 파일을 기준으로 하자.

# 테스트 리드 타임을 줄이기 위해 이미 검증된 코드는 실행에서 제외시킨다.