from pico2d import *
import game_world

Screen_x, Screen_y = 1920, 1080


# [game_background] 게임 배경 레이어
class GameBackGround:
    def __init__(self):
        self.background = load_image('GAME_ROUND/BackGround.png')
        self.ground = load_image('GAME_ROUND/Ground.png')
        self.x, self.y = Screen_x // 2, Screen_y // 2
        self.ground_x = Screen_x // 2

    def update(self):
        pass

    def draw(self):
        self.background.clip_draw(0, 0, Screen_x, Screen_y, self.x, self.y)
        self.ground.clip_draw(2000, 0, 2000, 460, self.ground_x, 228, 2000, 460)

    def handle_events(self, e):
        pass
