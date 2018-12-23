# Main Game Screens
# Mason Kury

from Level import *
from Entity import *


def forest_entrance(screen, clock, spritesheet, player, spawnpoint):
    """SCREEN 1"""

    bg_array = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    fg_array = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3,12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,11, 0,10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,13, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [5, 5,11, 0, 0, 0, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 9, 0, 0, 0, 6, 3, 3],
        [0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [4, 4, 9, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0,10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,11, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3,14, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 9, 0, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4,15, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

    forest_entrance = Level(spritesheet, 32, 256, bg_array, fg_array)
    collision_list = forest_entrance.get_collision_list()

    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()

    current_frame = player.animate(True)

    walking_animation_timer = pygame.USEREVENT+1
    walking_movement_timer = pygame.USEREVENT+2
    check_keypresses_timer = pygame.USEREVENT+3

    pygame.time.set_timer(check_keypresses_timer, 5)

    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == walking_animation_timer:
                current_frame = player.animate()

            if event.type == walking_movement_timer:
                player.move()

            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()

                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"

                    if not arrow_keys["up"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["up"] = True

                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"

                    if not arrow_keys["down"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["down"] = True

                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"

                    if not arrow_keys["right"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["right"] = True

                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"

                    if not arrow_keys["left"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["left"] = True

                if not keys_pressed[pygame.K_UP]:
                    arrow_keys["up"] = False

                if not keys_pressed[pygame.K_DOWN]:
                    arrow_keys["down"] = False

                if not keys_pressed[pygame.K_RIGHT]:
                    arrow_keys["right"] = False

                if not keys_pressed[pygame.K_LEFT]:
                    arrow_keys["left"] = False

                if not arrow_keys["up"] and not arrow_keys["down"] \
                   and not arrow_keys["right"] and not arrow_keys["left"]:

                    pygame.time.set_timer(walking_movement_timer, 0)
                    pygame.time.set_timer(walking_animation_timer, 0)
                    current_frame = player.animate(True)

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        collided_with = player.hitbox.collidelist(collision_list)
        if collided_with is not -1:
            player.collide(collision_list[collided_with])

        screen.fill((255, 255, 255))
        forest_entrance.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        forest_entrance.draw_fg(screen)
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)
        clock.tick(60)
        pygame.display.flip()


def southwestern_forest(screen, clock, spritesheet, player, spawnpoint):
    """SCREEN 2"""

    bg_array = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    fg_array = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3,12, 5, 5, 5,13, 3, 3, 3,12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,13, 3, 3, 3,12, 5, 5, 5, 5,13, 3, 3],
        [3, 3, 7, 0,18, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 8, 4, 4, 4, 9, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0,10, 5, 5],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 8, 4, 4],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0,10, 5, 5, 5,11, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0,10, 5, 5, 5,11, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3,14, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,15, 3, 3, 3,14, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,15, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

    southwestern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    collision_list = southwestern_forest.get_collision_list()

    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()

    current_frame = player.animate(True)

    walking_animation_timer = pygame.USEREVENT + 1
    walking_movement_timer = pygame.USEREVENT + 2
    check_keypresses_timer = pygame.USEREVENT + 3

    pygame.time.set_timer(check_keypresses_timer, 5)

    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == walking_animation_timer:
                current_frame = player.animate()

            if event.type == walking_movement_timer:
                player.move()

            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()

                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"

                    if not arrow_keys["up"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["up"] = True

                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"

                    if not arrow_keys["down"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["down"] = True

                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"

                    if not arrow_keys["right"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["right"] = True

                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"

                    if not arrow_keys["left"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["left"] = True

                if not keys_pressed[pygame.K_UP]:
                    arrow_keys["up"] = False

                if not keys_pressed[pygame.K_DOWN]:
                    arrow_keys["down"] = False

                if not keys_pressed[pygame.K_RIGHT]:
                    arrow_keys["right"] = False

                if not keys_pressed[pygame.K_LEFT]:
                    arrow_keys["left"] = False

                if not arrow_keys["up"] and not arrow_keys["down"] \
                        and not arrow_keys["right"] and not arrow_keys["left"]:
                    pygame.time.set_timer(walking_movement_timer, 0)
                    pygame.time.set_timer(walking_animation_timer, 0)
                    current_frame = player.animate(True)

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        collided_with = player.hitbox.collidelist(collision_list)
        if collided_with is not -1:
            player.collide(collision_list[collided_with])

        screen.fill((255, 255, 255))
        southwestern_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        southwestern_forest.draw_fg(screen)
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)
        clock.tick(60)
        pygame.display.flip()


def eastern_forest(screen, clock, spritesheet, player, spawnpoint, has_bow):
    """SCREEN 3"""

    bg_array = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    fg_array = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3,12, 5, 5, 5, 5, 5, 5, 5, 5, 5,11, 0,10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,13, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 4, 4, 4, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 8, 4, 4, 4, 4, 4, 4, 4, 4,15, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0,10, 5, 5, 5, 5, 5, 5, 5, 5,13, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [5, 5,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,21, 0, 6, 3, 3],
        [0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [4, 4,29, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,15, 3, 3, 3,14, 9, 0, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4,15, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

    # if the player has acquired the bow and arrow, remove the blockade of rocks
    if has_bow:
        fg_array[15][2] = 11
        fg_array[16][2] = 0
        fg_array[17][2] = 4

    eastern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    collision_list = eastern_forest.get_collision_list()

    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()

    current_frame = player.animate(True)

    walking_animation_timer = pygame.USEREVENT + 1
    walking_movement_timer = pygame.USEREVENT + 2
    check_keypresses_timer = pygame.USEREVENT + 3

    pygame.time.set_timer(check_keypresses_timer, 5)

    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == walking_animation_timer:
                current_frame = player.animate()

            if event.type == walking_movement_timer:
                player.move()

            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()

                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"

                    if not arrow_keys["up"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["up"] = True

                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"

                    if not arrow_keys["down"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["down"] = True

                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"

                    if not arrow_keys["right"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["right"] = True

                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"

                    if not arrow_keys["left"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["left"] = True

                if not keys_pressed[pygame.K_UP]:
                    arrow_keys["up"] = False

                if not keys_pressed[pygame.K_DOWN]:
                    arrow_keys["down"] = False

                if not keys_pressed[pygame.K_RIGHT]:
                    arrow_keys["right"] = False

                if not keys_pressed[pygame.K_LEFT]:
                    arrow_keys["left"] = False

                if not arrow_keys["up"] and not arrow_keys["down"] \
                        and not arrow_keys["right"] and not arrow_keys["left"]:
                    pygame.time.set_timer(walking_movement_timer, 0)
                    pygame.time.set_timer(walking_animation_timer, 0)
                    current_frame = player.animate(True)

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        collided_with = player.hitbox.collidelist(collision_list)
        if collided_with is not -1:
            player.collide(collision_list[collided_with])

        screen.fill((255, 255, 255))
        eastern_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        eastern_forest.draw_fg(screen)
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)
        clock.tick(60)
        pygame.display.flip()


def northern_forest(screen, clock, spritesheet, player, spawnpoint):
    """SCREEN 4"""

    bg_array = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    fg_array = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3,12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,13, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 4, 4, 9, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 8, 4, 4, 9, 0, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,15, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 6, 3, 3,12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,11, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 6, 3, 3, 7, 0, 0,16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 6, 3, 3, 7,19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0, 6, 3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3,14, 4, 4, 4, 4, 4, 4,15, 3, 3, 7, 0, 6, 3, 3,14, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,15, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

    northern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    collision_list = northern_forest.get_collision_list()

    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()

    current_frame = player.animate(True)

    walking_animation_timer = pygame.USEREVENT + 1
    walking_movement_timer = pygame.USEREVENT + 2
    check_keypresses_timer = pygame.USEREVENT + 3

    pygame.time.set_timer(check_keypresses_timer, 5)

    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == walking_animation_timer:
                current_frame = player.animate()

            if event.type == walking_movement_timer:
                player.move()

            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()

                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"

                    if not arrow_keys["up"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["up"] = True

                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"

                    if not arrow_keys["down"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["down"] = True

                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"

                    if not arrow_keys["right"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["right"] = True

                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"

                    if not arrow_keys["left"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["left"] = True

                if not keys_pressed[pygame.K_UP]:
                    arrow_keys["up"] = False

                if not keys_pressed[pygame.K_DOWN]:
                    arrow_keys["down"] = False

                if not keys_pressed[pygame.K_RIGHT]:
                    arrow_keys["right"] = False

                if not keys_pressed[pygame.K_LEFT]:
                    arrow_keys["left"] = False

                if not arrow_keys["up"] and not arrow_keys["down"] \
                        and not arrow_keys["right"] and not arrow_keys["left"]:
                    pygame.time.set_timer(walking_movement_timer, 0)
                    pygame.time.set_timer(walking_animation_timer, 0)
                    current_frame = player.animate(True)

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        collided_with = player.hitbox.collidelist(collision_list)
        if collided_with is not -1:
            player.collide(collision_list[collided_with])

        screen.fill((255, 255, 255))
        northern_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        northern_forest.draw_fg(screen)
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)
        clock.tick(60)
        pygame.display.flip()


def western_forest(screen, clock, spritesheet, player, spawnpoint):
    """SCREEN 5"""

    bg_array = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,28,28,28, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    fg_array = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7,22,23,24, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7,25,26,27, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3,12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,11, 0, 0, 0,10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,13, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,21, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 4, 4, 4, 4, 4, 4,15, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,15, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0,10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,13, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 3, 3],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10, 5, 5, 5, 5, 5],
        [3, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,17, 0, 0, 0, 0, 0, 0, 0],
        [3, 3,14, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

    western_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    collision_list = western_forest.get_collision_list()

    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()

    current_frame = player.animate(True)

    walking_animation_timer = pygame.USEREVENT + 1
    walking_movement_timer = pygame.USEREVENT + 2
    check_keypresses_timer = pygame.USEREVENT + 3

    pygame.time.set_timer(check_keypresses_timer, 5)

    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == walking_animation_timer:
                current_frame = player.animate()

            if event.type == walking_movement_timer:
                player.move()

            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()

                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"

                    if not arrow_keys["up"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["up"] = True

                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"

                    if not arrow_keys["down"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["down"] = True

                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"

                    if not arrow_keys["right"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["right"] = True

                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"

                    if not arrow_keys["left"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["left"] = True

                if not keys_pressed[pygame.K_UP]:
                    arrow_keys["up"] = False

                if not keys_pressed[pygame.K_DOWN]:
                    arrow_keys["down"] = False

                if not keys_pressed[pygame.K_RIGHT]:
                    arrow_keys["right"] = False

                if not keys_pressed[pygame.K_LEFT]:
                    arrow_keys["left"] = False

                if not arrow_keys["up"] and not arrow_keys["down"] \
                        and not arrow_keys["right"] and not arrow_keys["left"]:
                    pygame.time.set_timer(walking_movement_timer, 0)
                    pygame.time.set_timer(walking_animation_timer, 0)
                    current_frame = player.animate(True)

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        collided_with = player.hitbox.collidelist(collision_list)
        if collided_with is not -1:
            player.collide(collision_list[collided_with])

        screen.fill((255, 255, 255))
        western_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        western_forest.draw_fg(screen)
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)
        clock.tick(60)
        pygame.display.flip()


def cave(screen, clock, spritesheet, player, spawnpoint):
    """SCREEN 6"""

    bg_array = [
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],
        [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28]
        ]

    fg_array = [
        [29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0,30,31, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0,29,29,29,29,29,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29,29, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0,29,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0,29,29, 0, 0, 0, 0, 0, 0,29, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 29],
        [29, 0, 0, 0, 0, 0,29, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,29, 0, 0, 29],
        [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29],
        [29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29, 0, 0,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29]
        ]

    cave = Level(spritesheet, 32, 256, bg_array, fg_array)
    collision_list = cave.get_collision_list()

    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()

    current_frame = player.animate(True)

    walking_animation_timer = pygame.USEREVENT + 1
    walking_movement_timer = pygame.USEREVENT + 2
    check_keypresses_timer = pygame.USEREVENT + 3

    pygame.time.set_timer(check_keypresses_timer, 5)

    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == walking_animation_timer:
                current_frame = player.animate()

            if event.type == walking_movement_timer:
                player.move()

            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()

                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"

                    if not arrow_keys["up"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["up"] = True

                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"

                    if not arrow_keys["down"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["down"] = True

                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"

                    if not arrow_keys["right"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["right"] = True

                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"

                    if not arrow_keys["left"]:
                        current_frame = player.animate()
                        pygame.time.set_timer(walking_movement_timer, 50)
                        pygame.time.set_timer(walking_animation_timer, 200)
                        arrow_keys["left"] = True

                if not keys_pressed[pygame.K_UP]:
                    arrow_keys["up"] = False

                if not keys_pressed[pygame.K_DOWN]:
                    arrow_keys["down"] = False

                if not keys_pressed[pygame.K_RIGHT]:
                    arrow_keys["right"] = False

                if not keys_pressed[pygame.K_LEFT]:
                    arrow_keys["left"] = False

                if not arrow_keys["up"] and not arrow_keys["down"] \
                        and not arrow_keys["right"] and not arrow_keys["left"]:
                    pygame.time.set_timer(walking_movement_timer, 0)
                    pygame.time.set_timer(walking_animation_timer, 0)
                    current_frame = player.animate(True)

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        collided_with = player.hitbox.collidelist(collision_list)
        if collided_with is not -1:
            player.collide(collision_list[collided_with])

        screen.fill((255, 255, 255))
        cave.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        cave.draw_fg(screen)
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)
        clock.tick(60)
        pygame.display.flip()


def screen_handler(screen, clock, spritesheet, player):
    """Handles which screens should be called, and anything that goes on in between."""

    pygame.mixer.stop()
    scarlet_forest = pygame.mixer.Sound("Audio/scarlet_forest.ogg")
    scarlet_forest.play(-1)

    forest_entrance(screen, clock, spritesheet, player, (704, 608))
    southwestern_forest(screen, clock, spritesheet, player, (1120, 256))
    forest_entrance(screen, clock, spritesheet, player, (0, 256))
    eastern_forest(screen, clock, spritesheet, player, (704, 608), False)
    northern_forest(screen, clock, spritesheet, player, (416, 608))
    eastern_forest(screen, clock, spritesheet, player, (416, 0), True)
    western_forest(screen, clock, spritesheet, player, (1120, 512))

    pygame.mixer.stop()
    rude_buster = pygame.mixer.Sound("Audio/rude_buster.ogg")
    rude_buster.play(-1)

    cave(screen, clock, spritesheet, player, (562, 608))

if __name__ == "__main__":
    pygame.init()

    size = (1152, 850)
    screen = pygame.display.set_mode(size)

    spritesheet = pygame.image.load("Images/spritesheet.png").convert_alpha()

    pygame.display.set_caption("Forest Adventure")
    # SET ICON

    clock = pygame.time.Clock()

    player_south_sword_walking = get_frames(spritesheet, (0, 128, 128, 32), 32)
    player_north_sword_walking = get_frames(spritesheet, (128, 128, 128, 32), 32)
    player_east_sword_walking = get_frames(spritesheet, (0, 160, 128, 32), 32)
    player_west_sword_walking = get_frames(spritesheet, (128, 160, 128, 32), 32)

    animations = [player_north_sword_walking, player_south_sword_walking,
                  player_west_sword_walking, player_east_sword_walking]

    player = Player(7, 20, pygame.Rect(16, 16, 32, 32), pygame.Rect(0, 0, 64, 64), "up", 5, animations)

    screen_handler(screen, clock, spritesheet, player)
