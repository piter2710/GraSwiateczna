import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Santa's Present Dash")

# Load images and sounds
santa_image = pygame.image.load("img/santa.png")
stick_image = pygame.image.load("img/stick.png")
trash_image = pygame.image.load("img/trash.png")
present1_image = pygame.image.load("img/present1.png")

# Game variables
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_speed = 5

present_list = []  # List to store present positions
obstacle_list = []  # List to store obstacle positions

score = 0
health = 100

# Function to spawn presents
def spawn_present():
    present_x = random.randint(0, WIDTH - 50)
    present_y = 0
    present_list.append([present_x, present_y])

# Function to spawn obstacles
def spawn_obstacle():
    obstacle_x = random.randint(0, WIDTH - 50)
    obstacle_y = 0
    obstacle_list.append([obstacle_x, obstacle_y])

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    # Spawn presents and obstacles
    if random.randint(0, 100) < 2:  # Lower probability for slower spawning
        spawn_present()
    if random.randint(0, 100) < 1:  # Lower probability for slower spawning
        spawn_obstacle()

    # Update present and obstacle positions
    for present in present_list:
        present[1] += 2  # Adjust the speed as needed (slower)
    for obstacle in obstacle_list:
        obstacle[1] += 2  # Adjust the speed as needed (slower)

    # Check for collisions
    for present in present_list:
        if (
            player_x < present[0] < player_x + 50
            and player_y < present[1] < player_y + 50
        ):
            score += 10
            present_list.remove(present)

    for obstacle in obstacle_list:
        if (
            player_x < obstacle[0] < player_x + 50
            and player_y < obstacle[1] < player_y + 50
        ):
            health -= 10
            obstacle_list.remove(obstacle)

    # Draw everything
    screen.fill(WHITE)
    screen.blit(santa_image, (player_x, player_y))

    for present in present_list:
        screen.blit(present1_image, (present[0], present[1]))

    for obstacle in obstacle_list:
        screen.blit(trash_image, (obstacle[0], obstacle[1]))

    # Display score and health
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, RED)
    health_text = font.render(f"Health: {health}%", True, RED)
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))

    # Refresh screen
    pygame.display.flip()

    # Set the frames per second
    clock.tick(FPS)

# Quit the game
pygame.quit()
