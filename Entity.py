# Player module
# Mason Kury

import pygame


def get_frames(spritesheet, strip_rect, frame_width):
    """
    DOC
    """
    num_frames = (strip_rect.x // frame_width) * strip_rect.y // frame_width

    frame_rects = [pygame.Rect(strip_rect[0] + strip_rect[2] * x, strip_rect[1], strip_rect[2], strip_rect[3])
                   for x in range(num_frames)]

    frames = []

    for current_frame in range(num_frames):
        frame = pygame.Surface(frame_rects[current_frame].size, pygame.SRCALPHA)
        frame.blit(spritesheet, (0,0), frame_rects[current_frame])
        frames.append(frame)

    return frames


class Inventory():
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

    def __init__(self, spritesheet, move_speed, dodge_distance, hitbox, sword_swing, direction, health, total_frames):
        """DOC"""
        self.spritesheet = spritesheet
        self.move_speed = move_speed
        self.dodge_distance = dodge_distance
        self.hitbox = hitbox
        self.sword_swing = sword_swing
        self.direction = direction
        self.health = health

        self.current_frame = 0
        self.total_frames = total_frames

        self.inventory = Inventory()

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


class Enemy():
    """
    DOC
    """
