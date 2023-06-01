from setup import pg
from setup import font20, screen, clock
from setup import BLACK, WHITE, GREEN
from setup import WIDTH, HEIGHT, FPS


class Paddle:
    """
    Player class
    ------------
    NOTE: doc types assume that pygame has been imported as pg.
    """
    posx: int
    posy: int
    width: int
    height: int
    speed: int
    color: tuple(int, int, int)
    paddle_rect: pg.rect.Rect
    paddle: pg.rect.Rect

    def __init__(self, posx, posy, width, height, speed, color) -> None:
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
        self.paddle_rect = pg.Rect(posx, posy, width, height)
        # Object that is blit on the screen
        self.paddle = pg.draw.rect(screen, self.color, self.paddle_rect)

    def display(self):
        """
        Display the object on the screen.
        """
        self.paddle = pg.draw.rect(screen, self.color, self.paddle_rect)

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
        self.paddle_rect = (self.posx, self.posy, self.width, self.height)

    def display_score(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)

        screen.blit(text, text_rect)

    def get_rect(self):
        return self.paddle_rect