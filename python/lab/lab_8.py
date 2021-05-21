# Import a library of functions called 'pygame'
import pygame
import math
import random
 
# Initialize the game engine
pygame.init()
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY = (95, 198, 245)
GRASS = (98, 173, 83)
CAROUSEL = (124, 119, 128)
rect_x = 300
circle_x = 400
circle_y = 600
# vector
rect_move = 3
circle_move_x = 5
circle_move_y = 10
 
PI = 3.141592653
 
# Set the height and width of the screen
size = [1600, 900]
screen = pygame.display.set_mode(size)
 
my_clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
 
angle = 2 * PI
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Set the screen background
    screen.fill(SKY)

    pygame.draw.rect(screen, GRASS, [0, 600, 1600, 300])

    pygame.draw.circle(screen, CAROUSEL, [10, 400], 130, 5)
    pygame.draw.line(screen, CAROUSEL, [10,400], [10,270], 3)
    pygame.draw.line(screen, CAROUSEL, [10,400], [10,530], 3)
    pygame.draw.line(screen, CAROUSEL, [10,400], [130,400], 3)
    pygame.draw.line(screen, CAROUSEL, [10,400], [-100,400], 3)
    
    # moving rect
    pygame.draw.rect(screen, RED, [rect_x,300,300,300])
    rect_x = rect_x + rect_move
    if rect_x > 1300 or rect_x < 0:
        rect_move = rect_move * -1

    # moving circle 
    pygame.draw.circle(screen, BLUE, [circle_x, circle_y], 150, 30)
    circle_x = circle_x + circle_move_x
    circle_y = circle_y + circle_move_y
    if circle_x > 1450 or circle_x < 150:
        circle_move_x = circle_move_x * -1
    if circle_y > 750 or circle_y < 150:
        circle_move_y = circle_move_y * -1
        


    # Zeiger
    x = 125 * math.sin(angle) + 145
    y = 125 * math.cos(angle) + 145
    pygame.draw.line(screen, BLACK, [145, 145], [x, y], 2)
    angle = angle - .03
    if angle < 0:
        angle = angle + 2 * PI
 
    # Flip the display, wait out the clock tick
    pygame.display.flip()
    my_clock.tick(120)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
"""
Move an item across the screen.
Move an item back and forth.
Move up/down/diagonally.
Move in circles.
Have a person wave his/her arms.
Create a stoplight that changes colors.
"""
pygame.quit()