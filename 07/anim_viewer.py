from pico2d import *

open_canvas()

girl = load_image('running.png')

frame = 0

direction = 1
y = 90
for x in range(0, 800, 10):
    clear_canvas()
    girl.clip_draw(frame * 60, direction * 60, 60, 60, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay( 0.05)
    get_events()

direction = 0

for y in range(90, 580, 10):
    clear_canvas()
    girl.clip_draw(frame * 60, direction * 60, 60, 60, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay( 0.05)
    get_events()

direction = 2

for x in range(800, 0, -10):
    clear_canvas()
    girl.clip_draw(frame * 60, direction * 60, 60, 60, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay( 0.05)
    get_events()

direction = 3

for y in range(580, 90, -10):
    clear_canvas()
    girl.clip_draw(frame * 60, direction * 60, 60, 60, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay( 0.05)
    get_events()

close_canvas()
