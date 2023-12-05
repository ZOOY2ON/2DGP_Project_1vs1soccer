from pico2d import *
import game_world

Screen_x, Screen_y = 1920, 1080


# [game_mouse] 마우스
class GameMouse:
    def __init__(self):
        self.mouse = load_image('GAME_RESOURCE/mouse_set.png')
        self.x, self.y = Screen_x // 2, Screen_y // 2
        self.mouse_x, self.mouse_y = Screen_x // 2, Screen_y // 2
        self.bottom = 1

    def update(self):
        pass

    def draw(self):
        self.mouse.clip_draw(0, self.bottom * 120, 120, 120, self.mouse_x, self.mouse_y)

    def handle_events(self, e):
        if e.type == SDL_MOUSEMOTION:
            self.mouse_x, self.mouse_y = e.x, pico2d.get_canvas_height() - e.y - 1

        if e.type == SDL_MOUSEBUTTONUP:
            self.bottom = 1
        elif e.type == SDL_MOUSEBUTTONDOWN:
            self.bottom = 0

