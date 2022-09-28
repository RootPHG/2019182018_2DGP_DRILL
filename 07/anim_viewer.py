from pico2d import *

open_canvas()


rockman = load_image('img.png')

frame = 0
y = 0
for x in range(0, 800, 5):
    clear_canvas()
    rockman.clip_draw(frame * 170, y * 170, 170, 180, x, 90)
    update_canvas()
    frame = (frame + 1) % 5
    y = (y+1) % 2
    delay( 0.05)
    get_events()


close_canvas()
