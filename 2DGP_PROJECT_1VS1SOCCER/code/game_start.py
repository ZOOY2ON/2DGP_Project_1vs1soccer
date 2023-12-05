from pico2d import *
import game_world


Screen_x, Screen_y = 1920, 1080

# [game_start] 캐릭터를 선택합니다.
class GameStart:
    def __init__(self):

        from game_mouse import GameMouse
        gamemouse = GameMouse()
        game_world.add_object(gamemouse, 2)

        self.background = load_image('GAME_BACKGROUND/CharacterSelect.png')
        self.x, self.y = Screen_x // 2, Screen_y // 2
        self.character_01 = load_image('GAME_CHARACTER/CharacterSheet.png')
        self.character_02 = load_image('GAME_CHARACTER/CharacterSheet.png')
        self.characterST_01 = load_image('GAME_CHARACTER/CharacterSTSheet.png')
        self.characterST_02 = load_image('GAME_CHARACTER/CharacterSTSheet.png')
        self.bottom_01, self.bottom_02 = 0, 1
        self.frame_01, self.frame_02 = 0, 0

    def update(self):
        self.frame_01 = (self.frame_01 + 1) % 3
        self.frame_02 = (self.frame_02 + 1) % 3

    def draw(self):
        self.background.clip_draw(0, 0, Screen_x, Screen_y, self.x, self.y)
        self.character_01.clip_draw(self.frame_01 * 174, self.bottom_01 * 174, 174, 174, 530, 530)
        self.character_02.clip_draw(self.frame_02 * 174, self.bottom_02 * 174, 174, 174, 1370, 530)
        self.characterST_01.clip_draw(0, self.bottom_01 * 528, 436, 528, 540, 450)
        self.characterST_02.clip_draw(0, self.bottom_02 * 528, 436, 528, 1380, 450)

    def handle_events(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:  # Check if it's a mouse button down event
            x, y = e.x, e.y  # Extract mouse coordinates based on your library's event structure

            #이전버튼
            if 40 <= x <= 170 and 510 <= y <= 650:
                game_world.clear()
                from game_select import GameSelect
                game_list = GameSelect()
                game_world.add_object(game_list, 0)

            #다음버튼
            if self.bottom_01 == 0 and self.bottom_02 == 4:
                if 1745 <= x <= 1875 and 510 <= y <= 650:
                    game_world.clear()
                    from game_time import GameTime
                    gametime = GameTime()
                    game_world.add_object(gametime, 0)
            elif self.bottom_01 == 4 and self.bottom_02 == 0:
                if 1745 <= x <= 1875 and 510 <= y <= 650:
                    game_world.clear()
                    from game_time import GameTime
                    gametime = GameTime()
                    game_world.add_object(gametime, 0)
            else:
                pass

            #p1 캐릭터 이전/다음 버튼
            if 280 <= x <= 310 and 520 <= y <= 560:
                self.bottom_01 = (self.bottom_01 - 1) % 6
                if self.bottom_01 == self.bottom_02:
                    self.bottom_01 = (self.bottom_01 - 1) % 6
            elif 770 <= x <= 800 and 520 <= y <= 560:
                self.bottom_01 = (self.bottom_01 + 1) % 6
                if self.bottom_01 == self.bottom_02:
                    self.bottom_01 = (self.bottom_01 + 1) % 6

            #p2 캐릭터 이전/다음 버튼
            if 1110 <= x <= 1140 and 520 <= y <= 560:
                self.bottom_02 = (self.bottom_02 - 1) % 6
                if self.bottom_02 == self.bottom_01:
                    self.bottom_02 = (self.bottom_02 - 1) % 6
            elif 1600 <= x <= 1630 and 520 <= y <= 560:
                self.bottom_02 = (self.bottom_02 + 1) % 6
                if self.bottom_02 == self.bottom_01:
                    self.bottom_02 = (self.bottom_02 + 1) % 6

            self.bottom_value()

    def bottom_value(self):
        if self.bottom_01 != None and self.bottom_02 !=None:
            print(self.bottom_01, self.bottom_02)
            return (self.bottom_01,self.bottom_02)
        else:
            self.bottom_01, self.bottom_02 = 0, 1
            print("bottom 값이 존재하지 않습니다.")
