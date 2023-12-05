from pico2d import *
import game_world

Screen_x, Screen_y = 1920, 1080


# [game_ground] 게임 플레이 화면
class GameGround:
    def __init__(self):
        self.background = load_image('GAME_ROUND/BackGround.png')

        # === 운동장
        self.ground = load_image('GAME_ROUND/Ground.png')

        from game_character import GameCharacter
        character = GameCharacter()
        game_world.add_object(character, 0)

        from game_printtime import GamePrintTime
        gameprinttime = GamePrintTime()
        game_world.add_object(gameprinttime, 0)

    def update(self):
        pass

    def draw(self):
        pass

    def handle_events(self, e):
        if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            game_world.clear()
            from game_stop import GameStop
            stopgame = GameStop()
            game_world.add_object(stopgame, 0)
