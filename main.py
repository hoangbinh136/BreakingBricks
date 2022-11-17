import pygame
from pygame.locals import *

# Screen init
pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
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
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))
# End Brick

# Ball
ball = pygame.image.load("./images/football.png")
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (100, 280)
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start
# End Ball

# Pad
paddle = pygame.image.load("./images/paddle.png")
paddle = paddle.convert_alpha()
paddle_rect = paddle.get_rect()
paddle_rect[1] = screen.get_height() - 100

# End Pad

# Movement
x, y = (0, 0)

# Main
clock = pygame.time.Clock()
game_over = False
while not game_over:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))

    for b in bricks:
        screen.blit(brick, b)

    screen.blit(paddle, paddle_rect)
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        ball_served = True
    paddle_rect[0] = x

    if (paddle_rect[0] <= ball_rect[0] <= (paddle_rect[0] + paddle_rect[2]) and
            paddle_rect[1] <= ball_rect[1] + ball_rect[3] and
            sy > 0):
        sy *= -1
        sx *= 1.01
        sy *= 1.01
        continue

    # delete brick
    delete_brick = None
    for b in bricks:
        bx, by = b
        if (bx + brick_rect.width >= ball_rect[0] >= bx and
                by + brick_rect.height >= ball_rect[1] >= by):
            delete_brick = b

            if ball_rect[0] <= bx + 2:
                sx *= -1
            elif ball_rect[0] >= bx + brick_rect.width - 2:
                sx *= -1
            if ball_rect[1] <= by +2:
                sy *= -1
            elif ball_rect[1] >= by + brick_rect.height - 2:
                sy *= -1
            break
    if delete_brick is not None:
        bricks.remove(delete_brick)

    # top ball
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1

    # bottom ball
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        # ball_rect[1] = screen.get_height() - ball_rect.height
        # sy *= -1
        ball_served = False
        ball_rect.topleft = ball_start

    # left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1

    # right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1

    # start the ball

    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy

    pygame.display.update()
pygame.quit()

