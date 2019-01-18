# Player module
# Mason Kury

import pygame
import math


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
    # calculate the number of frames by getting the number of frames across, and multiplying by the number of frames
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

    if len(frames) > 1:
        return frames  # return the list of frames
    else:
        return frames[0]  # return only the one singular frame

def get_image(spritesheet, frame_rect):
    """
    Acts as a get_frames() function but for only one, singular, image.

    Parameters:
        spritesheet: must be of type pygame.Surface; the spritesheet to get images from
        frame_rect: must be of type pygame.Rect; the frame size and location of the image

    Returns: pygame.Surface; the image
    """
    image = pygame.Surface(frame_rect.size, pygame.SRCALPHA)
    image.blit(spritesheet, (0, 0), frame_rect)

    return image


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

    def sort(self):
        """Sorts the player's inventory based on the order of 'sword', 'bow', 'health potion', 'arrows', 'gold'"""
        # will hold the new inventory
        sorted_inventory = {}

        if "sword" in self.inventory_dict:
            sorted_inventory["sword"] = self.inventory_dict["sword"]
        if "bow" in self.inventory_dict:
            sorted_inventory["bow"] = self.inventory_dict["bow"]
        if "health potion" in self.inventory_dict:
            sorted_inventory["health potion"] = self.inventory_dict["health potion"]
        if "arrows" in self.inventory_dict:
            sorted_inventory["arrows"] = self.inventory_dict["arrows"]
        if "gold" in self.inventory_dict:
            sorted_inventory["gold"] = self.inventory_dict["gold"]

        self.inventory_dict = sorted_inventory  # set the new sorted inventory as the current one

    def add(self, item, number):
        """
        Adds an item(s) to the player's inventory.

        Parameters:
            item: must be string; the item to add.
            number: must be int; the number of items to add.

        Returns: (none)
        """
        if item in self.inventory_dict:
            self.inventory_dict[item] += number  # add the item(s) to the inventory_dict
        else:
            self.inventory_dict[item] = number  # otherwise create the item in the dict and add it

        self.sort()  # sort the inventory whenever a new item is added to the end of the inventory

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

        if item == self.current_item:
            self.current_item = list(self.inventory_dict.keys())[0]

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
                if key in ("sword", "bow", "health potion"):
                    self.current_item = key  # set the current item to the item in the current position
                    break
            else:
                current_pos += 1


class Arrow:
    """
    Creates an arrow that can be shot from ranged enemies or the player
    """
    def __init__(self, image, hitbox, move_speed, x, y):
        """DOC"""
        self.move_speed = move_speed
        self.velocity_x = 0
        self.velocity_y = 0

        self.original_image = image
        self.image = image

        self.hitbox = pygame.Rect(x, y, hitbox[0], hitbox[1])

        self.hit = False

    def move(self):
        """moves the arrow with the appropriate velocities"""
        self.hitbox.x += self.velocity_x
        self.hitbox.y += self.velocity_y

    def face_target(self, target):
        """
        Calculates an angle and x/y velocities used to point an arrow toward a target point.

        Parameters:
            target: must be tuple of len(2); the target point to aim at.
        """
        change_x = target[0] - self.hitbox.x
        change_y = -1 * (target[1] - self.hitbox.y)  # y must be inverted for trig calculations because positive y
                                                     # is down on a computer monitor
        diagonal = math.sqrt(change_x**2 + change_y**2)

        # first two statements avoid division by 0
        if change_x == 0:
            if change_y < 0:
                self.face_direction("up")
                return None
            elif change_y > 0:
                self.face_direction("down")
                return None
        elif change_y == 0:
            if change_x > 0:
                self.face_direction("right")
                return None
            elif change_x < 0:
                self.face_direction("left")
                return None
        elif change_x > 0 and change_y > 0:  # angle will be in quadrant 1
            angle = math.degrees(math.asin(change_y/diagonal))
        elif change_x < 0 and change_y > 0:  # angle will be in quadrant 2
            angle = 180 - math.degrees(math.asin(change_y/diagonal))
        elif change_x < 0 and change_y < 0:  # angle will be in quadrant 3
            angle = 180 + math.degrees(math.atan(change_y/change_x))
        else:  # angle will be in quadrant 4
            angle = 360 - math.degrees(math.acos(change_x/diagonal))

        self.image = pygame.transform.rotate(self.original_image, angle)

        # basically create a scaled down triangle with the same angles as the angular triangle, but this time
        # it is for x and y velocities.
        self.velocity_x = (self.move_speed/diagonal) * change_x
        self.velocity_y = (self.move_speed/diagonal) * change_y * -1  # y velocity must be inverted because positive y
                                                                      # is down on a computer monitor

    def face_direction(self, direction):
        """
        Points the arrow toward a given direction.

        Parameters:
            direction: must be string in ("up", "down", "left", "right"); the direction the arrow is to face.
        """
        if direction == "up":
            self.image = pygame.transform.rotate(self.original_image, 90)
            self.velocity_y = -1 * self.move_speed
            self.velocity_x = 0
        elif direction == "left":
            self.image = pygame.transform.rotate(self.original_image, 180)
            self.velocity_x = -1 * self.move_speed
            self.velocity_y = 0
        elif direction == "down":
            self.image = pygame.transform.rotate(self.original_image, 270)
            self.velocity_y = self.move_speed
            self.velocity_x = 0
        else:
            self.image = self.original_image
            self.velocity_x = self.move_speed
            self.velocity_y = 0

    def draw(self, surface):
        """
        DOC
        """
        surface.blit(self.image, (self.hitbox.x, self.hitbox.y))


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
        self.can_dodge = True
        self.can_use_item = True

        self.hitbox = hitbox
        self.sword_swing = sword_swing
        self.swing_x_offset = (self.hitbox.width // 2) - (self.sword_swing.width // 2)
        self.swing_y_offset = (self.hitbox.height // 2) - (self.sword_swing.height // 2)

        self.direction = direction

        self.health = health
        self.total_health = health
        self.dead = False
        self.respawning = False

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
        elif self.inventory.current_item == "bow":
            if self.direction == "up":
                return self.animations[4][self.current_frame]
            elif self.direction == "down":
                return self.animations[5][self.current_frame]
            elif self.direction == "left":
                return self.animations[6][self.current_frame]
            elif self.direction == "right":
                return self.animations[7][self.current_frame]
        else:
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
        Attacks any enemy within the sword swing area.

        Parameters:
            enemies_list: must be list with elements from Enemy class; the enemies on the current screen.
        """
        for enemy in enemies_list:
            if self.sword_swing.colliderect(enemy.hitbox):
                enemy.damage(1)

    def bow_attack(self,arrow_image, arrows_list):
        """
        Fires an arrow in the player's current direction.

        Parameters:
            arrow_image: must be of type pygame.Surface; the image to blit when drawing the arrow.
            arrows_list: must be list with elements from Arrow class; the player's arrows currently on the screen.
        """
        # if the player has arrows in their inventory
        if "arrows" in self.inventory.inventory_dict and self.inventory.inventory_dict["arrows"] > 0:
            # remove an arrow, and create an Arrow object, facing the player's direction
            self.inventory.remove("arrows", 1)
            arrow = Arrow(arrow_image, (32, 32), 15, self.hitbox.x, self.hitbox.y)
            arrow.face_direction(self.direction)

            arrows_list.append(arrow)  # add the arrow to the list
        return arrows_list             # then return the updated list

    def drink_potion(self):
        """Removes a health potion from the player's inventory and replenishes all their health."""
        # if the player has a health potion in their inventory and the player has lost some health
        if "health potion" in self.inventory.inventory_dict and self.inventory.inventory_dict["health potion"] > 0 \
                and self.health < self.total_health:
            # remove a health potion and replenish health
            self.inventory.remove("health potion", 1)
            self.health = self.total_health  # refill the player's health back up to the maximum

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

    def step_back(self):
        """Similar to dodge, but only moves back a slight bit to avoid issues with signs and things."""
        # move down
        if self.direction == "up":
            self.hitbox.y += self.move_speed
        # move up
        elif self.direction == "down":
            self.hitbox.y -= self.move_speed
        # move right
        elif self.direction == "left":
            self.hitbox.x += self.move_speed
        # move left
        elif self.direction == "right":
            self.hitbox.x -= self.move_speed

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
    Creates an enemy that can be melee or ranged; all enemies have spawnpoints, but melee enemies also follow paths.

    Attributes:
        enemy_type: must be string == "melee" or "ranged"; the type of enemy.

        move_speed: must be int; the move speed of the enemy.

        hitbox_size:  must be tuple of len(2); the width and height of the hitbox.
        sight_distance: must be int; the length of the enemy's line of sight.
        sight_width: must be int; the width of the enemy's line of sight.

        direction: must be string in ("up", "down", "left", "right"); the direction the enemy is facing.

        health: must be int; the maximum health of the enemy.

        animations: must be 2 dimensional list with elements of type pygame.Surface; the animation frames for the player.

        spawnpoint:  must be tuple of len(2); the spawnpoint of the enemy.
        path_point (OPTIONAL): must be tuple of len(2); the default target path point for the enemy.

        sword_swing (OPTIONAL):  must be int; the diameter of the sword_swing hitbox.
    """
    def __init__(self, enemy_type, move_speed, hitbox_size, sight_distance, sight_width, direction, health, animations, spawnpoint, path_point=None, sword_swing=None):
        """initializes the enemy's attributes"""
        self.enemy_type = enemy_type

        self.move_speed = move_speed

        self.hitbox = pygame.Rect(spawnpoint[0], spawnpoint[1], hitbox_size[0], hitbox_size[1])
        self.health = health
        self.dead = False

        if sword_swing is not None:
            self.sword_swing = pygame.Rect(0, 0, sword_swing, sword_swing)
            self.swing_x_offset = (self.hitbox.width // 2) - (self.sword_swing.width // 2)
            self.swing_y_offset = (self.hitbox.height // 2) - (self.sword_swing.height // 2)
            self.sword_swing.x = self.hitbox.x + self.swing_x_offset
            self.sword_swing.y = self.hitbox.y + self.swing_y_offset

        self.attacking = False

        self.sight_distance = sight_distance
        self.sight_width = sight_width
        self.direction = direction

        self.current_frame = 0
        self.animations = animations
        self.total_frames = len(self.animations[0])

        self.sight_rect = None
        self.align_sight()

        self.spawnpoint = spawnpoint
        self.path = []
        if path_point is not None:
            self.path_point = path_point
            self.calculate_path(self.path_point)

    def align_sight(self):
        """Aligns the sight_rect with the center of the enemy hitbox."""
        # melee enemies will have their sight_rects aligned in with the center of the edge facing their current direciton
        if self.enemy_type == "melee":
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

        # ranged enemies will have their sight_rects aligned directly with the center of their hitboxes
        elif self.enemy_type == "ranged":
            sight_x_offset = (self.hitbox.width // 2) - (self.sight_width // 2)
            sight_y_offset = (self.hitbox.height // 2) - (self.sight_distance // 2)

            self.sight_rect = pygame.Rect(self.hitbox.x + sight_x_offset, self.hitbox.y + sight_y_offset,
                                          self.sight_width, self.sight_distance)

    def align_sword_swing(self):
        """Aligns the sword_swing hitbox with the center of the enemy."""
        self.sword_swing.x = self.hitbox.x + self.swing_x_offset
        self.sword_swing.y = self.hitbox.y + self.swing_y_offset

    def damage(self, damage):
        """
        Deals a specified amount of damage to the enemy.

        Parameters:
            damage: must be int; the amount of damage to deal to the enemy.
        """
        self.health -= damage
        if self.health <= 0:
            self.dead = True

    def calculate_path(self, target_point):
        """
        Creates a long list of steps in directions that the enemy has to follow to reach a target point.

        Parameters:
            target_point: must be tuple of len(2); the target point the enemy needs to get to.
        """
        if self.move_speed > 0:

            change_x = target_point[0] - self.hitbox.x
            change_y = target_point[1] - self.hitbox.y

            x_steps = abs(int(change_x / self.move_speed))
            y_steps = abs(int(change_y / self.move_speed))

            self.path = []  # clear the path

            # if the enemy is moving left or right, calculate the y of the path first
            if self.direction in ("up", "down"):
                for step in range(y_steps):
                    if change_y > 0:  # positive so move down
                        self.path.append("down")
                    elif change_y < 0:  # negative so move up
                        self.path.append("up")

                for step in range(x_steps):
                    if change_x > 0:  # positive, so move right
                        self.path.append("right")
                    elif change_x < 0:  # negative so move left
                        self.path.append("left")

            # if the enemy is moving left or right, calculate the x of the path first
            elif self.direction in ("left", "right"):
                for step in range(x_steps):
                    if change_x > 0:  # positive, so move right
                        self.path.append("right")
                    elif change_x < 0:  # negative so move left
                        self.path.append("left")

                for step in range(y_steps):
                    if change_y > 0:  # positive so move down
                        self.path.append("down")
                    elif change_y < 0:  # negative so move up
                        self.path.append("up")

    def animate(self, stop=None):
        """
        Advances enemy animation to the next frame.

        Parameters:
            stop (OPTIONAL): suggested use -- Boolean; when stop is not None, the next frame will always be the first,
                             starting frame of the current animation.
        """
        # animate normally
        if stop is None and self.move_speed > 0:
            # if the end of the animation has not yet been reached, advance to the next frame
            if self.current_frame < self.total_frames - 1:
                self.current_frame += 1
            # otherwise the end has been reached, so loop back to the beginning
            else:
                self.current_frame = 0
        # stop on first frame
        else:
            self.current_frame = 0

        if self.direction == "up":
            return self.animations[0][self.current_frame]
        elif self.direction == "down":
            return self.animations[1][self.current_frame]
        elif self.direction == "left":
            return self.animations[2][self.current_frame]
        elif self.direction == "right":
            return self.animations[3][self.current_frame]

    def move(self):
        """Moves the enemy in the current direction based on it's move speed."""

        if self.direction == "up":
            self.hitbox.y -= self.move_speed
        elif self.direction == "down":
            self.hitbox.y += self.move_speed
        elif self.direction == "left":
            self.hitbox.x -= self.move_speed
        elif self.direction == "right":
            self.hitbox.x += self.move_speed

        self.align_sight()
        if self.enemy_type == "melee":
            self.align_sword_swing()

    def follow_path(self):
        """Follows the calculated path."""
        # if the enemy is currently following a path
        if len(self.path) > 0:
            # set the current direction to the next step in the path, move in the direction,
            # then delete the step in the list that was just performed.
            self.direction = self.path[0]
            self.move()
            del self.path[0]
        # otherwise the enemy needs to calculate a new one
        else:
            # if the enemy is at a point other than it's spawn, calculate a path back home
            if self.hitbox.x != self.spawnpoint[0] or self.hitbox.y != self.spawnpoint[1]:
                self.calculate_path(self.spawnpoint)
            # otherwise the enemy is already home, so if it isn't a ranged enemy, calculate a path
            # to it's default path point.
            elif self.enemy_type != "ranged":
                self.calculate_path(self.path_point)

    def collide(self, block):
        """
        Determines the appropriate movement for the player when a collision happens.

        Parameters:
             block: must be of type pygame.Rect; the block that the player has collided with.

        Returns: (none)
        """

        # if the enemy was moving up and the block is actually above the enemy, move to to the bottom of the block
        if self.direction == "up" and block.y < self.hitbox.y:
            self.hitbox.y = block.bottom
        # if the enemy was moving down and the block is actually below the enemy, move to to the top of the block
        elif self.direction == "down" and block.y > self.hitbox.y:
            self.hitbox.y = block.top - self.hitbox.height
        # if the enemy was moving left and the block is actually to the left of the enemy,
        # move to to the right of the block
        elif self.direction == "left" and block.x < self.hitbox.x:
            self.hitbox.x = block.right
        # if the enemy was moving right and the block is actually to the right of the enemy,
        # move to to the left of the block
        elif self.direction == "right" and block.x > self.hitbox.x:
            self.hitbox.x = block.left - self.hitbox.width

        self.align_sight()

        if self.enemy_type == "melee":
            self.align_sword_swing()  # align the sword_swing hitbox
