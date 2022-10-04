from pico2d import *
import turtle

open_canvas()

running_boy = load_image('animation_sheet.png')

frame = 0

direction = 3

x, y = 0

def drawing(direction):
    claer_canvas()
    running_boy.clip_draw(frame* 

