import pygame, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Game")

def random_grid():
    x = random.randint(0, 590) 
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))
direction = LEFT

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple_position = random_grid()

clock = pygame.time.Clock()

while True:

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if(event.key == K_UP):
                direction = UP
            if(event.key == K_RIGHT):
                direction = RIGHT
            if(event.key == K_DOWN):
                direction = DOWN
            if(event.key == K_LEFT):
                direction = LEFT

    if collision(snake[0], apple_position):
        apple_position = random_grid()
        snake.append((0,0))

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])


    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] -10)

    if direction == RIGHT:
        snake[0] = (snake[0][0] +10, snake[0][1])
    
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] +10)
    
    if direction == LEFT:
        snake[0] = (snake[0][0] -10, snake[0][1])

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_position)
    for position in snake:
        screen.blit(snake_skin, position)
    
    pygame.display.update()