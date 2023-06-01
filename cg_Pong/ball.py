from setup import pg

from setup import font20, screen, clock
from setup import BLACK, WHITE, GREEN
from setup import WIDTH, HEIGHT, FPS


class Ball:
    """
    Ball class
    ----------
    NOTE: doc types assume that pygame has been imported as pg.
    """

    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.x_fac = 1
        self.y_fac = -1
        self.ball = pg.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius
        )
        self.first_time = 1

    def display(self):
        self.ball = pg.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius
        )