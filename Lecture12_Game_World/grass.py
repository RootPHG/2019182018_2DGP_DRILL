from pico2d import *
import game_world
class Grass:
    def __init__(self, y):
        self.image = load_image('grass.png')
        self.y = y

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, self.y)


