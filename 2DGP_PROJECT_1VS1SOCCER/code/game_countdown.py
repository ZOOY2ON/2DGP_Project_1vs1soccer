from pico2d import *
import game_world
import time

Screen_x, Screen_y = 1920, 1080


# [game_countdown] 게임 진입 카운트다운
class GameCountDown:
    def __init__(self):
        # === 카운트다운
        self.count_03 = load_image('GAME_BACKGROUND/StartCount_03.png')
        self.count_02 = load_image('GAME_BACKGROUND/StartCount_02.png')
        self.count_01 = load_image('GAME_BACKGROUND/StartCount_01.png')

        self.start_time = time.time()
        self.show_count = True
        self.x, self.y = Screen_x // 2, Screen_y // 2

    def update(self):
        current_time = time.time() - self.start_time

        if current_time < 3.0:
            if current_time < 1.0:
                self.count_image = self.count_03
            elif current_time < 2.0:
                self.count_image = self.count_02
            else:
                self.count_image = self.count_01
        else:
            if self.show_count:
                self.show_count = False
                self.count_image = None

    def draw(self):
        if self.count_image is not None:
            self.count_image.clip_draw(0, 0, Screen_x, Screen_y, self.x, self.y)
        else:
            game_world.clear()
            from game_ground import GameGround
            gameground = GameGround()
            game_world.add_object(gameground, 0)

    def handle_events(self, e):
        pass