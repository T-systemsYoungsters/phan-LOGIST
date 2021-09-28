"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random

from pygame.constants import SYSTEM_CURSOR_SIZEALL
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Rectangle():
    def __init__(self):
        self.x = random.randrange(701)
        self.y = random.randrange(501)
        self.height = random.randrange(20,71,1)
        self.width = random.randrange(20,71,1)
        self.change_x = random.randrange(-3,4,1)
        self.change_y = random.randrange(-3,4,1)
        self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x,self.y,self.width,self.height])
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

class Ellipse(Rectangle):
    def __init__(self):
        super().__init__()
    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x,self.y,self.width,self.height])

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list_rect = []
for x in range(100):
    my_rect = Rectangle()
    my_list_rect.append(my_rect)

my_list_ellip = []
for x in range(100):
    my_ellip = Ellipse()
    my_list_ellip.append(my_ellip)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for x in my_list_rect:
        x.draw()
        x.move()

    for x in my_list_ellip:
        x.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()