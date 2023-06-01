import pygame as pg

from setup import font20, screen, clock
from setup import BLACK, WHITE, GREEN
from setup import WIDTH, HEIGHT, FPS



class Striker:
    """
    Player class
    """
    # Take the initial position, dimensions, speed, color of the object
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        # Rect: used to control position & collision of object
        self.rect_paddle = pg.Rect(posx, posy, width, height)
        # Object that is blit on the screen
        self.paddle = pg.draw.rect(screen, self.color, self.rect_paddle)