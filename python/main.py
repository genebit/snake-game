import pygame
import random

import texts

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (26 ,26, 26)
RED = (186, 45, 45)
# Window Properties
WINDOW = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake Game')
CLOCK = pygame.time.Clock()

TEXT = texts.Text(WINDOW)

# Snake
snake = pygame.Rect(250, 250, 25, 25)

snake_x_update = 0
snake_y_update = 0

# Food
x_grid = []
y_grid = []

for x in range(0, WINDOW.get_width(), 25):
    x_grid.append(x)
    for y in range(0, WINDOW.get_height(), 25):
        y_grid.append(y)        

def spawnFood(x_grid, y_grid):
    food_x_picker = random.randint(0, len(x_grid)-1)
    food_y_picker = random.randint(0, len(y_grid)-1)
    return pygame.Rect(food_x_picker, food_y_picker, 25, 25);

food = pygame.Rect(spawnFood(x_grid, y_grid))

def main():
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Movement Input
            if event.type == pygame.KEYDOWN:
                global snake_x_update, snake_y_update
                # Up
                if event.key == pygame.K_w: 
                    snake_x_update = 0
                    snake_y_update = -25
                # Left
                if event.key == pygame.K_a: 
                    snake_x_update = -25
                    snake_y_update = 0
                # Down
                if event.key == pygame.K_s: 
                    snake_x_update = 0
                    snake_y_update = 25
                # Right
                if event.key == pygame.K_d: 
                    snake_x_update = 25
                    snake_y_update = 0
                #----------------------
                # Reset
                if event.key == pygame.K_r:
                    snake.x = 250
                    snake.y = 250
                    game_over = False 
        
        if not game_over:
            snake.x += snake_x_update
            snake.y += snake_y_update

            WINDOW.fill(BLACK)
            pygame.draw.rect(WINDOW, WHITE, snake, 2)
            
            pygame.draw.rect(WINDOW, RED, food, 2)

            # Border Snake Collision Game Over
            if (snake.x < 0 or snake.x > WINDOW.get_width() or 
                snake.y < 0 or snake.y > WINDOW.get_height()):
                TEXT.show_gameover(WINDOW)
                game_over = True
            
            pygame.display.update()
            CLOCK.tick(15)

if __name__ == '__main__':
    print('Game is Running...')
    main()