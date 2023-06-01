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

    def __init__(self, posx, posy, radius, speed, color) -> None:
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

    def display(self) -> None:
        self.ball = pg.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius
        )

    def update(self) -> int:
        self.posx += self.speed * self.x_fac
        self.posy += self.speed * self.y_fac

        # If the ball hits the top or bottom surfaces,
        # then the sign of y_fac is changed.
        #   -> This results in a reflection.
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.y_fac *= -1

        # If the ball touches the left wall for the first time,
        # then self.first_time = 0
        #   -> This condition is met ONLY ONCE s.t. we can avoid giving
        #      multiple points to the player.
        if self.posx <= 0 and self.first_time:
            self.first_time = 0
            return 1
        elif (self.posx >= WIDTH) and self.first_time:
            self.first_time = 0
            return -1
        else:
            return 0

    def reset(self) -> None:
        """
        Call to reset the position of the ball to the center of the screen.
        """
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.x_fac *= -1
        self.first_time = 1

    def hit(self) -> None:
        """
        Call to reflect the ball along the x-axis.
        """
        self.x_fac *= -1

    def get_rect(self) -> pg.rect.Rect:
        return self.ball
