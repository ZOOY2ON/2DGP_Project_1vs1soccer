from pico2d import *
from game_start import GameStart


Screen_x, Screen_y = 1920, 1080


# [game_character] 게임 캐릭터 구현
class GameCharacter:
    def __init__(self):
        self.ch_01_st = {'speed': 10, 'power': 3, 'jump': 14}
        self.ch_02_st = {'speed': 6, 'power': 4, 'jump': 11}

        # === 캐릭터
        self.character_01 = load_image('GAME_CHARACTER/CharacterSheet.png')
        self.character_02 = load_image('GAME_CHARACTER/CharacterSheet.png')

        # === 설정
        self.x, self.y = Screen_x // 2, Screen_y // 2
        self.ch_x_01, self.ch_x_02 = Screen_x * 0.3, Screen_x * 0.7     # 캐릭터 초기 위치
        self.ch_y_01, self.ch_y_02 = 300, 300  # 캐릭터 초기 위치

        self.bottom_01, self.bottom_02 = 0,1
        self.frame_01, self.frame_02 = 0, 0
        self.dir_01, self.dir_02 = 0, 0     # 1 : right, -1 : left
        self.jump_01, self.jump_02 = False, False
        self.jump_01_count, self.jump_02_count = 0, 0       # ???
        self.jump_speed_01, self.jump_speed_02 = 2, 2

        print("GameCharacter")

    def update(self):
        self.frame_01 = (self.frame_01 + 1) % 3
        self.frame_02 = (self.frame_02 + 1) % 3

        # 캐릭터 1 이동 및 점프 로직
        if self.dir_01 == 1:  # 우측 이동 중
            self.ch_x_01 += self.ch_01_st['speed']
        elif self.dir_01 == -1:  # 좌측 이동 중
            self.ch_x_01 -= self.ch_01_st['speed']

        if self.jump_01:
            self.ch_y_01 += self.jump_speed_01
            self.jump_speed_01 -= 0.6  # 중력 효과

            # 점프 중에 땅에 닿으면 점프 종료
            if self.ch_y_01 < 300:
                self.ch_y_01 = 300
                self.jump_speed_01 = 0
                self.jump_01 = False

        # 캐릭터 2 이동 및 점프 로직
        if self.dir_02 == 1:  # 우측 이동 중
            self.ch_x_02 += self.ch_02_st['speed']
        elif self.dir_02 == -1:  # 좌측 이동 중
            self.ch_x_02 -= self.ch_02_st['speed']

        if self.jump_02:
            self.ch_y_02 += self.jump_speed_02
            self.jump_speed_02 -= 0.6  # 중력 효과

            # 점프 중에 땅에 닿으면 점프 종료
            if self.ch_y_02 < 300:
                self.ch_y_02 = 300
                self.jump_speed_02 = 0
                self.jump_02 = False

    def draw(self):
        # 캐릭터 1 그리기
        if self.dir_01 == 1:  # 우측 바라보기
            self.character_01.clip_draw(self.frame_01 * 174, self.bottom_01 * 174, 174, 174, self.ch_x_01, self.ch_y_01)
        elif self.dir_01 == -1:  # 좌측 바라보기 (좌우 대칭)
            self.character_01.clip_draw(self.frame_01 * 174, self.bottom_01 * 174, 174, 174, self.ch_x_01, self.ch_y_01)
        else:
            self.character_01.clip_draw(174, self.bottom_01 * 174, 174, 174, self.ch_x_01, self.ch_y_01)

        # 캐릭터 2 그리기
        if self.dir_02 == 1:  # 우측 바라보기
            self.character_02.clip_draw(self.frame_02 * 174, self.bottom_02 * 174, 174, 174, self.ch_x_02, self.ch_y_02)
        elif self.dir_02 == -1:  # 좌측 바라보기 (좌우 대칭)
            self.character_02.clip_draw(self.frame_02 * 174, self.bottom_02 * 174, 174, 174, self.ch_x_02, self.ch_y_02)
        else:
            self.character_02.clip_draw(174, self.bottom_02 * 174, 174, 174, self.ch_x_02, self.ch_y_02)

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN:
            # === 캐릭터 1 움직임 동작
            if e.key == SDLK_w and not self.jump_01:
                self.jump_01 = True
                self.jump_speed_01 = self.ch_01_st['jump']
            if e.key == SDLK_d:
                self.dir_01 = 1
            elif e.key == SDLK_a:
                self.dir_01 = -1

            # === 캐릭터 2 움직임 동작
            if e.key == SDLK_UP and not self.jump_02:
                self.jump_02 = True
                self.jump_speed_02 = self.ch_02_st['jump']
            if e.key == SDLK_RIGHT:
                self.dir_02 = 1
            elif e.key == SDLK_LEFT:
                self.dir_02 = -1

        elif e.type == SDL_KEYUP:
            # === 캐릭터 1 움직임 멈춤
            if e.key == SDLK_d or e.key == SDLK_a:
                self.dir_01 = 0

            # === 캐릭터 2 움직임 멈춤
            if e.key == SDLK_RIGHT or e.key == SDLK_LEFT:
                self.dir_02 = 0
