from pico2d import *

import game_world
from game_title import GameTitle
from game_select import GameSelect

# === 스크린 사이즈
Screen_x, Screen_y = 1920, 1080
GAME_NUM = 0

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DELETE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_BACKSPACE:
            game_world.clear()
            game_list = GameSelect()
            game_world.add_object(game_list, 0)
        else:
            game_world.handle_events(event)

def reset_world():
    global running

    running = True
    title = GameTitle()
    game_world.add_object(title, 0)


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas(Screen_x, Screen_y)
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
