# Lab 10
"""
Make sure this program is created in its own directory. 
If you are starting from the template I have at BitBucket, then make sure you start in the 
“Lab 11 - Bitmapped Graphics and User Control” folder and put everything in there.

Incorporate at least one function that draws an item on the screen. 
The function should take position data that specifies where to draw the item. 
(Note: You will also need to pass a reference to the “screen.” 
Another note, this is difficult to do with images loaded from a file. 
I recommend doing this only with regular drawing commands.)

Add the ability to control an item via mouse, keyboard, or game controller.

Include some kind of bit-mapped graphics. Do not include bit-mapped graphics as part of your 
“draw with a function.” That won't work well until we've learned a bit more.

Include sound. You could make a sound when the user clicks the mouse, hits a key, 
moves to a certain location, etc. If the sound is problematic, 
try using the program Audacity to load the sound, and then export it as a .ogg file.

Make sure all files are added to version control. It is easy to forget to add 
the images and sound files. Double check the website to make certain the files are added. 
If instead you need to send the program to someone, the entire directory must be zipped. See Figure 32.2. 
You do NOT need to do this if you are turning in your program using BitBucket or some other version control system.

Stop. Did you double check that all the files needed are uploaded?

Triple-check that your image and sound files are uploaded or zipped up. 
(If you are e-mailing your program, zip the files. If you are using version control with SourceTree or similar, 
then don't zip them, just make sure they get added to version control.) Even with a double-check about 25% of students seem to miss the files. 
Ask if you aren't sure. If you are using Bitbucket, make sure you can see those sound and graphic files in your lab folder on Bitbucket.
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, WHITE, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, WHITE, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, WHITE, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
 
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [800, 600]
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

# Load Sound
click_sound = pygame.mixer.Sound("c:\\Users\\Phan\\Documents\\phan-LOGIST\\python\\lab\\lab_11\\laser5.ogg")

# load Graphic
background_position = [0, 0]
background_image = pygame.image.load("c:\\Users\\Phan\\Documents\\phan-LOGIST\\python\\lab\\lab_11\\saturn_family1.jpg").convert()
 
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
        # Sound for Mousebutton Down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
 
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
    screen.blit(background_image, background_position)
 
    draw_stick_figure(screen, x_coord, y_coord)
    draw_stick_figure(screen, x_coord2, y_coord2)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()