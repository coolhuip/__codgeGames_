import pygame as pg


pg.init()

# Font that is used to render the text
font20 = pg.font.Font('freesansbold.ttf', 20)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
# Used to adjust the frame rate
clock = pg.time.Clock()
FPS = 30

z = pg.Rect(1, 1, 1, 1)
x = pg.draw.rect(screen, GREEN, z)
print(type(z))
print(type(x))