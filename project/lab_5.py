import pygame
import math
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BROWN = (146,74,23)
DARK_GREEN = (10,94,11)
LIGHT_BLUE = (78,161,225)


score = 1000

size=[1600,900]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("LAB 5")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
          done = True # Flag that we are done so we exit this loop

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLUE)

    pygame.draw.rect(screen, GREEN, [0,700,1600,900])
    pygame.draw.rect(screen, LIGHT_BLUE, [300,300,800,400])
    pygame.draw.rect(screen, BROWN, [100,500,50,200])
    pygame.draw.circle(screen, DARK_GREEN, [125,425], 50)
    for leaf_offset in range(0,100,50):
        pygame.draw.circle(screen, DARK_GREEN, [100+leaf_offset,475], 50)
    for tree_offset in range(0,300,200):
        pygame.draw.rect(screen, BROWN,[1250+tree_offset,500,50,200])
        pygame.draw.circle(screen, DARK_GREEN, [1275+tree_offset,425], 50)
        for leaf_offset2 in range(0,100,50):
            pygame.draw.circle(screen, DARK_GREEN, [1250+tree_offset+leaf_offset2,475], 50)
    pygame.draw.polygon(screen, RED, [[200,300],[1200,300],[700,0]])
    for window_offset_y in range(0,250,125):
        for window_offset_x in range(0,750,125):
            pygame.draw.rect(screen,BLACK,[350+window_offset_x,350+window_offset_y,50,50])
    pygame.draw.rect(screen,WHITE , [625,600,150,100])
    pygame.draw.line(screen, BLACK, [700,600], [700,700],3)
    for door_offset in range(0,50,40):
        pygame.draw.circle(screen, BLACK, [680+door_offset,650], 3)
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)