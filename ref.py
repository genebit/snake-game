import pygame
from pygame.locals import *

def draw_grid():
    screen.fill(BLACK)
    for y in range(height, h, height):#horizontal lines
        pygame.draw.line(screen, bg, (width, y), (w - width, y), 1)
    for x in range(width, w, width):#vertical lines
        pygame.draw.line(screen, bg, (x, height), (x, h - height), 1)

def draw_player():
    pygame.draw.rect(screen, [255, 255, 55], [left, top, width, height], 0)

pygame.init()
clock = pygame.time.Clock()
w = 1008
h = 640
left = 16
top = 16
width = 16
height = 16
YELLOW = (255, 255, 55)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
bg = (255, 255, 255)
x = 0
y = 0
screen = pygame.display.set_mode((w, h))
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                top += 16
            if event.key == K_UP:
                top -= 16
            if event.key == K_RIGHT:
                left += 16
            if event.key == K_LEFT:
                left -= 16

    draw_grid()
    draw_player()
    pygame.display.flip()

pygame.quit()