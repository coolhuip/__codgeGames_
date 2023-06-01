from setup import pg
from setup import font20, screen, clock
from setup import BLACK, WHITE, GREEN
from setup import WIDTH, HEIGHT, FPS



class Paddle:
    """
    Player class
    """
    def __init__(self, posx, posy, width, height, speed, color):
        """
        Takes the initial position, dimensions, speed, and color of the object.
        """
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

    def display(self):
        """
        Display the object on the screen.
        """
        self.paddle = pg.draw.rect(screen, self.color, self.rect_paddle)

    def update(self, y_fac):
        """
        """
        self.posy = self.posy + (self.speed * y_fac)

        # Restrict paddle to be below the top surface of screen
        if self.posy <= 0:
            self.posy = 0
        # Restrict paddle to be above the bottom surface of screen
        elif (self.posy + self.height) >= HEIGHT:
            self.posy = HEIGHT - self.height
        
        # Update rect w/ the new values
        self.rect_paddle = (self)