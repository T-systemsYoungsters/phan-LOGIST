# Lab 10
"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
1. Create at least two different functions that draw an object to the screen. 
For example, draw_bird and draw_tree. Do not draw a stick figure, we did that one already. 
Create your own unique item. Do not simply draw a circle or rectangle. That's boring. Draw a train, or cloud, or house, T-Rex or whatever. 
But minimal work = minimal points. If you created your own object in the create-a-picture lab feel free to adapt it to this lab.
2. In Chapter 10, we talked about moving graphics with the keyboard, a game controller, and the mouse. 
Pick two of those and use them to control two different items on the screen.
3. In the case of the game controller and the keyboard, make sure to add checks so that your object does not move off-screen and get lost. 
Remember the worksheet 10 question, don't just reverse the direction like the bouncing rectangle.
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
 
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10

# Current position 2. object
x_coord2 = 100
y_coord2 = 100

# Count the joysticks the computer has
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -10
            elif event.key == pygame.K_RIGHT:
                x_speed = 10
            elif event.key == pygame.K_UP:
                y_speed = -10
            elif event.key == pygame.K_DOWN:
                y_speed = 10

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # As long as there is a joystick
    if joystick_count != 0:
 
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)
 
        # Move x according to the axis. We multiply by 10
        # to speed up the movement.
        x_coord2 = x_coord2 + int(horiz_axis_pos * 10)
        y_coord2 = y_coord2 + int(vert_axis_pos * 10)

    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    
    if x_coord < 0:
        x_coord = 0
    if x_coord > 690:
        x_coord = 690
    if y_coord < 0:
        y_coord = 0
    if y_coord > 473:
        y_coord = 473

    if x_coord2 < 0:
        x_coord2 = 0
    if x_coord2 > 690:
        x_coord2 = 690
    if y_coord2 < 0:
        y_coord2 = 0
    if y_coord2 > 473:
        y_coord2 = 473
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    draw_stick_figure(screen, x_coord, y_coord)
    draw_stick_figure(screen, x_coord2, y_coord2)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()