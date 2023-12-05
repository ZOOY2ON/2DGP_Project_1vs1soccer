from pico2d import *
import game_world

Screen_x, Screen_y = 1920, 1080


# [game_time] 게임 시간 설정 화면
class GameTime:
    def __init__(self):
        self.background = load_image('GAME_BACKGROUND/RuleSetting.png')
        self.game_timer = load_image('GAME_RESOURCE/Timer_minute.png')

        self.bottom = 0
        self.x, self.y = Screen_x // 2, Screen_y // 2
        self.timeset = 120  # timeset 속성을 초기화합니다.

    def update(self):
        pass

    def draw(self):
        self.background.clip_draw(0, 0, Screen_x, Screen_y, self.x, self.y)
        self.game_timer.clip_draw(0, self.bottom * 303, 303, 303, 960, 300)

    def handle_events(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:  # Check if it's a mouse button down event
            x, y = e.x, e.y  # Extract mouse coordinates based on your library's event structure

            # 시간 선택 이전/다음 버튼
            if 30 <= x <= 780 and 750 <= y <= 800:
                self.bottom = (self.bottom - 1) % 4
                self.timeset = 60 * (self.bottom + 1)

            elif 1140 <= x <= 1190 and 750 <= y <= 800:
                self.bottom = (self.bottom + 1) % 4
                self.timeset = 60 * (self.bottom + 1)

            # 이전버튼, 다음버튼
            if 40 <= x <= 170 and 510 <= y <= 650:
                game_world.clear()
                from game_start import GameStart
                gamestart = GameStart()
                game_world.add_object(gamestart, 0)
            elif 1745 <= x <= 1875 and 510 <= y <= 650:
                if self.bottom == 1:
                    game_world.clear()

                    from game_ground import GameGround
                    gameground = GameGround()
                    game_world.add_object(gameground, 1)
                else:
                    pass

                #from game_character import GameCharacter
                #gamecharacter = GameCharacter()
                #game_world.add_object(gamecharacter, 0)
