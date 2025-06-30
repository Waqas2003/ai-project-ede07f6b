import pygame
import sys
import random
import time

pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600
SPEED = 10
BLOCK_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game variables
snake = [(200, 200), (220, 200), (240, 200)]
direction = 'RIGHT'
apple = (400, 300)
score = 0

# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move snake
    head = snake[0]
    if direction == 'UP':
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == 'LEFT':
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + BLOCK_SIZE, head[1])

    snake.insert(0, new_head)

    # Check collision with apple
    if snake[0] == apple:
        score += 1
        apple = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE, random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop()

    # Check collision with wall
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
        snake[0][1] < 0 or snake[0][1] >= HEIGHT):
        pygame.quit()
        sys.exit()

    # Check collision with self
    if snake[0] in snake[1:]:
        pygame.quit()
        sys.exit()

    # Draw game
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, WHITE, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (apple[0], apple[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()

    # Cap framerate
    clock.tick(SPEED)

    # Delay for smoother animation
    time.sleep(0.1)