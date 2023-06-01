from setup import pg

from setup import font20, screen, clock
from setup import BLACK, WHITE, GREEN
from setup import WIDTH, HEIGHT, FPS

from paddle import Paddle
from ball import Ball


def main():
    """
    Game Manager
    """
    running = True

    player1 = Paddle(20, 0, 10, 100, 10, GREEN)
    player2 = Paddle(WIDTH-30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

    players_list = [player1, player2]

    # Initial parameters of the players
    player1_score, player2_score = 0, 0
    player1_y_fac, player2_y_fac = 0, 0

    while running:
        screen.fill(BLACK)
        
        # Event handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    player2_y_fac = -1
                elif event.key == pg.K_DOWN:
                    player2_y_fac = 1
                if event.key == pg.K_w:
                    player1_y_fac = -1
                elif event.key == pg.K_s:
                    player1_y_fac = 1
            elif event.type == pg.KEYUP:
                if (event.key == pg.K_UP) or (event.key == pg.K_DOWN):
                    player2_y_fac = 0
                if (event.key == pg.K_w) or (event.key == pg.K_s):
                    player1_y_fac = 0
        
        # Collision detection
        for player in players_list:
            if pg.Rect.colliderect(ball.getRect(), player.getect()):
                ball.hit()

        # Updating the objects
        player1.update(player1_y_fac)
        player2.update(player2_y_fac)
        point = ball.update()

        # Player1 has scored --> -1
        # Player2 has scored --> +1
        # Neither player has scored --> 0
        if point == -1:
            player1_score += 1
        elif point == 1:
            player2_score += 1

        # Someone has scored a point & ball is out of bounds.
        # Now, reset the ball's position.
        if point:
            ball.reset()

        # Display objects on the screen
        player1.display()
        player2.display()
        ball.display()

        # Display the scores of the players
        player1.display_score("Player 1: ", player1_score, 100, 20, WHITE)
        player2.display_score("Player 2: ", player2_score, WIDTH-100, 20, WHITE)

        pg.display.update()
        # Adjust the frame rate
        clock.tick(FPS)


if __name__ == '__main__':
    main()
    pg.quit()