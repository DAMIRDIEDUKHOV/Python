import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Iron Man")

# Load the image of Iron Man
iron_man_image = pygame.image.load("iron_man.png")  # Replace "iron_man.png" with the path to your Iron Man image

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw Iron Man on the screen
    screen.blit(iron_man_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
