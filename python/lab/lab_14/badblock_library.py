import block_library
import random

class BadBlock(block_library.Block):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
    def update(self):
        self.change_x = random.randrange(-1,2)
        self.change_y = 2
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 685:
            self.rect.x = 685
        if self.rect.y > 450:
            self.rect.y = -50
            self.rect.x = random.randrange(0,686)