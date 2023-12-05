from pico2d import *
import game_world
from game_select import GameSelect

Screen_x, Screen_y = 1920, 1080


# [game_title] 게임 타이틀 화면
class GameTitle:
    def __init__(self):
        self.background = load_image('GAME_BACKGROUND/StartScreen.png')
        self.x, self.y = Screen_x // 2, Screen_y // 2

    def update(self):
        pass

    def draw(self):
        self.background.clip_draw(0, 0, Screen_x, Screen_y, self.x, self.y)

    def handle_events(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            game_world.clear()
            game_list = GameSelect()
            game_world.add_object(game_list, 0)