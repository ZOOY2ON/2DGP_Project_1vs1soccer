from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1600, 900
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('Screen_Select.png')


def handle_events():
    global running
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            print("Mouse Clicked at (x: {}, y: {})".format(event.x, TUK_HEIGHT - 1 - event.y))


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2


while running:
    clear_canvas()

    tuk_ground.clip_draw(0, 0, 4400, 2475, TUK_WIDTH // 2, TUK_HEIGHT // 2, TUK_WIDTH, TUK_HEIGHT)

    update_canvas()
    handle_events()

close_canvas()




