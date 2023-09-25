import pygame, random
from pygame.locals import *

def onGridRandom():
    x = random.randint(0,60)
    y = random.randint(0,60)
    return (x * 10, y * 10)

def colission(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 210), (220, 200)]
snakeSkin = pygame.Surface((10, 10))
snakeSkin.fill((255, 255, 255)) 

applePos = onGridRandom()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

myDirection = LEFT
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

gameOver = False
while not gameOver:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and myDirection != DOWN:
                myDirection = UP

            if event.key == K_LEFT and myDirection != RIGHT:
                myDirection = LEFT

            if event.key == K_DOWN and myDirection != UP:
                myDirection = DOWN

            if event.key == K_RIGHT and myDirection != LEFT:
                myDirection = RIGHT

    if colission(snake[0], applePos):
        applePos = onGridRandom()
        snake.append((0, 0))
        score = score + 1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        gameOver = True
        break

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            gameOver = True
        break

    if gameOver:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if myDirection == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if myDirection == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if myDirection == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if myDirection == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    screen.fill((0,0,0))
    screen.blit(apple, applePos)
    
    for x in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)
    
    for pos in snake:
        screen.blit(snakeSkin,pos)

    pygame.display.update()

while True:
    gameOverFont = pygame.font.Font('freesansbold.ttf', 75)
    gameOverScreen = gameOverFont.render('Game Over', True, (255, 255, 255))
    gameOverRect = gameOverScreen.get_rect()
    gameOverRect.midtop = (600 / 2, 10)
    screen.blit(gameOverScreen, gameOverRect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
