from pico2d import *
import game_world
from game_start import GameStart

Screen_x, Screen_y = 1920, 1080

class GameStop:
    def __init__(self):
        self.background = load_image('GAME_BACKGROUND/StopScreen.png')
        self.x, self.y = Screen_x // 2, Screen_y // 2

    def update(self):
        pass

    def draw(self):
        self.background.clip_draw(0, 0, Screen_x, Screen_y, self.x, self.y)

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_q:
                game_world.clear()
                from game_select import GameSelect  # Import inside the method
                game_list = GameSelect()
                game_world.add_object(game_list, 0)
            elif e.key == SDLK_e:
                game_world.clear()
                from game_ground import GameGround  # Import inside the method
                ground = GameGround()
                game_world.add_object(ground, 0)
