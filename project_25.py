# Space invaders game
import pygame # type: ignore
import random
import math

# Initialize
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')  # use your icon
pygame.display.set_icon(icon)

# Background
bg = pygame.image.load('background.jpg')  # use your background image

# Player
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for _ in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)

# Bullet
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"  # "ready" - can fire, "fire" - bullet is moving

# Score
score = 0
font = pygame.font.Font(None, 32)

# Collision
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)
    return distance < 27

# Draw Player
def player(x, y):
    screen.blit(player_img, (x, y))

# Draw Enemy
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

# Fire Bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

# Show Score
def show_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keydown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

        # Keyup
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_x_change = 0

    player_x += player_x_change
    player_x = max(0, min(player_x, 736))

    # Enemy movement
    for i in range(num_of_enemies):
        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] <= 0 or enemy_x[i] >= 736:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]

        # Collision
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    player(player_x, player_y)
    show_score()
    pygame.display.update()
