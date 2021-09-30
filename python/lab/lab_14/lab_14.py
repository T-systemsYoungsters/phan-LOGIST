"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
import goodblock_library
import badblock_library
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 205)
GREEN = (  0, 128,   0)
 
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Border and Border hit Sound
        if self.rect.x < 0:
            self.rect.x += 15
            w_collide_sound.play()
        if self.rect.x > 685:
            self.rect.x -= 15
            w_collide_sound.play()
        if self.rect.y < 0:
            self.rect.y += 15
            w_collide_sound.play()
        if self.rect.y > 385:
            self.rect.y -= 15
            w_collide_sound.play()

# Initialize Pygame
pygame.init()

# Loading in Soundfile through Directory
collide_sound = pygame.mixer.Sound("c:\\Users\\Phan\\Documents\\phan-LOGIST\\python\\lab\\lab_14\\good_block.wav")
b_collide_sound = pygame.mixer.Sound("c:\\Users\\Phan\\Documents\\phan-LOGIST\\python\\lab\\lab_14\\bad_block.wav")
w_collide_sound = pygame.mixer.Sound("c:\\Users\\Phan\\Documents\\phan-LOGIST\\python\\lab\\lab_14\\bump.wav")

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a good block
    block = goodblock_library.GoodBlock(GREEN, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the good block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)

for i in range(50):
    # This represents a bad block
    block = badblock_library.BadBlock(RED, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the bad block to the list of objects
    bad_block_list.add(block)
    all_sprites_list.add(block)

# Create a Blue player block
player = Player(15, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # Clear the screen
    screen.fill(WHITE)
 
    # See if the player block has collided with good block.
    blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
 
    # Check the good list of collisions. and play sound
    for block in blocks_hit_list:
        score += 1
        collide_sound.play()
        print(score)
    
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
 
    # Check the bad list of collisions. and play sound
    for block in bad_blocks_hit_list:
        score -= 1
        b_collide_sound.play()
        print(score)

    # update all sprites
    all_sprites_list.update()

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("Score: "+ str(score), True, BLACK)
 
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [300, 0])
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()