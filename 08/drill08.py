from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir_x
    global dir_y
    global anime

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                anime = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                anime = 0
            elif event.key == SDLK_UP:
                dir_y += 1
                anime -= 2
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                anime -= 2
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                anime = 3
            elif event.key == SDLK_LEFT:
                dir_x += 1
                anime = 2
            elif event.key == SDLK_UP:
                dir_y -= 1
                anime += 2
            elif event.key == SDLK_DOWN:
                dir_y += 1
                anime += 2


open_canvas()

running_boy = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')

running = True
frame = 0
dir_x = 0
dir_y = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
anime = 3

while running:
    clear_canvas()
    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    running_boy.clip_draw(frame * 100, anime * 100, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    x += dir_x * 5
    y += dir_y * 5
    handle_events()

close_canvas()

