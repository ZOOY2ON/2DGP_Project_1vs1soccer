from pico2d import *
import game_world
from game_how import GameHow
from game_start import GameStart

Screen_x, Screen_y = 1920, 1080


class GameSelect:
    def __init__(self):
        self.frame = 0
        self.image = load_image('GAME_BACKGROUND/MainScreen.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, Screen_x, Screen_y, Screen_x/2, Screen_y/2)

    def handle_events(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:  # Check if it's a mouse button down event
            x, y = e.x, e.y  # Extract mouse coordinates based on your library's event structure

            if 200 <= x <= 770 and 740 <= y <= 920:
                # Mouse click coordinates are in the range 200,740 to 770,920
                game_world.clear()
                gamehow = GameHow()
                game_world.add_object(gamehow, 0)
            elif 1150 <= x <= 1700 and 740 <= y <= 920:
                # Mouse click coordinates are in the range 1150,740 to 1700,920
                game_world.clear()
                gamestart = GameStart()
                game_world.add_object(gamestart, 0)
