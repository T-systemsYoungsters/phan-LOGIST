#  Worksheet 16 
upload
http://programarcadegames.com/worksheets/show_file.php?file=worksheet_16.php&lang=de

1. Start with the program at the end of Chapter 16. Modify it so that rather than just changing the block the user clicks on, also change the blocks of the squares next to the user's click. If the user clicks on an edge, make sure the program doesn't crash and still handles the click appropriately. Paste your working program below.
```python
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
width = 20
height = 20
margin = 5

grid = [[1 for x in range(11)] for y in range(11)]
grid[1][5] = 1
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (255, 255)
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width+margin)
            row = pos[1] // (width+margin)
            # Set that location to one
            grid[row][column] *= -1
            if row > 0:
                grid[row-1][column] *= -1
            if row < 9:
                grid[row+1][column] *= -1
            if column > 0:
                grid[row][column-1] *= -1
            if column < 9:
                grid[row][column+1] *= -1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == -1:
                color = GREEN
            if grid[row][column] == 1:
                color = WHITE
            pygame.draw.rect(screen, color, [(margin+width)*column+margin, (margin+height)*row+margin,width,height])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 

```
2. Write a celebrity-finding function. \
Start with a function check_celebrity that takes an n by n matrix named grid as a parameter.\
The grid location grid[i][j] = 1 if person i knows person j and grid[i][j] = 0 otherwise.\
(Assume that grid[i][i] = 1 for every i, since every person knows him/herself.)\
A celebrity is a person who is known by everyone and does not know anyone besides him/herself. \
Write a function that given the matrix grid, prints all the celebrities.\
For example, in the following grid person 2 is a celebrity:\
```python
def check_celebrity(grid):
    list =[]
    for i in range(len(grid)):
        list.append(grid[0][i])
    for row in range(1, len(grid)):
        for column in range(len(grid)):
            if grid[row][column] == 0:
                list[column] = 0

    for w in range(len(list)):
        if list[w] == 1:
            if list == grid[w]: 
                print("Person ",w," is a celebrity.")
            else:
                list[w] = 0

    celeb = False
    j = 0
    while j < len(list) and not celeb:
        if list[j] == 1:
            celeb = True
        j += 1
    if not celeb:
        print("There is no celebrity in here.")
        

print("Test 1, Should show #2 is a celebrity.")
grid = [ [1, 1, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 0],
         [1, 0, 1, 1] ]
 
check_celebrity(grid)
 
print("Test 2, Should show no one is a celebrity.")
grid = [ [1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1],
         [0, 0, 1, 0, 0],
         [1, 0, 0, 1, 1],
         [1, 0, 0, 1, 1] ]
 
check_celebrity(grid)

print("Test 3, Should show #2 is a celebrity.")
grid = [ [1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 1, 1, 1] ]
 
check_celebrity(grid)
 
print("Test 4, Should show no one is a celebrity.")
grid = [ [1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1],
         [1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 1, 1, 1] ]
 
check_celebrity(grid)
```