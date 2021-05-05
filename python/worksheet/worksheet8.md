# Chapter 8

http://programarcadegames.com/worksheets/show_file.php?file=worksheet_08.php&lang=de

1. Why does using this code in the main loop not work to move the rectangle?
```python
#given code
rect_x = 50
pygame.draw.rect(screen, WHITE, [rect_x, 50, 50, 50])
rect_x += 1

#my answer
rect_x = 50 have to be outside of the loop otherwise the starting point will always be reset through the loop
```
2. The example code to bounce a rectangle used a total of four variables. What did each variable represent?
```python
#given code
if rect_y > 450 or rect_y < 0:
    rect_change_y = rect_change_y * -1
if rect_x > 650 or rect_x < 0:
    rect_change_x = rect_change_x * -
    
#my answer
rect_y is the Y Coordinate limit, rect_x will be the X Coordinate Limit
rect_change_y the variable how much the rectangle move in y
rect_change_x the variable how much the rectangle move in x
```
3. If the screen is 400 pixels tall, and the shape is 20 pixels high, at what point should the code check to see if the shape is in contact with the bottom of the screen.
```python
it should check the bottom of the screen by y>380 because of the 20 pixels high
```
4. Explain what is wrong with the following code (explain it, don't just correct the code):
```python
#given code
if rect_y > 450 or rect_y < 0:
    rect_y = rect_y * -1

#my answer
you have to change the vector so the direction where the rectangle is moving will change not the starting point. In this code it will teleport the rectangle to rect_y = -450 and will eventually coming back into the screen
```
5. A student is animating a stick figure. He creates separate variables for tracking the position of the head, torso, legs, and arms. When the figure moves to the right he adds one to each of the variables. Explain an easier way to do this that only requires one pair of x, y variables. (And no, the answer has nothing to do with a list.)
```python
use a vector variable, so every shape can use the same variable to move
```
6. When drawing a starry background, explain why it doesn't work to put code like this in the main program loop:
```python
#given code
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    pygame.draw.circle(screen, WHITE, [x, y], 2)
#my answer
it is similar to first question. the for loop in the main loop will be reset and will draw a new background every frame instead of a static one
```
7. Explain how to animate dozens of items at the same time:
```python
you can use a for loop to create dozens of items. in the loop you need a random x and y coordinate to give position for your items. then draw your items with the starting points. if the items need more variables you can also add them by some random variables
```
8. If you have a list of coordinates like the following, what code would be required to print out the array location that holds the number 33?
```python
#given code
stars = [[ 3,  4],
         [33, 94],
         [ 0,  0]]
#my answer
print(stars[1][0])
```
9. This code example causes snow to fall:
```python
#given code
# Process each snow flake in the list
for i in range(len(snow_list)):
 
    # Get the x and y from the list
    x = snow_list[i][0]
    y = snow_list[i][1]
 
    # Draw the snow flake
    pygame.draw.circle(screen, WHITE, [x, y], 2)
 
    # Move the snow flake down one pixel
    snow_list[i][1] += 1
```
So does the example below. Explain why this example works as well.
```python
#given code
# Process each snow flake in the list
for i in range(len(snow_list)):
 
    # Draw the snow flake
    pygame.draw.circle(screen, WHITE, snow_list[i], 2)
 
    # Move the snow flake down one pixel
    snow_list[i][1] += 1
```
```python
#my answer 
it will only work the same if each entry has to in the list has exactly 2 numbers. - snow_list[i] will give an array entry of to numbers for the position similiar to x = snow_list[i][0] and y = snow_list[i][1]. Exampt that the first code the snow_list entries can have more than 2 numbers per entry.
```
10. Take a look at the radar_sweep.py program. You can find this example under the ``graphics examples'' subsection on the examples page. The radar_sweep.py is near the end of that list. Explain how this program animates the sweep to go in a circle.
```python
"""
 Show how to do a radar sweep.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
# Import a library of functions called 'pygame'
import pygame
import math
 
# Initialize the game engine
pygame.init()
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
PI = 3.141592653
 
# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)
 
my_clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
 
angle = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Set the screen background
    screen.fill(WHITE)
 
    # Dimensions of radar sweep
    # Start with the top left at 20,20
    # Width/height of 250
    box_dimensions = [20, 20, 250, 250]
 
    # Draw the outline of a circle to 'sweep' the line around
    pygame.draw.ellipse(screen, GREEN, box_dimensions, 2)
 
    # Draw a black box around the circle
    pygame.draw.rect(screen, BLACK, box_dimensions, 2)
 
    # Calculate the x,y for the end point of our 'sweep' based on
    # the current angle
    x = 125 * math.sin(angle) + 145
    y = 125 * math.cos(angle) + 145
 
    # Draw the line from the center at 145, 145 to the calculated
    # end spot
    pygame.draw.line(screen, GREEN, [145, 145], [x, y], 2)
 
    # Increase the angle by 0.03 radians
    angle = angle + .03
 
    # If we have done a full sweep, reset the angle to 0
    if angle > 2 * PI:
        angle = angle - 2 * PI
 
    # Flip the display, wait out the clock tick
    pygame.display.flip()
    my_clock.tick(60)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
```
```python
the endpoint of the pointer is dependent on an angle variable. so by changing the angle variable the endpoint will move in a circle. and if the angle goes a full circle then the angle will be resetted to 0
```