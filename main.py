import pygame
from pygame.locals import *

# Screen init
pygame.init()
screen = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption("Breaking Bricks")
screen.fill((0, 0, 0))

# Load images
# Load brick
brick = pygame.image.load("./images/brick.png")
brick = brick.convert_alpha()
brick_rect = brick.get_rect()

# Set bricks
bricks = []
brick_gap = 5
brick_rows = 6
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols) // 2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))
# End Brick

# ball
ball = pygame.image.load("./images/football.png")
ball = ball.convert_alpha()
ball_rect = ball.get_rect()


# pad
paddle = pygame.image.load("./images/paddle.png")
paddle = paddle.convert_alpha()
paddle_rect = paddle.get_rect()
paddle_rect[1] = screen.get_height() - paddle_rect[3]

# Movement


# Main
clock = pygame.time.Clock()
game_over = False
while not game_over:
    dt = clock.tick(50)
    for b in bricks:
        screen.blit(brick, b)
    screen.blit(paddle, (paddle_rect[0], paddle_rect[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             game_over = True

    pressed = pygame.key.get_pressed()

    if pressed[K_LEFT]:
        paddle_rect[0] -= 5
    if pressed[K_RIGHT]:
        paddle_rect[0] += 5
    if paddle_rect[0] < 0:
        paddle_rect[0] = 0
    if paddle_rect[0] > (screen.get_width() - paddle_rect[2]):
        paddle_rect[0] = screen.get_width() - paddle_rect[2]
    pygame.display.update()
pygame.quit()

