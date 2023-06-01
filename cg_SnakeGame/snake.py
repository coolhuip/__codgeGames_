import pygame as pg     # Needed to develop the game
import random as rand   # Generate objects randomly
import time             # Time manipulation

# GLOBAL VAR's
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 460
initial_direction = 'RIGHT'

# Colors
midnight_blue = pg.Color(25, 25, 112)
mint_cream = pg.Color(245, 255, 250)
crimson_red = pg.Color(220, 20, 60)
lawn_green = pg.Color(124, 252, 0)
orange_red = pg.Color(255, 69, 0)

pg.init()   # Initialize the PyGame window
display_screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('codge_SnakeGame')   # Set title of application
game_clock = pg.time.Clock()   # Create a Clock object to set refresh rate

# Snake
snake_speed = 15   # Speed of snake
snake_position = [100, 50]   # Default position of Snake
snake_body = [   # First 4 blocks of snake body
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50],
]
snake_direction = initial_direction

# Fruit
fruit_position = [
    rand.randrange(1, (SCREEN_WIDTH // 10)) * 10,
    rand.randrange(1, (SCREEN_HEIGHT // 10)) * 10,
]
fruit_spawn = True;

# Initial Score
player_score = 0

# Functions
def display_score(
        selection,
        font_color,
        font_style: str,
        font_size: int
    ):
    """
    Display the player's score.
    ---------------------------
    Outside of this function, we defined an initial score of 0.
    display_score() does the following:
        1. 
        2. 
        3. 
        4. 
    """
    # Create Font object
    score_font_style = pg.font.SysFont(font_style, font_size)
    # Create Surface object (display)
    score_surface = score_font_style.render('Your Score: ' + str(player_score),
                                            True, font_color)
    # Create a rectangular object for text placement
    score_rectangle = score_surface.get_rect()
    # Display the text
    display_screen.blit(score_surface, score_rectangle)

def game_over():
    """
    End the game.
    """
    # Create Font object
    game_over_font_style = pg.font.SysFont('times new roman', 50)
    # Create display surface object
    game_over_surface = game_over_font_style.render(
        'Your score is: ' + str(player_score), True, crimson_red
    )
    # Create a rectangular object for text placement
    game_over_rectangle = game_over_surface.get_rect()
    # Set position of the text
    game_over_rectangle.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    # Display the text
    display_screen.blit(game_over_surface, game_over_rectangle)
    # Update the small portion of the screen
    pg.display.flip()
    # Suspend the execution of the current thread for 2 sec
    time.sleep(2)
    # Quit game
    pg.quit()
    # Quit the application
    quit()

# =============================================================================

# GAME LOOP
game_run = True
while game_run:
    # Iterate thru events in the pg.event module
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_run = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake_direction = 'UP'
            elif event.key == pg.K_DOWN:
                snake_direction = 'DOWN'
            elif event.key == pg.K_LEFT:
                snake_direction = 'LEFT'
            elif event.key == pg.K_RIGHT:
                snake_direction = 'RIGHT'
    
    # Neglect the action taken if the key of opposite direction is pressed
    if snake_direction == 'UP' and initial_direction != 'DOWN':
        initial_direction = 'UP'
    elif snake_direction == 'DOWN' and initial_direction != 'UP':
        initial_direction = 'DOWN'
    elif snake_direction == 'LEFT' and initial_direction != 'RIGHT':
        initial_direction = 'LEFT'
    elif snake_direction == 'RIGHT' and initial_direction != 'LEFT':
        initial_direction = 'RIGHT'
    
    # Update the position of the snake for every direction
    if initial_direction == 'UP':
        snake_position[1] -= 10
    if initial_direction == 'DOWN':
        snake_position[1] += 10
    if initial_direction == 'LEFT':
        snake_position[0] -= 10
    if initial_direction == 'RIGHT':
        snake_position[0] += 10
    
    # Update snake's body
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        player_score += 1
        fruit_spawn = False
    else:
        snake_body.pop()
    

    # Spawn fruit randomly
    if not fruit_spawn:
        fruit_position = [
            rand.randrange(1, (SCREEN_WIDTH // 10)) * 10,
            rand.randrange(1, (SCREEN_HEIGHT // 10)) * 10
        ]
    fruit_spawn = True

    # Fill color on screen
    display_screen.fill(mint_cream)

    # Draw the game objects on screen
    for pos in snake_body:
        pg.draw.rect(display_screen, lawn_green, pg.Rect(pos[0], pos[1], 10, 10))
        pg.draw.rect(display_screen, orange_red, pg.Rect(fruit_position[0], fruit_position[1], 10, 10))
    
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > SCREEN_WIDTH - 10:
        game_over()
    elif snake_position[1] < 0 or snake_position[1] > SCREEN_HEIGHT - 10:
        game_over()
    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

     # Display the score continuously
    display_score(1, midnight_blue, 'times new roman', 20)

    # Refresh the game screen
    pg.display.update()

    # Refresh rate
    game_clock.tick(snake_speed)

# QUIT THE APPLICATION
quit()