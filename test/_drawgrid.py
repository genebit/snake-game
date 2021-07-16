
import pygame
import random
import sys

window_width = 400
window_height = 400

screen = pygame.display.set_mode((window_width, window_height))

def draw_grid():
    for x in range(0, window_width, 25):
        for y in range(0, window_height, 25):
            rect = pygame.Rect(x, y, 25, 25)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_grid()
    
    pygame.display.update()