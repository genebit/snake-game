import pygame
import time
import random
 
pygame.init()
 
WHITE = (255, 255, 255)
BLACK = (26, 26, 26)
RED = (186, 45, 45)
 
WINDOW_width = 600
WINDOW_height = 400
 
WINDOW = pygame.display.set_mode((WINDOW_width, WINDOW_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 20
snake_speed = 15
 
FONT = pygame.font.SysFont("./font/Welbut.ttf", 30)
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(WINDOW, WHITE, [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
    mesg = FONT.render(msg, True, color)
    WINDOW.blit(mesg, [WINDOW_width / 6, WINDOW_height / 3])
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = WINDOW_width / 2
    y1 = WINDOW_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, WINDOW_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, WINDOW_height - snake_block) / 20.0) * 20.0
 
    while not game_over:
 
        while game_close == True:
            WINDOW.fill(BLACK)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
    
        # Border Collision
        if x1 >= WINDOW_width or x1 < 0 or y1 >= WINDOW_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        WINDOW.fill(BLACK)
        
        # Food
        pygame.draw.rect(WINDOW, RED, [foodx, foody, snake_block, snake_block])
        
        # Snake Length process
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
        # Collision between food and snake
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WINDOW_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, WINDOW_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
 
        pygame.display.update()
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()