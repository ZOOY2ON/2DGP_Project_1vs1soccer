from pico2d import *
import asyncio
import game_world
import time
from game_time import GameTime

Screen_x, Screen_y = 1920, 1080


class GamePrintTime:
    def __init__(self):
        self.end_game = load_image('GAME_ROUND/GameEndMSG.png')

        # RuleSetting 클래스의 인스턴스 생성
        rule_setting = GameTime()
        # timeset 값을 countdown_time으로 할당
        self.countdown_time = rule_setting.timeset

        # DNFBitBitv2.ttf 폰트를 로드
        self.font = load_font('Font/DNFBitBitv2.ttf', 50)

        self.start_time = time.time()
        self.show_count = True
        self.x, self.y = Screen_x // 2, Screen_y // 2

        self.end_check = False

    def update(self):
        if self.countdown_time > 0.1:
            self.countdown_time -= 0.05
            print(self.countdown_time)
        else:
            self.countdown_time = 0
            self.game_end()

    def draw(self):
        # 카운트 다운 시간 출력
        minutes = self.countdown_time // 60
        seconds = self.countdown_time % 60
        minutes = int(minutes)
        seconds = int(seconds)
        time_string = f'{minutes:02}:{seconds:02}'  # 분과 초를 2자리 숫자로 표현
        self.font.draw(self.x - 80, self.y + 500, time_string, (255, 255, 255))

        if self.end_check == True:
            self.end_game.clip_draw(0, 0, Screen_x, Screen_y, self.x, self.y)

    def game_end(self):
        self.end_check = True

    def handle_events(self, e):
        pass
