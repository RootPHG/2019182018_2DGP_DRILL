from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_char_and_grass(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)


x1 = 400
y1 = 90
R=180
while(True):   
    while(R<360):
        draw_char_and_grass(400 + 210*math.sin(R/360*2*math.pi), 300 + 210*math.cos(R/360*2*math.pi))
        R = R+1
        delay(0.01)
    R=0
    while(R<180):
        draw_char_and_grass(400 + 210*math.sin(R/360*2*math.pi), 300 + 210*math.cos(R/360*2*math.pi))
        R = R+1
        delay(0.01)
    while(x1<800):
        draw_char_and_grass(x1, y1)
        x1 = x1+2
        delay(0.01)
    while(y1<550):
        draw_char_and_grass(x1, y1)
        y1 = y1+2
        delay(0.01)
    while(x1>0):
        draw_char_and_grass(x1, y1)
        x1 = x1-2
        delay(0.01)
    while(y1>90):
        draw_char_and_grass(x1, y1)
        y1 = y1-2
        delay(0.01)
    while(x1<400):
        draw_char_and_grass(x1, y1)
        x1 = x1+2
        delay(0.01)
    

close_canvas()
