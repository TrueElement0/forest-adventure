# Level module used to load and manage the game screens
# Mason Kury

import pygame


class Level():
    """A level class used for making RPG 'levels' (screens) that will handle collision and interactions from the
    objects and blocks on screen.

    Attributes:
        spritesheet: must be of type pygame.image converted to a per-pixel alpha surface; the spritesheet containing
                     all the tiles, items, enemies, and player animations.

        block_width: must be int; the width (in pixels) of one column or 'block' of the spritesheet.
        sheet_width: must be int; the width (in pixels) of the entire spritesheet. (ex: an 8 column spritesheet with
                     each column 32 pixels wide would need to have a width of 256)

        bg_array: must be a two dimensional array containing all the tileset numbers for the background layer.
        fg_array: must be a two dimensional array containing all the tileset numbers for the foreground layer.

    Created Attributes:
        num_columns: the number of columns in each row of the spritesheet.

        collision_array: an array the same size as the fg and bg arrays, corresponding to different types
                         of collision blocks.
    """

    def __init__(self, spritesheet, block_width, sheet_width, bg_array, fg_array):
        """Initializes the level attributes, and fabricates an array of collision 'blocks' based off the blocks in
        the fg_array."""

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

                # current tile is a pathway to another screen
                if self.fg_array[row][column] == 32:
                    self.collision_array[row][column] = 4

                # current tile is a chest
                elif self.fg_array[row][column] in range(18, 22) or self.fg_array[row][column] in range(30, 32):
                    self.collision_array[row][column] = 3

                # current tile is a sign
                elif self.fg_array[row][column] in range(16, 18):
                    self.collision_array[row][column] = 2

                # special case: current tile is the bottom portion of the cave (must be non-collision)
                elif self.fg_array[row][column] in range(25, 28):
                    self.collision_array[row][column] = 0

                # current tile is just a collision block
                elif self.fg_array[row][column] not in range(4, 16) and self.fg_array[row][column] is not 0:
                    self.collision_array[row][column] = 1

                # current tile is non-collision, or is a background block
                else:
                    self.collision_array[row][column] = 0

    def get_collision_list(self):
        """
        creates a list of pygame rectangles based on the collision_list attribute.

        returns: list with elements of type pygame.Rect; the collision rectangles of the environment
        """

        list = []

        for row in range(len(self.collision_array)):
            for column in range(len(self.collision_array[0])):
                if self.collision_array[row][column] is not 0:
                    x = column * self.block_width
                    y = row * self.block_width

                    list.append(pygame.Rect(x, y, self.block_width, self.block_width))

                else:
                    list.append(None)

        return list

    def get_tile(self, number):
        """
            Gets and returns the desired block from a spritesheet, given the corresponding number.

            Parameters:
                number: must be an int no grater than the number of different blocks (tiles in the spritesheet);
                the number corresponding to the block type.

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
        """
        Draws the blocks in the background layer, based on the numbers in self.bg_array.

        Parameters:
            surface: must be of type pygame.surface; the screen  surface to blit to.

        Returns: (nothing) -- draws the background layer to the screen surface.
        """

        # get the width and height of the array
        height = len(self.bg_array)
        width = len(self.bg_array[0])

        # go through each tile in the array
        for row in range(height):
            for column in range(width):

                # get the tile that corresponds to the current position's number
                current_tile = self.get_tile(self.bg_array[row][column])

                if current_tile is not None:  # a tile is to be drawn at the current location

                    # convert the position in the array to x and y coordinates
                    x = self.block_width * column
                    y = self.block_width * row

                    surface.blit(current_tile, (x, y))  # blit the tile to the screen position

    def draw_fg(self, surface):
        """
        Draws the blocks in the foreground layer, based on the numbers in self.fg_array.

        Parameters:
            surface: must be of type pygame.surface; the screen  surface to blit to.

        Returns: (nothing) -- draws the foreground layer to the screen surface.
        """

        # get the width and height of the array
        height = len(self.fg_array)
        width = len(self.fg_array[0])

        # go through each tile in the array
        for row in range(height):
            for column in range(width):

                # get the tile that corresponds to the current position's number
                current_tile = self.get_tile(self.fg_array[row][column])

                if current_tile is not None:  # a tile is to be drawn at the current location

                    # convert the position in the array to x and y coordinates
                    x = self.block_width * column
                    y = self.block_width * row

                    surface.blit(current_tile, (x, y))  # blit the tile to the screen position


class HUD:
    """DOC"""

    def __init__(self, spritesheet, base_rect, inventory_dict, current_item, quest_text, health, boss_health=None):
        """DOC"""

        self.spritesheet = spritesheet
        self.base_rect = base_rect
        self.inventory_dict = inventory_dict
        self.current_item = current_item
        self.quest_text = quest_text
        self.health = health
        self.boss_health = boss_health

        self.hud = pygame.Surface(base_rect.size, pygame.SRCALPHA)
        self.hud.blit(spritesheet, (0, 0), base_rect)

    def draw(self, screen, coordinates):
        """DOC"""
        screen.blit(self.hud, coordinates)
