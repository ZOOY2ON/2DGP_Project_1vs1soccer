from pico2d import *
import game_world

SCREEN_X, SCREEN_Y = 1600, 900

class Game_Select:
    def __init__(self):
        self.frame = 0
        self.image = load_image('resource/Screen/Screen_Select.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(SCREEN_X // 2, SCREEN_Y // 2)

    def handle_events(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            x, y = e.x, SCREEN_Y - e.y  # 윈도우 좌표계에서 게임 좌표계로 변환

            # 만약 마우스 클릭 좌표가 x1, y1 ~ x2, y2일 경우 game_world.add_object(start, 0)
            if x >= 172 and x <= 646 and y >= 133 and y <= 285:
                game_start = Game_ch_Select()
                game_world.add_object(game_start, 0)

            # 만약 마우스 클릭 좌표가 x3, y1 ~ x3, y2일 경우 game_world.add_object(how, 0)
            elif x >= 957 and x <= 1431 and y >= 133 and y <= 285:
                game_how = Game_How()
                game_world.add_object(game_how, 0)
