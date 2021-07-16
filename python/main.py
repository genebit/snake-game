import pygame
import sys

FPS = 8
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake = pygame.Rect(100, WINDOW_HEIGHT/2, 25, 25)
x_update = 0
y_update = 0
movelength = 25
direction = 'RIGHT'

food = pygame.Rect(0, 0, 25, 25)

gameover = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not direction == 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and not direction == 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and not direction == 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and not direction == 'LEFT':
                direction = 'RIGHT'
    
    if direction == 'UP':
        x_update = 0
        y_update = -movelength
    if direction == 'DOWN':
        x_update = 0
        y_update = movelength
    if direction == 'LEFT':
        x_update = -movelength
        y_update = 0
    if direction == 'RIGHT':
        x_update = movelength
        y_update = 0
    
    window.fill((20, 20, 20))
    
    snake.x += x_update
    snake.y += y_update
    pygame.draw.rect(window, (255, 255, 255), snake, 2)
    
    clock.tick(FPS)
    pygame.display.update()