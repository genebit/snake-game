import pygame
import sys

window = pygame.display.set_mode((400, 400))

snake = [None, None, None]

def draw_snake():
    snake_x_update = 300

    for i in range(0, len(snake)):
        
        snake[i] = pygame.Rect(snake_x_update, window.get_height()/2, 30, 30)
        snake_x_update -= 30   

        pygame.draw.rect(window, (255, 255, 255), snake[i], 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Grow
                snake.append(None)

    window.fill((30, 30, 30))

    draw_snake()

    pygame.display.update()
    
