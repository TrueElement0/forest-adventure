# Player module
# Mason Kury

import pygame


def get_frames(spritesheet, strip_rect, frame_width):
    """
    creates a list of pygame surfaces each containing a frame of an animation strip.

    Parameters:
        spritesheet: must be of type pygame.surface; the spritesheet containing all objects and entity frames.
        strip_rect: must be tuple of length 4 with elements (x, y, width, height);
                    the rectangle containing all the frames of the animation strip.
        frame_width: must be int; the width of one frame in the animation strip.

    Returns: list with elements of type pygame.Surface; the list of animation strip frames.
    """
    # calculate the number of frames by getting the number of frames accross, and multiplying by the number of frames
    # down. (in an animation strip, the number of frames down would just be one.)
    num_frames = (strip_rect[2] // frame_width) * strip_rect[3] // frame_width

    # create a list of pygame rectangles based on the number of frames
    frame_rects = [pygame.Rect(strip_rect[0] + frame_width * x, strip_rect[1], frame_width, frame_width)
                   for x in range(num_frames)]

    frames = []  # initialize an empty list to hold the final surface frames

    # go through each 'frame' to be made
    for current_frame in range(num_frames):
        frame = pygame.Surface(frame_rects[current_frame].size, pygame.SRCALPHA)  # create a surface with the right size
        frame.blit(spritesheet, (0, 0), frame_rects[current_frame])               # blit the image from the spritesheet
                                                                                  # onto the surface
        frames.append(frame)                                                      # add the frame to the list of frames

    return frames  # return the list of frames


class Inventory:
    """
    An inventory class used to manage the player's items.

    Created Attributes:
        sword: the number of swords the player has.
        gold: the amount of gold the player has.

        current_item: the current item the player has equipped.

        inventory_dict: a dictionary allowing easy access to the player's inventory.
    """

    def __init__(self):
        """Initializes the inventory object, and defines some attributes for items to start out with."""
        self.sword = 1
        self.gold = 0
        self.current_item = "sword"

        self.inventory_dict = {"sword": self.sword, "gold": self.gold}

    def add(self, item, number):
        """
        Adds an item(s) to the player's inventory.

        Parameters:
            item: must be string; the item to add.
            number: must be int; the number of items to add.

        Returns: (none)
        """
        self.inventory_dict[item] = number  # add the item(s) to the inventory_dict

    def delete(self, item):
        """
        Deletes all of an item from the player's inventory.

        Parameters:
            item: must be string; the item to delete.

        Returns: (none)
        """

        # check if the item exists in the inventory
        if item in self.inventory_dict:
            del self.inventory_dict[item]  # remove the item(s)
        else:
            print("ERROR: CAN'T DELETE ITEM; ITEM NOT IN INVENTORY")

    def remove(self, item, number):
        """
        removes an item(s) from the player's inventory.

        Parameters:
            item: must be string; the item to remove.
            number: must be int; the number of items to remove.

        Returns: (none)
        """

        # check to see if the item exists in the inventory
        if item in self.inventory_dict:
            if self.inventory_dict[item] - number > 0:  # if there is enough of the item to remove,
                self.inventory_dict[item] -= number     # remove the number of items
            else:
                self.delete(item)  # otherwise there were enough removed to delete the item altogether
        else:
            print("ERROR: CAN'T REMOVE ITEM; ITEM NOT IN INVENTORY")

    def set_item(self, number):
        """
        Sets the current item for the player to have equipped, based off of a number from the HUD

        Parameters:
            number: must be int; the number corresponding to the item to switch to.

        Returns: (none)
        """
        current_pos = 0

        # go through all the items in the inventory
        for key in self.inventory_dict.keys():

            # if the current position matches the number
            if current_pos == number - 1:
                # and the item in the position exists and is equippable:
                if key in ("sword", "bow", "potion"):
                    self.current_item = key  # set the current item to the item in the current position
                    break
            else:
                current_pos += 1


class Arrow:
    """
    DOC
    """
    def __init__(self, move_speed, x, y, direction):
        """DOC"""
        self.move_speed = move_speed
        self.direction = direction

        if self.direction == "up" or self.direction == "down":
            self.hitbox = pygame.Rect(x, y, 5, 32)
        elif self.direction == "left" or self.direction == "right":
            self.hitbox = pygame.Rect(x, y, 23, 5)

    def move(self):
        """
        DOC
        """
        if self.direction == "up":
            self.hitbox.y -= self.move_speed
        elif self.direction == "down":
            self.hitbox.y += self.move_speed
        elif self.direction == "left":
            self.hitbox.x -= self.move_speed
        elif self.direction == "right":
            self.hitbox.x += self.move_speed

    def draw(self):
        """
        DOC
        """


class Player:
    """
    A player class used to create a player with an inventory, health, animations, move speed, etc.

    Attributes:
        move_speed:     must be int; the move speed of the player.
        dodge_distance: must be int; the number of pixels the player moves when he dodges.

        hitbox:      must be of type pygame.Rect; the hitbox of the player.
        sword_swing: must be of type pygame.Rect; the area the player can hit with his sword.

        direction: must be string with value == "up", "down", "left", or "right"; the direction of the player.

        health: must be int; the current health of the player.

        animations: must be a list with list elements containing pygame.Surface objects; the animations of the player
                    and the frames of the animation strips.

    Created Attributes:
        swing_x_offset: the x offset used to center the sword swing hitbox.
        swing_y_offset: the y offset used to center the sword swing hitbox.

        current_frame: the current frame of the player's animation.
        total_frames: the total number of frames in the player's animations.

        inventory: an Inventory object, now tied into the player.
    """

    def __init__(self, move_speed, dodge_distance, hitbox, sword_swing, direction, health, animations):
        """Initializes the player object, and creates some other attributes used for animation and combat"""
        self.move_speed = move_speed
        self.dodge_distance = dodge_distance

        self.hitbox = hitbox
        self.sword_swing = sword_swing
        self.swing_x_offset = (self.hitbox.width // 2) - (self.sword_swing.width // 2)
        self.swing_y_offset = (self.hitbox.height // 2) - (self.sword_swing.height // 2)

        self.direction = direction

        self.health = health

        self.current_frame = 0
        self.animations = animations
        self.total_frames = len(self.animations[0])

        self.inventory = Inventory()

    def align_sword_swing(self):
        """Simply centers the sword_swing hitbox around the player's hitbox"""
        self.sword_swing.x = self.hitbox.x + self.swing_x_offset
        self.sword_swing.y = self.hitbox.y + self.swing_y_offset

    def animate(self, stop=None):
        """
        Advances the player to the next frame in the current animation, or stops the player's animation on the first
        frame if specified.

        Parameters:
            stop: (OPTIONAL) can be any value (I suggest a boolean); used to determine if the player's animation should
                  be stopped on the first frame or not.

        Returns: pygame.Surface; the next frame in the player's animation
        """

        # animate normally
        if stop is None:
            # if the end of the animation has not yet been reached, advance to the next frame
            if self.current_frame < self.total_frames - 1:
                self.current_frame += 1
            # otherwise the end has been reached, so loop back to the beginning
            else:
                self.current_frame = 0

        # stop on first frame
        else:
            self.current_frame = 0

        # if the current weapon equipped is a sword, return the sword walking animation in the appropriate direction
        if self.inventory.current_item == "sword":
            if self.direction == "up":
                return self.animations[0][self.current_frame]
            elif self.direction == "down":
                return self.animations[1][self.current_frame]
            elif self.direction == "left":
                return self.animations[2][self.current_frame]
            elif self.direction == "right":
                return self.animations[3][self.current_frame]

    def sword_attack(self, enemies_list):
        """
        DOC
        """
        if self.inventory.current_item == "sword":
            pygame.time.set_timer("sword_animation", 1/60)
            for enemy in enemies_list:
                if self.sword_swing.colliderect(enemy.hitbox):
                    enemy.damage(20)

    def bow_attack(self, arrows_list):
        """
        DOC
        """
        if self.inventory.current_item == "bow" and "arrows" in self.inventory.inventory_dict and \
                self.inventory.inventory_dict["arrows"] > 0:

            self.inventory.remove("arrows", 1)
            arrow = Arrow(5, self.hitbox.x, self.hitbox.y // 2, self.direction)
            pygame.time.set_timer("bow_animation", 1/60)
            arrows_list.append(arrow)

            return arrows_list

    def drink_potion(self):
        """
        DOC
        """
        if "potions" in self.inventory.inventory_dict and self.inventory.inventory_dict["potions"] > 0 \
                and self.health <= 4:
            self.inventory.inventory_dict["potions"] -= 1
            pygame.time.set_timer("potion_animation", 1/60)
            self.health = 5  # refill the player's health back up to 5

    def move(self):
        """
        Moves the player in the appropriate direction based off of the direction attribute, and also aligns the
        sword_swing hitbox.
        """

        # move up
        if self.direction == "up":
            self.hitbox.y -= self.move_speed
        # move down
        elif self.direction == "down":
            self.hitbox.y += self.move_speed
        # move left
        elif self.direction == "left":
            self.hitbox.x -= self.move_speed
        # move right
        elif self.direction == "right":
            self.hitbox.x += self.move_speed

        self.align_sword_swing()  # align the sword_swing hitbox

    def dodge(self):
        """
        Dodges (sort of a teleport) in teh appropriate direction based off of the direction attribute, and also aligns
        the sword_swing hitbox.
        """

        # dodge up
        if self.direction == "up":
            self.hitbox.y -= self.dodge_distance
        # dodge down
        elif self.direction == "down":
            self.hitbox.y += self.dodge_distance
        # dodge left
        elif self.direction == "left":
            self.hitbox.x -= self.dodge_distance
        # dodge right
        elif self.direction == "right":
            self.hitbox.x += self.dodge_distance

        self.align_sword_swing()  # align the sword_swing hitbox

    def collide(self, block):
        """
        Determines the appropriate movement for the player when a collision happens.

        Parameters:
             block: must be of type pygame.Rect; the block that the player has collided with.

        Returns: (none)
        """

        # if the player was moving up and the block is actually above the player, move to to the bottom of the block
        if self.direction == "up" and block.y < self.hitbox.y:
            self.hitbox.y = block.bottom
        # if the player was moving down and the block is actually below the player, move to to the top of the block
        elif self.direction == "down" and block.y > self.hitbox.y:
            self.hitbox.y = block.top - self.hitbox.height
        # if the player was moving left and the block is actually to the left of the player,
        # move to to the right of the block
        elif self.direction == "left" and block.x < self.hitbox.x:
            self.hitbox.x = block.right
        # if the player was moving right and the block is actually to the right of the player,
        # move to to the left of the block
        elif self.direction == "right" and block.x > self.hitbox.x:
            self.hitbox.x = block.left - self.hitbox.width

        self.align_sword_swing()  # align the sword_swing hitbox

class Enemy:
    """
    DOC
    """
    def __init__(self, number, enemy_type, move_speed, hitbox, sight_distance, sight_width, direction, total_frames):
        """DOC"""
        self.number = number
        self.enemy_type = enemy_type
        self.move_speed = move_speed
        self.hitbox = hitbox
        self.sight_distance = sight_distance
        self.sight_width = sight_width
        self.direction = direction

        self.current_frame = 0
        self.total_frames = total_frames

        self.sight_rect = None
        self.align_sight()

    def align_sight(self):
        """
        DOC
        """

        center_x = self.hitbox.x + (self.hitbox.width // 2)
        center_y = self.hitbox.y + (self.hitbox.height // 2)

        if self.direction == "up":
            height = self.sight_distance
            width = self.sight_width

            self.sight_rect = pygame.Rect(center_x - (width // 2), self.hitbox.y - height, width, height)

        elif self.direction == "down":
            height = self.sight_distance
            width = self.sight_width

            self.sight_rect = pygame.Rect(center_x - (width // 2), self.hitbox.y + self.hitbox.height, width, height)

        elif self.direction == "left":
            width = self.sight_distance
            height = self.sight_width

            self.sight_rect = pygame.Rect(self.hitbox.x - width, center_y - (height // 2), width, height)

        elif self.direction == "right":
            width = self.sight_distance
            height = self.sight_width

            self.sight_rect = pygame.Rect(self.hitbox.x + self.hitbox.width, center_y - (height // 2), width, height)

    def animate(self, screen, frames_list, stop=None):
        """
        DOC
        """
        if stop is not None:
            if self.current_frame <= self.total_frames:
                self.current_frame += 1
            else:
                self.current_frame = 0

        else:
            self.current_frame = 0

        screen.blit(frames_list[self.current_frame])

    def move(self, path=None):
        """
        DOC
        """
        if path is not None:
            self.direction = path[0]
            del path[0]

        self.align_sight()

        if self.direction == "up":
            self.hitbox.y -= self.move_speed
        elif self.direction == "down":
            self.hitbox.y += self.move_speed
        elif self.direction == "left":
            self.hitbox.x -= self.move_speed
        elif self.direction == "right":
            self.hitbox.x += self.move_speed

    def chase(self, player):
        """
        DOC
        """
        x_distance = player.hitbox.x - self.hitbox.x
        y_distance = player.hitbox.y - self.hitbox.y
