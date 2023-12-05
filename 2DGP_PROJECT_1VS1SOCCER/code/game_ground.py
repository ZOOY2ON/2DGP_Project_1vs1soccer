from pico2d import *
import game_world
import time
from rulesetting import RuleSetting
from game_character import GameCharacter

Screen_x, Screen_y = 1920, 1080

class GameGround:
    def __init__(self):
        self.background = load_image('GAME_ROUND/BackGround.png')

        # === 카운트다운
        self.count_03 = load_image('GAME_BACKGROUND/StartCount_03.png')
        self.count_02 = load_image('GAME_BACKGROUND/StartCount_02.png')
        self.count_01 = load_image('GAME_BACKGROUND/StartCount_01.png')

        # === 운동장 & 공
        self.ground = load_image('GAME_ROUND/Ground.png')
        self.ball = load_image('GAME_ROUND/Ball.png')

        # RuleSetting 클래스의 인스턴스 생성
        rule_setting = RuleSetting()
        # timeset 값을 countdown_time으로 할당
        self.countdown_time = rule_setting.timeset
        print("countdown_time : ",self.countdown_time)

        # DNFBitBitv2.ttf 폰트를 로드
        self.font = load_font('Font/DNFBitBitv2.ttf', 50)


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

        # 키 입력 상태 업데이트
        if e.type == SDL_KEYDOWN:
            self.handle_key_down(e.key)
        elif e.type == SDL_KEYUP:
            self.handle_key_up(e.key)

    def handle_key_down(self, key):
        if key in self.key_states:
            self.key_states[key] = True

    def handle_key_up(self, key):
        if key in self.key_states:
            self.key_states[key] = False

    def is_collide_character(self, character_x, character_y, character_image):
        character_left = character_x - 87
        character_right = character_x + 87
        character_bottom = character_y - 87
        character_top = character_y + 87

        ball_left = 960 + self.ball_x - 20
        ball_right = 960 + self.ball_x + 20
        ball_bottom = 230 - 20
        ball_top = 230 + 20

        # 충돌 검사
        if character_right < ball_left or character_left > ball_right or \
           character_top < ball_bottom or character_bottom > ball_top:
            return False  # 충돌하지 않음
        else:
            return True  # 충돌함

