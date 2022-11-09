from pico2d import *
import game_world
import random
import game_framework


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 100.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Bird:
    image = None

    def __init__(self, x = 200 + random.randint(0, 100), y = 300):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.frame = 0
        self.x, self.y, self.velocity = x, y, 1

    def draw(self):
        if self.velocity > 0:
            self.image.clip_draw(int(self.frame)*100, 0, 100, 100, self.x, self.y)
        elif self.velocity < 0:
            self.image.clip_composite_draw(int(self.frame)*100, 0, 100, 100, 180, 'v',self.x, self.y)

    def update(self):
        self.x += self.velocity * RUN_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if self.x < 25 or self.x > 1600 - 25:
            self.velocity = self.velocity * -1
