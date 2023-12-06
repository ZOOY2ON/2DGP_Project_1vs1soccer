from pico2d import *
import math
from game_start import GameStart


Screen_x, Screen_y = 1920, 1080

class Ball:
    def __init__(self, x, y, radius, speed, is_moving):
        self.x = x               # 공의 x 좌표
        self.y = y               # 공의 y 좌표
        self.radius = radius     # 공의 반지름
        self.speed = speed       # 공의 이동 속도
        self.is_moving = is_moving  # 공의 움직임 여부

        self.dx = 0              # 공의 x 방향 속도
        self.dy = 0              # 공의 y 방향 속도

        # === 공
        self.ball = load_image('GAME_ROUND/Ball.png')

    def update(self):
        if self.is_moving:
            self.x += self.dx * self.speed
            self.y += self.dy * self.speed

    def draw(self):
        self.ball.clip_draw(0, 0, 41, 41, self.x, self.y, 60, 60)

    def set_movement(self, dx, dy):
        self.dx = dx
        self.dy = dy

# [game_character] 게임 캐릭터 구현
class GameCharacter:
    def __init__(self):

        # === 캐릭터
        self.character_01 = load_image('GAME_CHARACTER/CharacterSheet.png')
        self.character_02 = load_image('GAME_CHARACTER/CharacterSheet.png')
        self.character_01_flip = load_image('GAME_CHARACTER/CharacterSheetFlip.png')
        self.character_02_flip = load_image('GAME_CHARACTER/CharacterSheetFlip.png')

        # === 캐릭터 설정
        self.ch_01_st = {'speed': 10, 'power': 3, 'jump': 13}   #5/3/3
        self.ch_02_st = {'speed': 6, 'power': 5, 'jump': 13}    #3/5/3

        self.ch_x_01, self.ch_x_02 = Screen_x * 0.3, Screen_x * 0.7     # 캐릭터 초기 위치 x 좌표
        self.ch_y_01, self.ch_y_02 = 300, 300  # 캐릭터 초기 위치 y 좌표

        self.dir_01, self.dir_02 = 0, 0     # 1 : right, -1 : left
        self.jump_01, self.jump_02 = False, False
        self.jump_01_count, self.jump_02_count = 0, 0
        self.jump_speed_01, self.jump_speed_02 = 2, 2

        self.character_1, self.character_2 = 1, 0   # 좌우대칭 확인용
        self.ch_r = 174 // 2

        # === 공
        self.ball = load_image('GAME_ROUND/Ball.png')

        # === 공 설정
        #self.ball_x, self.ball_y = Screen_x // 2, 230
        #self.ball_r = 60 // 2
        #self.ball_dx, self.ball_dy = 0, 0

        # === 공 객체 생성 (정지 상태)
        self.static_ball = Ball(Screen_x // 2, 230, 30, 10, False)   # x / y / 반지름 / 속도 / 움직임 여부

        # === 기본 설정
        self.x, self.y = Screen_x // 2, Screen_y // 2
        self.bottom_01, self.bottom_02 = 0, 4
        self.frame_01, self.frame_02 = 0, 0

        print("GameCharacter")

    def update(self):
        self.frame_01 = (self.frame_01 + 1) % 3
        self.frame_02 = (self.frame_02 + 1) % 3

        self.update_character()
        self.check_collision()

    def check_collision(self):
        # 공과 캐릭터 1의 충돌 검사
        distance_01 = math.sqrt((self.ch_x_01 - self.static_ball.x)**2 + (self.ch_y_01 - self.static_ball.y)**2)
        if distance_01 < self.ch_r + self.static_ball.radius:
            # 충돌 시 튕김
            self.bounce_ball(self.ch_01_st['power'], self.ch_x_01, self.ch_y_01)
            self.static_ball.is_moving = True
            print("충돌 발생 : ball-01")

        # 공과 캐릭터 2의 충돌 검사
        distance_02 = math.sqrt((self.ch_x_02 - self.static_ball.x)**2 + (self.ch_y_02 - self.static_ball.y)**2)
        if distance_02 < self.ch_r + self.static_ball.radius:
            # 충돌 시 튕김
            self.bounce_ball(self.ch_02_st['power'], self.ch_x_02, self.ch_y_02)
            self.static_ball.is_moving = True
            print("충돌 발생 : ball-02")

    def bounce_ball(self, power, character_x, character_y):
        # 충돌 시 튕김 로직
        direction_x = self.static_ball.x - character_x
        direction_y = self.static_ball.y - character_y
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)

        if distance != 0:  # 0으로 나누는 경우 방지
            direction_x /= distance
            direction_y /= distance

            # 튕겨나가는 거리 계산
            bounce_distance = power * 5

            self.static_ball.x = character_x + direction_x * (self.ch_r + self.static_ball.radius + bounce_distance)

            # 중력 효과 적용
            if self.static_ball.is_moving:
                self.static_ball.y += self.static_ball.speed
                self.static_ball.speed -= 0.5  # 중력 효과

                # 충돌 중에 땅에 닿으면 충돌 종료
                if self.static_ball.y < 230:
                    self.static_ball.y = 230
                    self.static_ball.speed = 0
                    self.static_ball.is_moving = False

                # 공의 이동 방향 업데이트
                self.static_ball.dx = direction_x
                self.static_ball.dy = direction_y
                print(self.static_ball.x, self.static_ball.y)

    def draw(self):
        self.draw_character()
        #self.ball.clip_draw(0, 0, 41, 41, self.ball_x,self.ball_y, 60, 60)
        # === 정지 상태의 공 그리기
        self.static_ball.draw()

    def handle_events(self, e):
        self.move_character(e)

    # === 캐릭터
    def draw_character(self):
        # 캐릭터 1 그리기
        if self.dir_01 == 1:  # 우측 바라보기
            self.character_01_flip.clip_draw(self.frame_01 * 174, self.bottom_01 * 174, 174, 174, self.ch_x_01, self.ch_y_01)
            self.character_1 = 1
        elif self.dir_01 == -1:  # 좌측 바라보기 (좌우 대칭)
            self.character_01.clip_draw(self.frame_01 * 174, self.bottom_01 * 174, 174, 174, self.ch_x_01, self.ch_y_01)
            self.character_1 = 0
        else:
            if self.character_1 == 1:
                self.character_01_flip.clip_draw(174, self.bottom_01 * 174, 174, 174, self.ch_x_01, self.ch_y_01)
            else:
                self.character_01.clip_draw(174, self.bottom_01 * 174, 174, 174, self.ch_x_01,self.ch_y_01)

        # 캐릭터 2 그리기
        if self.dir_02 == 1:  # 우측 바라보기
            self.character_02_flip.clip_draw(self.frame_02 * 174, self.bottom_02 * 174, 174, 174, self.ch_x_02, self.ch_y_02)
            self.character_2 = 1
        elif self.dir_02 == -1:  # 좌측 바라보기 (좌우 대칭)
            self.character_02.clip_draw(self.frame_02 * 174, self.bottom_02 * 174, 174, 174, self.ch_x_02, self.ch_y_02)
            self.character_2 = 0
        else:
            if self.character_2 == 1:
                self.character_02_flip.clip_draw(174, self.bottom_02 * 174, 174, 174, self.ch_x_02, self.ch_y_02)
            else:
                self.character_02.clip_draw(174, self.bottom_02 * 174, 174, 174, self.ch_x_02, self.ch_y_02)

    def update_character(self):
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

    def move_character(self,e):
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
