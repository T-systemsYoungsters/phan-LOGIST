# Lab 6

http://programarcadegames.com/index.php?chapter=lab_loopy_lab&lang=de

1. Part 1
```python
x = 10
for row in range(9):
    for column in range(row+1):
        print(x, end=" ")
        x += 1
    print("")
```
2. Part 2
```python
x = int(input("How big should the box be?"))
for row in range(x):
    for column in range(2*x):
        if row == 0 or row == x-1 or column == 0 or column == 2*x-1:
            print("o", end="")
        else:
            print(" ", end="")        
    print("")
```
3. Part 3
```python
x = int(input("How big should the box be?")) # Zahlen 0 - 6 sind möglich TODO Zahlen größer als 6 Siehe Chapter 20 Formatting

for row in range(x):
    for column in range(2*x):
        if 2*row < column:
            if column%2 == 1:
                print(column, end="")
            else:
                print(" ", end="")

    for space in range(2*row):
        print(" ", end=" ")   
           
    for column in range(2*x):
        if (2*x)-(2*row) > column:
            if column%2 == 1:
                print(2*x-column, end="")
            else:
                print(" ", end="")

    print("")

for row in range(x):
    for column in range(2*x):
        if 2*x-2*(row+1) < column:
            if column%2 == 1:
                print(column, end="")
            else:
                print(" ", end="")

    for space in range(2*x-row,row+2,-1):
        print(" ", end=" ")  
    
    for column in range(2*x):
        if 2*row >= column-1:
            if column%2 == 1:
                print(2*x-column, end="")
            else:
                print(" ", end="")
    print("")
```
4. Part 4
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
    for row in range(0,700,10):
        for column in range(0,500,10):
            pygame.draw.rect(screen, GREEN, [row, column, 5,5])
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
```
