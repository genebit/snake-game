import pygame
import sys

FPS = 15
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snakespeed = [5, 0]
snake = pygame.Rect(0, 0, 10, 10)
snake.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

direction = 'right'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not direction == 'down':
                direction = 'up'
            if event.key == pygame.K_DOWN and not direction == 'up':
                direction = 'down'
            if event.key == pygame.K_LEFT and not direction == 'right':
                direction = 'left'
            if event.key == pygame.K_RIGHT and not direction == 'left':
                direction = 'right'

    window.fill((20, 20, 20))

    snake = snake.move(snakespeed)
    pygame.draw.rect(window, (255, 255, 255), snake, 3)

    clock.tick(FPS)
    pygame.display.update()