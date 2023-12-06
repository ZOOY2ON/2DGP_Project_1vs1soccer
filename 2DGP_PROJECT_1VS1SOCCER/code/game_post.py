from pico2d import *
import game_world

Screen_x, Screen_y = 1920, 1080


# [game_post] 골대 앞면
class GamePost:
    def __init__(self):

        # === 골대
        self.post_front_r = load_image('GAME_ROUND/PostFront.png')
        self.post_front_l = load_image('GAME_ROUND/PostFront_Left.png')

    def update(self):
        pass

    def draw(self):
        self.post_front_r.clip_draw(0, 0, 342, 593, 1740, 365)
        self.post_front_l.clip_draw(0, 0, 342, 593, 180, 365)

    def handle_events(self, e):
        pass
