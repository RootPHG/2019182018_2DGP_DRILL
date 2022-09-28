from pico2d import*

open_canvas()

rockman = load_image('img.png')

frame = 0
for x in range(0, 800, 5):
    clear_canvas()
    rockman.clip_draw(frame * 130, 0, 130, 360, x, 90)
    frame = (frame + 1) % 5
    delay(0.01)
    get_events()


close_canvas()
