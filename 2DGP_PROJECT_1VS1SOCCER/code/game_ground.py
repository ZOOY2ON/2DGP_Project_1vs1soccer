from pico2d import *
import game_world
import time
from game_time import GameTime

Screen_x, Screen_y = 1920, 1080

class GameGround:
    def __init__(self):
        self.background = load_image('GAME_ROUND/BackGround.png')

        # === 카운트다운
        self.count_03 = load_image('GAME_BACKGROUND/StartCount_03.png')
        self.count_02 = load_image('GAME_BACKGROUND/StartCount_02.png')
        self.count_01 = load_image('GAME_BACKGROUND/StartCount_01.png')

        # === 운동장
        self.ground = load_image('GAME_ROUND/Ground.png')

        # RuleSetting 클래스의 인스턴스 생성
        rule_setting = GameTime()
        # timeset 값을 countdown_time으로 할당
        self.countdown_time = rule_setting.timeset
        print("countdown_time : ",self.countdown_time)

        # DNFBitBitv2.ttf 폰트를 로드
        self.font = load_font('Font/DNFBitBitv2.ttf', 50)

        self.start_time = time.time()
        self.show_count = True
        self.x, self.y = Screen_x // 2, Screen_y // 2

        from game_character import GameCharacter
        character = GameCharacter()
        game_world.add_object(character, 0)


    # Ground 클래스의 update 메서드 전체를 아래와 같이 수정
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

            if self.countdown_time > 0:
                delay(1)
                self.countdown_time -= 1


    def draw(self):
        if self.count_image is not None:
            self.count_image.clip_draw(0, 0, Screen_x, Screen_y, self.x, self.y)
        else:
            self.background.clip_draw(0, 0, Screen_x, Screen_y, self.x, self.y)

            # 카운트 다운 시간 출력
            self.font.draw(self.x, self.y + 500, f'{self.countdown_time // 60}:{self.countdown_time % 60}',(255, 255, 255))

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            game_world.clear()
            from game_stop import GameStop
            stopgame = GameStop()
            game_world.add_object(stopgame, 0)
