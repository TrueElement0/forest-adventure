# Player module
# Mason Kury

import pygame


def get_frames(spritesheet, strip_rect, frame_width):
    """
    DOC
    """
    num_frames = (strip_rect[2] // frame_width) * strip_rect[3] // frame_width

    frame_rects = [pygame.Rect(strip_rect[0] + frame_width * x, strip_rect[1], frame_width, frame_width)
                   for x in range(num_frames)]

    frames = []

    for current_frame in range(num_frames):
        frame = pygame.Surface(frame_rects[current_frame].size, pygame.SRCALPHA)
        frame.blit(spritesheet, (0, 0), frame_rects[current_frame])
        frames.append(frame)

    return frames


class Inventory:
    """
    DOC
    """

    def __init__(self):
        """DOC"""
        self.sword = 1
        self.gold = 0
        self.current_item = "sword"

        self.inventory_dict = {"sword": self.sword, "gold": self.gold}

    def add(self, item, number):
        """
        DOC
        """
        self.inventory_dict[item] = number

    def delete(self, item):
        """
        DOC
        """
        if item in self.inventory_dict:
            del self.inventory_dict[item]
        else:
            print("ERROR: CAN'T DELETE ITEM; ITEM NOT IN INVENTORY")

    def remove(self, item, number):
        """
        DOC
        """
        if item in self.inventory_dict:
            if self.inventory_dict[item] - number > 0:
                self.inventory_dict[item] -= number
            else:
                self.delete(item)
        else:
            print("ERROR: CAN'T REMOVE ITEM; ITEM NOT IN INVENTORY")

    def set_item(self, number):
        """
        DOC
        """
        current_pos = 0

        for key in self.inventory_dict.keys():

            if current_pos == number - 1:
                if key in ("sword", "bow", "potion"):
                    self.current_item = key
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
    DOC
    """

    def __init__(self, move_speed, dodge_distance, hitbox, sword_swing, direction, health, animations):
        """DOC"""
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
        """DOC"""
        self.sword_swing.x = self.hitbox.x + self.swing_x_offset
        self.sword_swing.y = self.hitbox.y + self.swing_y_offset

    def animate(self, stop=None):
        """
        DOC
        """
        if stop is None:
            if self.current_frame < self.total_frames - 1:
                self.current_frame += 1
            else:
                self.current_frame = 0

        else:
            self.current_frame = 0

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

        self.align_sword_swing()

    def dodge(self):
        """
        DOC
        """
        if self.direction == "up":
            self.hitbox.y -= self.dodge_distance
        elif self.direction == "down":
            self.hitbox.y += self.dodge_distance
        elif self.direction == "left":
            self.hitbox.x -= self.dodge_distance
        elif self.direction == "right":
            self.hitbox.x += self.dodge_distance

        self.align_sword_swing()

    def collide(self, block):
        if self.direction == "up":
            self.hitbox.y = block.bottom
        elif self.direction == "down":
            self.hitbox.y = block.top - self.hitbox.height
        elif self.direction == "left":
            self.hitbox.x = block.right
        elif self.direction == "right":
            self.hitbox.x = block.left - self.hitbox.width

        self.align_sword_swing()

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
