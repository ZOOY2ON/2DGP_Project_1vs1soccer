from pico2d import load_image


class Grass:
    def __init__(self, x = 0, y = 0):
        self.x , self.y = x, y
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
