import pygame
import os

pygame.init()

# Set up the display
win = pygame.display.set_mode((1080, 600))

# Load images
back = pygame.image.load(os.path.join('img', 'back2.webp'))
course = pygame.image.load(os.path.join('img', 'course.png'))
course1 = pygame.transform.scale(course, (200, 200))

# Function to render the main screen with the background and course image
def renderScreen():
    surf = pygame.Surface((1080, 600))
    surf.blit(back, (0, 0))
    surf.blit(course1, (440, 240))  # Position the course image at (440, 240)
    
    win.blit(surf, (0, 0))
    pygame.display.update()

# Main loop to keep the window open and render the images
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    renderScreen()

pygame.quit()

