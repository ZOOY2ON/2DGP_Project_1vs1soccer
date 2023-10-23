from pico2d import load_image


class BackGround:
    def __init__(self, x = 0, y = 0):
        self.x , self.y = x, y
        self.background = load_image('Screen_InGame.png')

    def draw(self):
        self.background.clip_draw(0, 0, 4400, 2475, self.x, self.y, 880, 495)

    def update(self):
        pass
