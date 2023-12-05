from pico2d import *
import random
import game_world
from game_select import Game_List

SCREEN_X, SCREEN_Y = 1600, 900


class Title:
    def __init__(self):
        self.background = load_image('resource/Screen/Screen_Main.png')
        self.x, self.y = SCREEN_X // 2, SCREEN_Y // 2

    def update(self):
        pass

    def draw(self):
        self.background.clip_draw(0, 0, 724, 384, self.x, self.y, SCREEN_X, SCREEN_Y)

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
            game_world.clear()
            game_list = Game_List()
            game_world.add_object(game_list, 0)