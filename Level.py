# Level module used to load and manage the game screens
# Mason Kury

import pygame


class Level():
    """DOC"""

    def __init__(self, spritesheet, block_width, sheet_width, bg_array, fg_array):
        """DOC"""

        self.spritesheet = spritesheet

        self.block_width = block_width
        self.num_columns = sheet_width // block_width

        self.bg_array = bg_array
        self.fg_array = fg_array

        # create an empty array equal to the size of the other arrays, that will store invisible collision data
        self.collision_array = [[0 for column in range(len(self.fg_array[0]))] for row in range(len(self.fg_array))]

        # set up the collision tiles based on the foreground tiles of the level object
        for row in range(len(self.collision_array)):
            for column in range(len(self.collision_array[0])):

                # current tile is an interactive tile (chest or sign)
                if self.fg_array[row][column] in range(16, 22) or self.fg_array[row][column] in (30, 31):
                    self.collision_array[row][column] = 2

                # current tile is just a collision block
                elif self.fg_array[row][column] not in range(4, 12) and self.fg_array[row][column] is not 0:
                    self.collision_array[row][column] = 1

                # current tile is non-collision, or is a background block
                else:
                    self.collision_array[row][column] = 0

    def get_tile(self, number):
        """
            Gets and returns the desired block from a spritesheet, given the corresponding number.

            Parameters:
                sheet: must be an object of the Spritesheet class; the spritesheet containing the blocks.

                width:  must be an int equal to the width of a column; the width of the block.
                height: must be an int equal to the height of a row; the height of the block.

                num: must be an int no grater than the number of different blocks; the number corresponding to the block type.

                columns: must be an int equal to the number of columns in the spritesheet; the number of columns in the sheet.

            Returns: pygame.surface with size equal to width and height; the image of the block
            """
        # Any number != 0 corresponds to a block type
        if number != 0:
            # Create a rectangle with x and y coordinates at the top left hand corner of the desired block
            # (found by dividing the (number - 1) by the number of columns to get the number of rows down,
            # and using the remainder to get the number of columns over) and width and height equal to the
            # width and height parameters.
            rectangle = pygame.Rect((number - 1) % self.num_columns * self.block_width,
                                    (number - 1) // self.num_columns * self.block_width,
                                    self.block_width, self.block_width)

            image = pygame.Surface(rectangle.size, pygame.SRCALPHA)
            image.blit(self.spritesheet, (0,0), rectangle)

            return image

        # Numbers == 0 are nothing, and should not be blitted to the screen
        else:
            return None  # Don't return an image

    def draw_bg(self, surface):
        """DRAWS THE BACKGROUND ARRAY AS THE CORRESPONDING BLOCKS"""

        height = len(self.bg_array)
        width = len(self.bg_array[0])

        for row in range(height):
            for column in range(width):

                current_tile = self.get_tile(self.bg_array[row][column])

                if current_tile is not None:

                    x = self.block_width * column
                    y = self.block_width * row

                    surface.blit(current_tile, (x, y))

    def draw_fg(self, surface):
        """DRAWS THE FOREGROUND ARRAY AS THE CORRESPONDING BLOCKS"""

        height = len(self.fg_array)
        width = len(self.fg_array[0])

        for row in range(height):
            for column in range(width):

                current_tile = self.get_tile(self.fg_array[row][column])

                if current_tile is not None:

                    x = self.block_width * column
                    y = self.block_width * row

                    surface.blit(current_tile, (x, y))
