# Code Review Chapter 6 Lab Task 4

Dustin
```python
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
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
    # Green rectangles
    # Rect(x, y, width, height)
    x = 0
    y = 0
    width = 5
    height = 5
    paddingTop = width
    paddingRight = height

    x += paddingRight
    y += paddingTop

    for o in range(0, 50):
        for i in range(0, 90):
            pygame.draw.rect(screen, GREEN, pygame.Rect(x, y, width, height))
            x = x + (paddingRight * 2)
        x = 0 + paddingRight
        y = y + (paddingTop * 2)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
```

Marvin
```python
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("6.4 Part 4")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
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
    #Anfangskoordinaten
    x_rect_origin = 10
    y_rect_origin = 10
    
    for i in range(33): #Zeilen
        for j in range(46): #Spalten
            pygame.draw.rect(screen, GREEN, pygame.Rect(x_rect_origin, y_rect_origin, 10, 10)) #zeichnen des Rechtecks
            x_rect_origin = x_rect_origin + 15 #erhöhen der x Koordinate um 15 nach jedem Rechteck
        x_rect_origin = 10 #zurücksetzen der X Koordinate um die nächste Zeile wieder bei x=10 zu starten
        y_rect_origin = y_rect_origin + 15 ##erhöhen der y Koordinate/Zeilenabstand um 15 nach jeder Zeile
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
```