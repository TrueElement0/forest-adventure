# Main Game Screens
# Mason Kury

from Level import *
from Entity import *


# global pygame timer event ID's used for activating events like animation and movement
walking_animation_timer = pygame.USEREVENT + 0  # timer for walking frame animation
walking_movement_timer = pygame.USEREVENT + 1   # timer for walking movement
check_keypresses_timer = pygame.USEREVENT + 2   # timer for checking user keyboard input
enemy_animations_timer = pygame.USEREVENT + 3   # timer for animating the enemies
entity_movement_timer = pygame.USEREVENT + 4     # timer for all movement other than the player
reset_player_abilities = pygame.USEREVENT + 5   # timer for controlling the speed of player abilities
enemy_attack_timer = pygame.USEREVENT + 6       # timer for controlling the enemies' attack speeds

# set up some global timers that will never stop running
pygame.time.set_timer(check_keypresses_timer, 5)     # set the keypress check timer to run every 5 milliseconds
pygame.time.set_timer(enemy_animations_timer, 200)   # set the enemy animations timer to run every 200 milliseconds
pygame.time.set_timer(entity_movement_timer, 50)     # set the entity movement timer to run every 50 milliseconds
pygame.time.set_timer(enemy_attack_timer, 1200)      # set the enemy attack timer to run every 1000 milliseconds
pygame.time.set_timer(reset_player_abilities, 1000)  # set a timer to reset the dodge ability every 1000 milliseconds


def check_events(player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames, arrow_image, arrow_keys, showing_sign=False):
    """DOC"""

    # parse pygame events
    for event in pygame.event.get():

        # user clicked exit
        if event.type == pygame.QUIT:
            return -1

        # advance player walking animation
        if event.type == walking_animation_timer and not showing_sign:
            # get the next frame of the animation
            current_frame = player.animate()

        # advance actual positional movement
        if event.type == walking_movement_timer and not showing_sign:
            # move the player based on their movement speed
            player.move()

        # advance enemy walking animations
        if event.type == enemy_animations_timer and not showing_sign:
            # get the next frame of the animation
            for enemy in range(len(enemies_list)):
                if not enemies_list[enemy].hitbox.colliderect(player.hitbox):
                    if enemies_list[enemy].attacking and not enemies_list[enemy].enemy_type == "ranged":
                        enemy_frame = enemies_list[enemy].animate(True)
                        enemy_frames[enemy] = enemy_frame
                    elif len(enemies_list[enemy].path) > 0:
                        enemy_frame = enemies_list[enemy].animate()
                        enemy_frames[enemy] = enemy_frame

        if event.type == entity_movement_timer and not showing_sign:
            # check if any enemies can 'see' the player; if so, calculate a path to the player
            for enemy in enemies_list:
                if player.hitbox.colliderect(enemy.sight_rect):
                    enemy.calculate_path(player.hitbox.topleft)
            # move the enemies based on their movement speed and current paths
            for enemy in enemies_list:
                if not enemy.attacking or (enemy.enemy_type == "ranged" and not enemy.hitbox.colliderect(player.hitbox)):
                    enemy.follow_path()
                elif enemy.enemy_type == "ranged" and enemy.hitbox.colliderect(player.hitbox):
                    enemy.collide(player.hitbox)

            for arrow in player_arrows:
                arrow.move()
            for arrow in enemy_arrows:
                arrow.move()

        if event.type == reset_player_abilities and not showing_sign:
            player.can_dodge = True
            player.can_use_item = True

        if event.type == enemy_attack_timer:
            for enemy in enemies_list:
                if enemy.attacking:
                    if enemy.enemy_type == "melee" and enemy.sword_swing.colliderect(player.hitbox):
                        if player.health > 1:
                            player.health -= 1
                        else:
                            return -2
                    elif enemy.enemy_type == "ranged" and enemy.sight_rect.colliderect(player.hitbox):
                        arrow = Arrow(arrow_image, (32, 32), 12, enemy.hitbox.x, enemy.hitbox.y)
                        arrow.face_target((player.hitbox.x, player.hitbox.y))
                        enemy_arrows.append(arrow)
                    enemy.attacking = False

        # check keypresses
        if event.type == check_keypresses_timer and not showing_sign:

            keys_pressed = pygame.key.get_pressed()  # get the currently pressed keypresses

            # up is pressed
            if keys_pressed[pygame.K_UP]:
                player.direction = "up"  # update the player direction

                # only run on the actual keypress:
                if not arrow_keys["up"]:
                    current_frame = player.animate()  # orient the player with a new frame
                    pygame.time.set_timer(walking_movement_timer, 50)  # set the movement timer for every 50 ms
                    pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                    arrow_keys["up"] = True  # set the up arrow state to True (pressed)

            # down is pressed
            elif keys_pressed[pygame.K_DOWN]:
                player.direction = "down"  # update the player direction

                # only run on the actual keypress:
                if not arrow_keys["down"]:
                    current_frame = player.animate()  # orient the player with a new frame
                    pygame.time.set_timer(walking_movement_timer, 50)  # set the movement timer for every 50 ms
                    pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                    arrow_keys["down"] = True  # set the down arrow state to True

            # right is pressed
            elif keys_pressed[pygame.K_RIGHT]:
                player.direction = "right"  # update the player direction

                # only run on the actual keypress:
                if not arrow_keys["right"]:
                    current_frame = player.animate()  # orient the player with a new frame
                    pygame.time.set_timer(walking_movement_timer, 50)  # set the movement timer for every 50 ms
                    pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                    arrow_keys["right"] = True  # set the right arrow state to True

            # left is pressed
            elif keys_pressed[pygame.K_LEFT]:
                player.direction = "left"  # update the player direction

                # only run on the actual keypress:
                if not arrow_keys["left"]:
                    current_frame = player.animate()  # orient the player with a new frame
                    pygame.time.set_timer(walking_movement_timer, 50)  # set the movement timer for every 50 ms
                    pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                    arrow_keys["left"] = True  # set the right arrow state to True

            # up is NOT being pressed
            if not keys_pressed[pygame.K_UP]:
                arrow_keys["up"] = False

            # down is NOT being pressed
            if not keys_pressed[pygame.K_DOWN]:
                arrow_keys["down"] = False

            # right is NOT being pressed
            if not keys_pressed[pygame.K_RIGHT]:
                arrow_keys["right"] = False

            # left is NOT being pressed
            if not keys_pressed[pygame.K_LEFT]:
                arrow_keys["left"] = False

            # NO arrow keys are being pressed (all False)
            if not arrow_keys["up"] and not arrow_keys["down"] \
                    and not arrow_keys["right"] and not arrow_keys["left"]:
                pygame.time.set_timer(walking_movement_timer, 0)  # shut down the movement timer
                pygame.time.set_timer(walking_animation_timer, 0)  # shut down the animation timer
                current_frame = player.animate(True)  # set the current frame to the standing frame

        # keys that should only register once when pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and player.can_dodge and not showing_sign:
                player.dodge()
                player.can_dodge = False

            elif event.key == pygame.K_LALT and player.can_use_item and not showing_sign:
                if player.inventory.current_item == "sword":
                    player.sword_attack(enemies_list)
                elif player.inventory.current_item == "bow":
                    player_arrows = player.bow_attack(arrow_image, player_arrows)
                elif player.inventory.current_item == "health potion":
                    player.drink_potion()
                player.can_use_item = False

            elif event.key == pygame.K_ESCAPE:
                showing_sign = False

            elif event.key == pygame.K_1:
                player.inventory.set_item(1)
            elif event.key == pygame.K_2:
                player.inventory.set_item(2)
            elif event.key == pygame.K_3:
                player.inventory.set_item(3)
            elif event.key == pygame.K_4:
                player.inventory.set_item(4)
            elif event.key == pygame.K_5:
                player.inventory.set_item(5)

    return current_frame, player_arrows, enemy_frames, enemy_arrows, arrow_keys, showing_sign


def draw(screen, clock, level, hud, player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames, debug_mode, showing_sign=False, sign_text=None, font=None):
    """
    DOC
    """

    screen.fill((255, 255, 255))  # (reset the screen with white)

    # draw the background layer, then the player and enemies, then the foreground layer
    level.draw_bg(screen)

    screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
    for enemy in range(len(enemies_list)):
        if not enemies_list[enemy].dead:
            screen.blit(enemy_frames[enemy], (enemies_list[enemy].hitbox.x, enemies_list[enemy].hitbox.y))
        else:
            del enemies_list[enemy]
            del enemy_frames[enemy]
            break  # exit the loop to avoid index errors, now that an enemy has been removed. If more than one enemy
            # was somehow killed at once, the other one will be removed one tick later (1/60 seconds)

    for arrow in player_arrows:
        if not arrow.hit:
            arrow.draw(screen)
        else:
            player_arrows.remove(arrow)
            break
    for arrow in enemy_arrows:
        if not arrow.hit:
            arrow.draw(screen)
        else:
            enemy_arrows.remove(arrow)
            break

    level.draw_fg(screen)

    # draw the HUD
    if len(enemies_list) == 1 and enemies_list[0].enemy_type == "ranged":
        hud.update(player, enemies_list[0])
    else:
        hud.update(player)
    hud.draw(screen, (0, 640))

    if debug_mode:
        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)
        for enemy in enemies_list:
            if enemy.enemy_type == "melee":
                pygame.draw.rect(screen, (0, 255, 0), enemy.sword_swing, 2)
            pygame.draw.rect(screen, (255, 0, 0), enemy.hitbox, 2)
            pygame.draw.rect(screen, (0, 0, 255), enemy.sight_rect, 2)
        for arrow in player_arrows:
            pygame.draw.rect(screen, (255, 0, 0), arrow.hitbox, 2)
        for arrow in enemy_arrows:
            pygame.draw.rect(screen, (255, 0, 0), arrow.hitbox, 2)

    if showing_sign:
        pygame.draw.rect(screen, (100, 100, 25), (100, 50, 950, 500))
        for line in sign_text:
            current_text = font.render(line, True, (0, 0, 0))
            screen.blit(current_text, (120, 100 + (50 * sign_text.index(line))))

    clock.tick(60)
    pygame.display.flip()


def title_screen(screen, clock):
    """
    DOC
    """
    # stop any music that is playing, and play the title screen music in a loop
    pygame.mixer.stop()
    the_holy = pygame.mixer.Sound("Audio/the_holy.ogg")
    the_holy.play(-1)

    title_font = pygame.font.SysFont("calibri", 100, True)
    title = title_font.render("Forest Adventure", True, (255, 255, 255))

    message_font = pygame.font.SysFont("calibri", 22, True)
    message = message_font.render("Press any button to start", True, (255, 255, 255))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return 0, 1

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (9, 113, 23), pygame.Rect(0, 0, 1152, 600))
        pygame.draw.rect(screen, (102, 69, 8), pygame.Rect(0, 600, 1152, 250))
        screen.blit(title, (225, 250))
        screen.blit(message, (465, 700))
        clock.tick(60)
        pygame.display.flip()


def forest_entrance(screen, clock, spritesheet, player, hud, spawnpoint, enemies_list, arrow_image):
    """
    Screen 1 -- The forest entrance. The player enters from the South and cannot go back through the entrance.
    There is one enemy that spawns, and the player can progress to screen 2 or 3 from this screen.

    Parameters:
        screen: must be of type pygame.Surface; the screen surface to draw to.
        clock: must be of type pygame.Clock; the graphics clock used for drawing.
        player: must be a player object from the entity module; the player character.
        spawnpoint: must be a tuple of length 2; the x and y coordinates of where the player spawns.

    Returns: (none)
    """

    # the background tileset to be drawn before the player (includes grass, dirt or stone)
    bg_array = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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

    # the foreground tileset to be drawn after the player (includes any interactive blocks, trees, rocks, etc.)
    fg_array = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3,12, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,11, 0,10, 5, 5, 5, 5, 5, 5, 5, 5, 5,13, 3, 3],
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

    # rectangles touching the borders of the game screen; used to stop the player from getting out of the map
    screen_boundaries = [pygame.Rect(0, -32, 1152, 32), pygame.Rect(0, 640, 1152, 32),
                         pygame.Rect(-32, 0, 32, 640), pygame.Rect(1152, 0, 32, 640)]

    # create a level object, and give it the two arrays created above
    forest_entrance = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = forest_entrance.get_collision_list()

    sign_text = ["Welcome to the windy forest. There have been rumors of great riches lying around here somewhere:",
                "something about a cave? I'll bet it's guarded though...so you should probably look around for a",
                "better weapon. Move around with the arrow keys, attack with left ALT, and dodge with left CTRL.",
                "You can also use the numbers 1-5 to access items in your inventory, and use them with left ALT.",
                "Oh, and you can press ESCAPE to exit signs!",
                "Good luck, adventurer!"]

    font = pygame.font.SysFont("calibri", 22, True)

    showing_sign = False

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    entered_forest = False
    entered_screen = False

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction
    enemy_frames = []  # initialize a list to hold all the enemy animation frames

    player_arrows = []
    enemy_arrows = []

    # for every enemy in the level, get the first frame and add it to the frames list
    for enemy in enemies_list:
        enemy_frame = enemy.animate(True)
        enemy_frames.append(enemy_frame)

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    # MAIN GAME SCREEN LOOP
    while True:
        # check all events, such as timers for animation/movement, keypresses, etc.
        event_data = check_events(player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames, arrow_image, arrow_keys, showing_sign)

        if event_data is not -1 and event_data is not -2:
            # update the animation lists based on the returned data from events, and update the arrow key states
            current_frame = event_data[0]
            player_arrows = event_data[1]
            enemy_frames = event_data[2]
            enemy_arrows = event_data[3]
            arrow_keys = event_data[4]
            showing_sign = event_data[5]
        elif event_data is -1:
            return -1  # otherwise the user quit
        else:
            return 1, 8  # player died

        # if the player enters the forest or the player comes in from a different spawn point (already entered)
        if spawnpoint[1] != 608 or (not entered_forest and player.hitbox.y < spawnpoint[1] - player.hitbox.height):

            # draw a rock barrier in front of the entrance
            forest_entrance.fg_array[19][21] = 29
            forest_entrance.fg_array[19][22] = 29
            forest_entrance.fg_array[19][23] = 29
            # update the collision array to have simple collision for the rocks
            forest_entrance.collision_array[19][21] = 1
            forest_entrance.collision_array[19][22] = 1
            forest_entrance.collision_array[19][23] = 1

            collision_list = forest_entrance.get_collision_list()  # update the collision list

            entered_forest = True  # the player has now entered the forest

        # if the player fully enters the screen from a different screen, add the exit paths to the collision array
        if not entered_screen and (player.hitbox.x > spawnpoint[0] + player.hitbox.width or
                                   player.hitbox.x < spawnpoint[0] - player.hitbox.width or
                                   player.hitbox.y > spawnpoint[1] + player.hitbox.height or
                                   player.hitbox.y < spawnpoint[1] - player.hitbox.height):

            # set the exit pathways' collision physics to 4
            forest_entrance.collision_array[8][0] = 4
            forest_entrance.collision_array[0][22] = 5

            collision_list = forest_entrance.get_collision_list()  # update the collision_list

            entered_screen = True  # the player has now entered the screen

        for boundary in screen_boundaries:
            if player.hitbox.colliderect(boundary):
                player.collide(boundary)
            for enemy in enemies_list:
                if enemy.hitbox.colliderect(boundary):
                    enemy.hitbox.x = enemy.spawnpoint[0]
                    enemy.hitbox.y = enemy.spawnpoint[1]
                    enemy.align_sight()
                    if enemy.enemy_type == "melee":
                        enemy.align_sword_swing()
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True


        for block in range(len(collision_list) - 1):
            if collision_list[block] is not None and player.hitbox.colliderect(collision_list[block]):

                row = block // len(forest_entrance.collision_array[0])
                column = block % len(forest_entrance.collision_array[0])

                block_type = forest_entrance.collision_array[row][column]

                # collided with a sign, so collide, step back, and set the showing_sign variable to true
                if block_type is 2:
                    player.collide(collision_list[block])
                    player.step_back()
                    showing_sign = True

                    hud.quest_text = ["Find a better weapon!"]

                elif block_type is 4:
                    return 1, 2  # go to screen 2
                elif block_type is 5:
                    return 1, 3  # go to screen 3
                else:
                    player.collide(collision_list[block])

            for arrow in player_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True

        for enemy in enemies_list:
            if enemy.enemy_type == "melee" and enemy.sword_swing.colliderect(player.hitbox):
                enemy.attacking = True
            if enemy.hitbox.colliderect(player.hitbox):
                enemy.collide(player.hitbox)
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(enemy.hitbox):
                    arrow.hit = True
                    enemy.damage(1)

        draw(screen, clock, forest_entrance, hud, player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames, False, showing_sign, sign_text, font)


def southwestern_forest(screen, clock, spritesheet, player, hud, spawnpoint, enemies_list, arrow_image, looted_chest):
    """
    Screen 2 -- The Southwestern forest. The player enters from the East (from screen 1) and can return if they choose.
    There are three enemies that spawn throughout the screen, and one chest at the end of the pathway that
    contains gold and a health potion.

    Parameters:
        screen: must be of type pygame.Surface; the screen surface to draw to.
        clock: must be of type pygame.Clock; the graphics clock used for drawing.
        player: must be a player object from the entity module; the player character.
        spawnpoint: must be a tuple of length 2; the x and y coordinates of where the player spawns.

    Returns: (none)
    """

    # the background tileset to be drawn before the player (includes grass, dirt or stone)
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

    # the foreground tileset to be drawn after the player (includes any interactive blocks, trees, rocks, etc.)
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

    if looted_chest:
        fg_array[3][4] = 0

    # rectangles touching the borders of the game screen; used to stop the player from getting out of the map
    screen_boundaries = [pygame.Rect(0, -32, 1152, 32), pygame.Rect(0, 640, 1152, 32),
                         pygame.Rect(-32, 0, 32, 640), pygame.Rect(1152, 0, 32, 640)]

    # create a level object, and give it the two arrays created above
    southwestern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = southwestern_forest.get_collision_list()

    chest_contents = {"health potion":1, "gold":50}

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    can_dodge = True

    entered_screen = False

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction
    enemy_frames = []  # initialize a list to hold all the enemy animation frames

    player_arrows = []
    enemy_arrows = []

    # for every enemy in the level, get the first frame and add it to the frames list
    for enemy in enemies_list:
        enemy_frame = enemy.animate(True)
        enemy_frames.append(enemy_frame)

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    # MAIN GAME SCREEN LOOP
    while True:

        # check all events, such as timers for animation/movement, keypresses, etc.
        event_data = check_events(player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames,
                                  arrow_image, arrow_keys)

        if event_data is not -1 and event_data is not -2:
            # update the animation lists based on the returned data from events, and update the arrow key states
            current_frame = event_data[0]
            player_arrows = event_data[1]
            enemy_frames = event_data[2]
            enemy_arrows = event_data[3]
            arrow_keys = event_data[4]
        elif event_data is -1:
            return -1  # otherwise the user quit
        else:
            return 1, 8  # player died

        # if the player fully enters the screen from a different screen, add the exit paths to the collision array
        if not entered_screen and (player.hitbox.x > spawnpoint[0] + player.hitbox.width or
                                   player.hitbox.x < spawnpoint[0] - player.hitbox.width or
                                   player.hitbox.y > spawnpoint[1] + player.hitbox.height or
                                   player.hitbox.y < spawnpoint[1] - player.hitbox.height):

            # set the exit pathway's collision physics to 4
            southwestern_forest.collision_array[8][35] = 4

            collision_list = southwestern_forest.get_collision_list()  # update the collision_list

            entered_screen = True  # the player has now entered the screen

        for boundary in screen_boundaries:
            if player.hitbox.colliderect(boundary):
                player.collide(boundary)
            for enemy in enemies_list:
                if enemy.hitbox.colliderect(boundary):
                    enemy.hitbox.x = enemy.spawnpoint[0]
                    enemy.hitbox.y = enemy.spawnpoint[1]
                    enemy.align_sight()
                    if enemy.enemy_type == "melee":
                        enemy.align_sword_swing()
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True


        for block in range(len(collision_list) - 1):
            if collision_list[block] is not None and player.hitbox.colliderect(collision_list[block]):

                row = block // len(southwestern_forest.collision_array[0])
                column = block % len(southwestern_forest.collision_array[0])

                block_type = southwestern_forest.collision_array[row][column]

                if block_type is 4:
                    return 2, 1, looted_chest # go to screen 1 (pass back chest status as well)
                elif block_type is 3:
                    # remove the chest from the fg_array and collision array, and update the collision_list
                    southwestern_forest.fg_array[row][column] = 0
                    southwestern_forest.collision_array[row][column] = 0
                    collision_list = southwestern_forest.get_collision_list()
                    looted_chest = True

                    # add the chest contents to the player's inventory
                    for item in chest_contents.keys():
                        player.inventory.add(item, chest_contents[item])
                else:
                    player.collide(collision_list[block])

            for arrow in player_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True


        for enemy in enemies_list:
            if enemy.enemy_type == "melee" and enemy.sword_swing.colliderect(player.hitbox):
                enemy.attacking = True
            if enemy.hitbox.colliderect(player.hitbox):
                enemy.collide(player.hitbox)
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(enemy.hitbox):
                    arrow.hit = True
                    enemy.damage(1)

        draw(screen, clock, southwestern_forest, hud, player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames, False)


def eastern_forest(screen, clock, spritesheet, player, hud, spawnpoint, enemies_list, arrow_image, looted_chest):
    """
    Screen 3 -- The Eastern forest. The player enters from the South originally, or the North if they have collected
    the bow and arrows from the Northern screen. There are two enemies that spawn, both melee, on this screen, and one
    chest near the entrance that contains a health potion. The player can exit the screen back through the South
    (to go to screen 1), through the North (to go to screen 4), or through the West (to screen 5) if they have acquired
    the bow and arrows.

    Parameters:
        screen: must be of type pygame.Surface; the screen surface to draw to.
        clock: must be of type pygame.Clock; the graphics clock used for drawing.
        player: must be a player object from the entity module; the player character.
        spawnpoint: must be a tuple of length 2; the x and y coordinates of where the player spawns.

    Returns: (none)
    """

    # the background tileset to be drawn before the player (includes grass, dirt or stone)
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

    # the foreground tileset to be drawn after the player (includes any interactive blocks, trees, rocks, etc.)
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

    if looted_chest:
        fg_array[15][31] = 0

    # rectangles touching the borders of the game screen; used to stop the player from getting out of the map
    screen_boundaries = [pygame.Rect(0, -32, 1152, 32), pygame.Rect(0, 640, 1152, 32),
                         pygame.Rect(-32, 0, 32, 640), pygame.Rect(1152, 0, 32, 640)]

    # if the player has acquired the bow and arrow, remove the blockade of rocks
    if "bow" in player.inventory.inventory_dict:
        fg_array[15][2] = 11
        fg_array[16][2] = 0
        fg_array[17][2] = 4

    # create a level object, and give it the two arrays created above
    eastern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = eastern_forest.get_collision_list()

    chest_contents = {"health potion":1, "gold":75}

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    entered_screen = False

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction
    enemy_frames = []  # initialize a list to hold all the enemy animation frames

    player_arrows = []
    enemy_arrows = []

    # for every enemy in the level, get the first frame and add it to the frames list
    for enemy in enemies_list:
        enemy_frame = enemy.animate(True)
        enemy_frames.append(enemy_frame)

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    # MAIN GAME SCREEN LOOP
    while True:

        # check all events, such as timers for animation/movement, keypresses, etc.
        event_data = check_events(player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames,
                                  arrow_image, arrow_keys)

        if event_data is not -1 and event_data is not -2:
            # update the animation lists based on the returned data from events, and update the arrow key states
            current_frame = event_data[0]
            player_arrows = event_data[1]
            enemy_frames = event_data[2]
            enemy_arrows = event_data[3]
            arrow_keys = event_data[4]
        elif event_data is -1:
            return -1  # otherwise the user quit
        else:
            return 1, 8  # player died

        # if the player fully enters the screen from a different screen, add the exit paths to the collision array
        if not entered_screen and (player.hitbox.x > spawnpoint[0] + player.hitbox.width or
                                   player.hitbox.x < spawnpoint[0] - player.hitbox.width or
                                   player.hitbox.y > spawnpoint[1] + player.hitbox.height or
                                   player.hitbox.y < spawnpoint[1] - player.hitbox.height):

            # set the exit pathways' collision physics to the appropriate pathway number
            eastern_forest.collision_array[19][22] = 4
            eastern_forest.collision_array[0][13] = 5
            eastern_forest.collision_array[16][0] = 6

            collision_list = eastern_forest.get_collision_list()  # update the collision_list

            entered_screen = True  # the player has now entered the screen

        for boundary in screen_boundaries:
            if player.hitbox.colliderect(boundary):
                player.collide(boundary)
            for enemy in enemies_list:
                if enemy.hitbox.colliderect(boundary):
                    enemy.hitbox.x = enemy.spawnpoint[0]
                    enemy.hitbox.y = enemy.spawnpoint[1]
                    enemy.align_sight()
                    if enemy.enemy_type == "melee":
                        enemy.align_sword_swing()
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True

            for arrow in enemy_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True

        for block in range(len(collision_list) - 1):
            if collision_list[block] is not None and player.hitbox.colliderect(collision_list[block]):

                row = block // len(eastern_forest.collision_array[0])
                column = block % len(eastern_forest.collision_array[0])

                block_type = eastern_forest.collision_array[row][column]

                if block_type is 4:
                    return 3, 1, looted_chest  # go to screen 1
                elif block_type is 5:
                    return 3, 4, looted_chest  # go to screen 4
                elif block_type is 6:
                    return 3, 5, looted_chest  # go to screen 5
                elif block_type is 3:
                    # remove the chest from the fg_array and collision array, and update the collision_list
                    eastern_forest.fg_array[row][column] = 0
                    eastern_forest.collision_array[row][column] = 0
                    collision_list = eastern_forest.get_collision_list()
                    looted_chest = True

                    # add the chest contents to the player's inventory
                    for item in chest_contents.keys():
                        player.inventory.add(item, chest_contents[item])
                else:
                    player.collide(collision_list[block])

            for arrow in player_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True

            for arrow in enemy_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True

        for enemy in enemies_list:
            if enemy.enemy_type == "melee" and enemy.sword_swing.colliderect(player.hitbox):
                enemy.attacking = True
            elif enemy.enemy_type == "ranged" and enemy.sight_rect.colliderect(player.hitbox):
                enemy.attacking = True
            if enemy.hitbox.colliderect(player.hitbox):
                enemy.collide(player.hitbox)
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(enemy.hitbox):
                    arrow.hit = True
                    enemy.damage(1)


        for arrow in enemy_arrows:
            if arrow.hitbox.colliderect(player.hitbox):
                arrow.hit = True
                if player.health > 1:
                    player.health -= 1
                else:
                    return 0, 8

        draw(screen, clock, eastern_forest, hud, player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames, False)


def northern_forest(screen, clock, spritesheet, player, hud, spawnpoint, enemies_list, arrow_image, looted_chest):
    """
    Screen 4 -- The Northern forest. The player enters from the South and can return (to screen 3) if they choose.
    There are three enemies that spawn on this screen, one ranged enemy on the left, one melee enemy that patrols the
    entryway into the screen, and one melee enemy that guards the bow and arrows contained within the chest on the
    right. There is one chest on the right with a sign that explains the contents and controls (for the bow within
    the chest.)

    Parameters:
        screen: must be of type pygame.Surface; the screen surface to draw to.
        clock: must be of type pygame.Clock; the graphics clock used for drawing.
        player: must be a player object from the entity module; the player character.
        spawnpoint: must be a tuple of length 2; the x and y coordinates of where the player spawns.

    Returns: (none)
    """

    # the background tileset to be drawn before the player (includes grass, dirt or stone)
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

    # the foreground tileset to be drawn after the player (includes any interactive blocks, trees, rocks, etc.)
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

    if looted_chest:
        fg_array[15][18] = 0

    # rectangles touching the borders of the game screen; used to stop the player from getting out of the map
    screen_boundaries = [pygame.Rect(0, -32, 1152, 32), pygame.Rect(0, 640, 1152, 32),
                         pygame.Rect(-32, 0, 32, 640), pygame.Rect(1152, 0, 32, 640)]

    # create a level object, and give it the two arrays created above
    northern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = northern_forest.get_collision_list()

    sign_text = ["This chest contains a bow and some arrows. Use them wisely, because you can run out!",
                 "The controls are the same as for the sword; whichever direction you are facing is the direction",
                 "that you will shoot. (left ALT to shoot)",
                 "You should try practicing on that red enemy over there..."]

    font = pygame.font.SysFont("calibri", 22, True)

    showing_sign = False

    chest_contents = {"bow":1, "arrows":10, "health potion":1, "gold":100}

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    entered_screen = False

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction
    enemy_frames = []  # initialize a list to hold all the enemy animation frames

    player_arrows = []
    enemy_arrows = []

    # for every enemy in the level, get the first frame and add it to the frames list
    for enemy in enemies_list:
        enemy_frame = enemy.animate(True)
        enemy_frames.append(enemy_frame)

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    # MAIN GAME SCREEN LOOP
    while True:

        # check all events, such as timers for animation/movement, keypresses, etc.
        event_data = check_events(player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames,
                                  arrow_image, arrow_keys, showing_sign)

        if event_data is not -1 and event_data is not -2:
            # update the animation lists based on the returned data from events, and update the arrow key states
            current_frame = event_data[0]
            player_arrows = event_data[1]
            enemy_frames = event_data[2]
            enemy_arrows = event_data[3]
            arrow_keys = event_data[4]
            showing_sign = event_data[5]
        elif event_data is -1:
            return -1  # otherwise the user quit
        else:
            return 1, 8  # player died

        # if the player fully enters the screen from a different screen, add the exit paths to the collision array
        if not entered_screen and (player.hitbox.x > spawnpoint[0] + player.hitbox.width or
                                   player.hitbox.x < spawnpoint[0] - player.hitbox.width or
                                   player.hitbox.y > spawnpoint[1] + player.hitbox.height or
                                   player.hitbox.y < spawnpoint[1] - player.hitbox.height):

            # set the exit pathway's collision physics to 4
            northern_forest.collision_array[19][13] = 4

            collision_list = northern_forest.get_collision_list()  # update the collision_list

            entered_screen = True  # the player has now entered the screen

        for boundary in screen_boundaries:
            if player.hitbox.colliderect(boundary):
                player.collide(boundary)
            for enemy in enemies_list:
                if enemy.hitbox.colliderect(boundary):
                    enemy.hitbox.x = enemy.spawnpoint[0]
                    enemy.hitbox.y = enemy.spawnpoint[1]
                    enemy.align_sight()
                    if enemy.enemy_type == "melee":
                        enemy.align_sword_swing()
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True

            for arrow in enemy_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True

        for block in range(len(collision_list) - 1):
            if collision_list[block] is not None and player.hitbox.colliderect(collision_list[block]):

                row = block // len(northern_forest.collision_array[0])
                column = block % len(northern_forest.collision_array[0])

                block_type = northern_forest.collision_array[row][column]

                # collided with a sign, so collide, step back, and set the showing_sign variable to true
                if block_type is 2:
                    player.collide(collision_list[block])
                    player.step_back()
                    showing_sign = True

                elif block_type is 3:
                    # remove the chest from the fg_array and collision array, and update the collision_list
                    northern_forest.fg_array[row][column] = 0
                    northern_forest.collision_array[row][column] = 0
                    collision_list = northern_forest.get_collision_list()
                    looted_chest = True

                    hud.quest_text = ["Find the cave!"]

                    # add the chest contents to the player's inventory
                    for item in chest_contents.keys():
                        player.inventory.add(item, chest_contents[item])

                elif block_type is 4:
                    return 4, 3, looted_chest  # go to screen 3
                else:
                    player.collide(collision_list[block])

            for arrow in player_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True

            for arrow in enemy_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True

        for enemy in enemies_list:
            if enemy.enemy_type == "melee" and enemy.sword_swing.colliderect(player.hitbox):
                enemy.attacking = True
            elif enemy.enemy_type == "ranged" and enemy.sight_rect.colliderect(player.hitbox):
                enemy.attacking = True
            if enemy.hitbox.colliderect(player.hitbox):
                enemy.collide(player.hitbox)
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(enemy.hitbox):
                    arrow.hit = True
                    enemy.damage(1)


        for arrow in enemy_arrows:
            if arrow.hitbox.colliderect(player.hitbox):
                arrow.hit = True
                if player.health > 1:
                    player.health -= 1
                else:
                    return 0, 8

        draw(screen, clock, northern_forest, hud, player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames, False, showing_sign, sign_text, font)


def western_forest(screen, clock, spritesheet, player, hud, spawnpoint, enemies_list, arrow_image, looted_chest):
    """
    Screen 5 -- The Western forest. The player enters from the east (from screen 3) and can return if they choose.
    The player can also exit through the cave in the North to advance to the bossfight. There are three enemies that
    spawn throughout the screen, (one melee near the entry, and two ranged guarding the cave), and one chest to the
    right of the cave containing gold and one final health potion.

    Parameters:
        screen: must be of type pygame.Surface; the screen surface to draw to.
        clock: must be of type pygame.Clock; the graphics clock used for drawing.
        player: must be a player object from the entity module; the player character.
        spawnpoint: must be a tuple of length 2; the x and y coordinates of where the player spawns.

    Returns: (none)
    """

    # the background tileset to be drawn before the player (includes grass, dirt or stone)
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

    # the foreground tileset to be drawn after the player (includes any interactive blocks, trees, rocks, etc.)
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

    if looted_chest:
        fg_array[4][32] = 0

    # rectangles touching the borders of the game screen; used to stop the player from getting out of the map
    screen_boundaries = [pygame.Rect(0, -32, 1152, 32), pygame.Rect(0, 640, 1152, 32),
                         pygame.Rect(-32, 0, 32, 640), pygame.Rect(1152, 0, 32, 640)]

    # create a level object, and give it the two arrays created above
    western_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = western_forest.get_collision_list()

    sign_text = ["The cave is just up ahead -- beware, though, of what may lay waiting inside!"]

    font = pygame.font.SysFont("calibri", 22, True)

    showing_sign = False

    chest_contents = {"arrows": 25, "health potion":1, "gold":150}

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    entered_screen = False

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction
    enemy_frames = []  # initialize a list to hold all the enemy animation frames

    player_arrows = []
    enemy_arrows = []

    # for every enemy in the level, get the first frame and add it to the frames list
    for enemy in enemies_list:
        enemy_frame = enemy.animate(True)
        enemy_frames.append(enemy_frame)

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    # MAIN GAME SCREEN LOOP
    while True:

        # check all events, such as timers for animation/movement, keypresses, etc.
        event_data = check_events(player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames,
                                  arrow_image, arrow_keys, showing_sign)

        if event_data is not -1 and event_data is not -2:
            # update the animation lists based on the returned data from events, and update the arrow key states
            current_frame = event_data[0]
            player_arrows = event_data[1]
            enemy_frames = event_data[2]
            enemy_arrows = event_data[3]
            arrow_keys = event_data[4]
            showing_sign = event_data[5]
        elif event_data is -1:
            return -1  # otherwise the user quit
        else:
            return 1, 8  # player died

        # if the player fully enters the screen from a different screen, add the exit paths to the collision array
        if not entered_screen and (player.hitbox.x > spawnpoint[0] + player.hitbox.width or
                                   player.hitbox.x < spawnpoint[0] - player.hitbox.width or
                                   player.hitbox.y > spawnpoint[1] + player.hitbox.height or
                                   player.hitbox.y < spawnpoint[1] - player.hitbox.height):

            # set the exit pathways collision physics to 4
            western_forest.collision_array[16][35] = 4

            western_forest.collision_array[0][18] = 5
            western_forest.collision_array[0][19] = 5
            western_forest.collision_array[0][21] = 5

            collision_list = western_forest.get_collision_list()  # update the collision_list

            entered_screen = True  # the player has now entered the screen

        for boundary in screen_boundaries:
            if player.hitbox.colliderect(boundary):
                player.collide(boundary)
            for enemy in enemies_list:
                if enemy.hitbox.colliderect(boundary):
                    enemy.hitbox.x = enemy.spawnpoint[0]
                    enemy.hitbox.y = enemy.spawnpoint[1]
                    enemy.align_sight()
                    if enemy.enemy_type == "melee":
                        enemy.align_sword_swing()
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True

            for arrow in enemy_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True

        for block in range(len(collision_list) - 1):
            if collision_list[block] is not None and player.hitbox.colliderect(collision_list[block]):

                row = block // len(western_forest.collision_array[0])
                column = block % len(western_forest.collision_array[0])

                block_type = western_forest.collision_array[row][column]

                # collided with a sign, so collide, step back, and set the showing_sign variable to true
                if block_type is 2:
                    player.collide(collision_list[block])
                    player.step_back()
                    showing_sign = True

                elif block_type is 3:
                    # remove the chest from the fg_array and collision array, and update the collision_list
                    western_forest.fg_array[row][column] = 0
                    western_forest.collision_array[row][column] = 0
                    collision_list = western_forest.get_collision_list()
                    looted_chest = True

                    # add the chest contents to the player's inventory
                    for item in chest_contents.keys():
                        player.inventory.add(item, chest_contents[item])

                elif block_type is 4:
                    return 5, 3, looted_chest  # go to screen 3
                elif block_type is 5:
                    return 5, 6, looted_chest  # go to screen 6
                else:
                    player.collide(collision_list[block])

            for arrow in player_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True

            for arrow in enemy_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True

        for enemy in enemies_list:
            if enemy.enemy_type == "melee" and enemy.sword_swing.colliderect(player.hitbox):
                enemy.attacking = True
            elif enemy.enemy_type == "ranged" and enemy.sight_rect.colliderect(player.hitbox):
                enemy.attacking = True
            if enemy.hitbox.colliderect(player.hitbox):
                enemy.collide(player.hitbox)
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(enemy.hitbox):
                    arrow.hit = True
                    enemy.damage(1)

        for arrow in enemy_arrows:
            if arrow.hitbox.colliderect(player.hitbox):
                arrow.hit = True
                if player.health > 1:
                    player.health -= 1
                else:
                    return 0, 8

        draw(screen, clock, western_forest, hud, player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames, False, showing_sign, sign_text, font)


def cave(screen, clock, spritesheet, player, hud, spawnpoint, enemies_list, arrow_image):
    """
    Screen 6 -- The cave. The player enters from the south and cannot exit back through. There is only one enemy
    in the cave -- the boss -- which is 4 times the size of the player. He is both ranged and melee, which is determined
    by a random number as he is moving. When the boss is defeated, rocks in front of the chest area disappear, allowing
    access for the player to collect the final loot and win the game.

    Parameters:
        screen: must be of type pygame.Surface; the screen surface to draw to.
        clock: must be of type pygame.Clock; the graphics clock used for drawing.
        player: must be a player object from the entity module; the player character.
        spawnpoint: must be a tuple of length 2; the x and y coordinates of where the player spawns.

    Returns: (none)
    """

    # the background tileset to be drawn before the player (includes grass, dirt or stone)
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

    # the foreground tileset to be drawn after the player (includes any interactive blocks, trees, rocks, etc.)
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

    # rectangles touching the borders of the game screen; used to stop the player from getting out of the map
    screen_boundaries = [pygame.Rect(0, -32, 1152, 32), pygame.Rect(0, 640, 1152, 32),
                         pygame.Rect(-32, 0, 32, 640), pygame.Rect(1152, 0, 32, 640)]

    # create a level object, and give it the two arrays created above
    cave = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = cave.get_collision_list()

    pygame.mixer.stop()  # now that the level has been loaded, stop all music from playing (for suspense, of course!)

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    entered_screen = False

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction
    enemy_frames = []  # initialize a list to hold all the enemy animation frames

    player_arrows = []
    enemy_arrows = []

    # for every enemy in the level, get the first frame and add it to the frames list
    for enemy in enemies_list:
        enemy.attacking = "stopped"
        enemy_frame = enemy.animate(True)
        enemy_frames.append(enemy_frame)

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    # MAIN GAME SCREEN LOOP
    while True:

        if len(enemies_list) == 0:
            cave.fg_array[4][17] = 0
            cave.fg_array[4][18] = 0
            cave.collision_array[4][17] = 0
            cave.collision_array[4][18] = 0
            collision_list = cave.get_collision_list()
            pygame.mixer.stop()

        # check all events, such as timers for animation/movement, keypresses, etc.
        event_data = check_events(player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames,
                                  arrow_image, arrow_keys)

        if event_data is not -1 and event_data is not -2:
            # update the animation lists based on the returned data from events, and update the arrow key states
            current_frame = event_data[0]
            player_arrows = event_data[1]
            enemy_frames = event_data[2]
            enemy_arrows = event_data[3]
            arrow_keys = event_data[4]
        elif event_data is -1:
            return -1  # otherwise the user quit
        else:
            return 1, 8  # player died

        # if the player fully enters the screen from a different screen, add the exit paths to the collision array
        if not entered_screen and (player.hitbox.x > spawnpoint[0] + player.hitbox.width or
                                   player.hitbox.x < spawnpoint[0] - player.hitbox.width or
                                   player.hitbox.y > spawnpoint[1] + player.hitbox.height or
                                   player.hitbox.y < spawnpoint[1] - player.hitbox.height):

            # block off the entrance to the cave with rocks
            cave.fg_array[19][17] = 29
            cave.fg_array[19][18] = 29
            # set the rocks' collision mode to 1 (standard collision)
            cave.collision_array[19][17] = 1
            cave.collision_array[19][18] = 1

            collision_list = cave.get_collision_list()  # update the collision_list

            entered_screen = True  # the user has now entered the screen

            # play some boss music!
            rude_buster = pygame.mixer.Sound("Audio/rude_buster.ogg")
            rude_buster.play(-1)

            # let the boss move
            enemies_list[0].move_speed = 5
            enemies_list[0].attacking = True

        for boundary in screen_boundaries:
            if player.hitbox.colliderect(boundary):
                player.collide(boundary)
            for enemy in enemies_list:
                if enemy.hitbox.colliderect(boundary):
                    enemy.hitbox.x = enemy.spawnpoint[0]
                    enemy.hitbox.y = enemy.spawnpoint[1]
                    enemy.align_sight()
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True

            for arrow in enemy_arrows:
                if arrow.hitbox.colliderect(boundary):
                    arrow.hit = True

        for block in range(len(collision_list) - 1):
            if collision_list[block] is not None and player.hitbox.colliderect(collision_list[block]):

                row = block // len(cave.collision_array[0])
                column = block % len(cave.collision_array[0])

                block_type = cave.collision_array[row][column]

                if block_type is 3:
                    return 6, 7  # display player wins screen
                else:
                    player.collide(collision_list[block])

            for arrow in player_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True

            for arrow in enemy_arrows:
                if collision_list[block] is not None and arrow.hitbox.colliderect(collision_list[block]):
                    arrow.hit = True

        for enemy in enemies_list:
            if enemy.enemy_type == "ranged" and enemy.sight_rect.colliderect(player.hitbox) and not enemy.attacking == "stopped":
                enemy.attacking = True
            if enemy.hitbox.colliderect(player.hitbox):
                enemy.collide(player.hitbox)
            for arrow in player_arrows:
                if arrow.hitbox.colliderect(enemy.hitbox):
                    arrow.hit = True
                    enemy.damage(1)

        for arrow in enemy_arrows:
            if arrow.hitbox.colliderect(player.hitbox):
                arrow.hit = True
                if player.health > 1:
                    player.health -= 1
                else:
                    return 0, 8

        draw(screen, clock, cave, hud, player, player_arrows, current_frame, enemies_list, enemy_arrows, enemy_frames, False)


def screen_handler():
    """Handles which screens should be called, and anything that goes on in between."""

    # set the screen size and create a surface
    size = (1152, 850)
    screen = pygame.display.set_mode(size)

    # load the tileset and entity spritesheet
    spritesheet = pygame.image.load("Images/spritesheet.png").convert_alpha()
    hud_elements = pygame.image.load("Images/hud_elements.png").convert_alpha()
    icon = pygame.image.load("Images/icon.png").convert_alpha()

    pygame.display.set_caption("Forest Adventure")  # set the caption on the top of the window
    pygame.display.set_icon(icon)  # set the icon to the icon image

    clock = pygame.time.Clock()  # create a clock object used to control the drawing rate

    # load animation strips from the spritesheet
    player_south_sword_walking = get_frames(spritesheet, (0, 128, 128, 32), 32)
    player_north_sword_walking = get_frames(spritesheet, (128, 128, 128, 32), 32)
    player_east_sword_walking = get_frames(spritesheet, (0, 160, 128, 32), 32)
    player_west_sword_walking = get_frames(spritesheet, (128, 160, 128, 32), 32)

    player_south_bow_walking = get_frames(spritesheet, (0, 192, 128, 32), 32)
    player_north_bow_walking = get_frames(spritesheet, (128, 192, 128, 32), 32)
    player_east_bow_walking = get_frames(spritesheet, (0, 224, 128, 32), 32)
    player_west_bow_walking = get_frames(spritesheet, (128, 224, 128, 32), 32)

    enemy_south_melee_walking = get_frames(spritesheet, (0, 256, 128, 32), 32)
    enemy_north_melee_walking = get_frames(spritesheet, (128, 256, 128, 32), 32)
    enemy_east_melee_walking = get_frames(spritesheet, (0, 288, 128, 32), 32)
    enemy_west_melee_walking = get_frames(spritesheet, (128, 288, 128, 32), 32)

    enemy_south_ranged_walking = get_frames(spritesheet, (0, 320, 128, 32), 32)
    enemy_north_ranged_walking = get_frames(spritesheet, (128, 320, 128, 32), 32)
    enemy_east_ranged_walking = get_frames(spritesheet, (0, 352, 128, 32), 32)
    enemy_west_ranged_walking = get_frames(spritesheet, (128, 352, 128, 32), 32)

    # put player animations into a list
    player_animations = [player_north_sword_walking, player_south_sword_walking,
                         player_west_sword_walking, player_east_sword_walking,
                         player_north_bow_walking, player_south_bow_walking,
                         player_west_bow_walking, player_east_bow_walking]

    # create the player using the animations as well as a bunch of other stats
    player = Player(7, 20, pygame.Rect(16, 16, 32, 32), pygame.Rect(0, 0, 64, 64), "up", 5, player_animations)

    # put enemy animations into a list
    enemy_animations = [enemy_north_melee_walking, enemy_south_melee_walking,
                        enemy_west_melee_walking, enemy_east_melee_walking,
                        enemy_north_ranged_walking, enemy_south_ranged_walking,
                        enemy_west_ranged_walking, enemy_east_ranged_walking]

    # create a two dimensional list containing a list element for each screen, which contains the enemies
    # that will spawn on the screen.
    enemies_list = [
        [   # SCREEN 1
            Enemy("melee", 5, (32, 32), 250, 100, "right", 2, enemy_animations[0:4], (384, 128), (800, 128), 50)
        ],
        [   # SCREEN 2
            Enemy("melee", 4, (32, 32), 250, 175, "down", 1, enemy_animations[0:4], (688, 160), (688, 512), 50),
            Enemy("melee", 4, (32, 32), 250, 175, "up", 1, enemy_animations[0:4], (400, 512), (400, 160), 50),
            Enemy("melee", 4, (32, 32), 250, 175, "down", 2, enemy_animations[0:4], (128, 160), (128, 512), 50)
        ],
        [   # SCREEN 3
            Enemy("melee", 4, (32, 32), 250, 100, "left", 2, enemy_animations[0:4], (960, 128), (384, 128), 55),
            Enemy("ranged", 3, (32, 32), 450, 450, "up", 4, enemy_animations[4:], (224, 512))
        ],
        [   # SCREEN 4
            Enemy("melee", 5, (32, 32), 250, 100, "up", 3, enemy_animations[0:4], (992, 480), (992, 128), 55),
            Enemy("ranged", 4, (32, 32), 350, 350, "up", 3, enemy_animations[4:], (176, 416))
        ],
        [   # SCREEN 5
            Enemy("melee", 6, (32, 32), 250, 200, "right", 3, enemy_animations[0:4], (96, 512), (544, 512), 64),
            Enemy("ranged", 4, (32, 32), 400, 400, "down", 3, enemy_animations[4:], (544, 96)),
            Enemy("ranged", 4, (32, 32), 400, 400, "down", 3, enemy_animations[4:], (672, 96))
        ],
        [
            # SCREEN 6
            Enemy("ranged", 0, (32, 32), 3000, 3000, "down", 8, enemy_animations[4:], (560, 416))
        ]
    ]

    arrow_image = get_frames(spritesheet, (224, 96, 32, 32), 32)

    # get all necessary images from the spritesheet
    base_image = get_image(hud_elements, pygame.Rect(0, 0, 1152, 210))
    items_elements = get_frames(hud_elements, pygame.Rect(0, 210, 900, 150), 150)
    hearts = get_frames(hud_elements, pygame.Rect(900, 210, 64, 32), 32)

    # add them all to one list
    hud_list = [base_image]
    for item in items_elements:
        hud_list.append(item)
    for heart in hearts:
        hud_list.append(heart)

    # create a hud using the items_list of images and stats from the player
    hud = HUD(hud_list, pygame.Rect(0, 0, 1152, 210), player.inventory.inventory_dict,
              player.inventory.current_item, ["Using the arrow keys to move,", "go bump into that sign over there!"], player.health)

    returned_info = (0, 0)
    prev_screen = returned_info[0]
    next_screen = returned_info[1]

    looted_chests = [False for screen in range(4)]

    while True:

        if next_screen is 0:
            returned_info = title_screen(screen, clock)

        elif next_screen is 1:
            if prev_screen is 0:
                # stop any music that is playing, and play the forest music in a loop
                pygame.mixer.stop()
                scarlet_forest = pygame.mixer.Sound("Audio/scarlet_forest.ogg")
                scarlet_forest.play(-1)
                returned_info = forest_entrance(screen, clock, spritesheet, player, hud, (704, 608), enemies_list[0], arrow_image)
            elif prev_screen is 2:
                returned_info = forest_entrance(screen, clock, spritesheet, player, hud, (0, 256), enemies_list[0], arrow_image)
            elif prev_screen is 3:
                returned_info = forest_entrance(screen, clock, spritesheet, player, hud, (704, 0), enemies_list[0], arrow_image)

        elif next_screen is 2:
            if prev_screen is 1:
                returned_info = southwestern_forest(screen, clock, spritesheet, player, hud, (1120, 256), enemies_list[1], arrow_image, looted_chests[0])

        elif next_screen is 3:
            if prev_screen is 1:
                returned_info = eastern_forest(screen, clock, spritesheet, player, hud, (704, 608), enemies_list[2], arrow_image, looted_chests[1])
            elif prev_screen is 4:
                returned_info = eastern_forest(screen, clock, spritesheet, player, hud, (416, 0), enemies_list[2], arrow_image, looted_chests[1])
            elif prev_screen is 5:
                returned_info = eastern_forest(screen, clock, spritesheet, player, hud, (0, 512), enemies_list[2], arrow_image, looted_chests[1])

        elif next_screen is 4:
            if prev_screen is 3:
                returned_info = northern_forest(screen, clock, spritesheet, player, hud, (416, 608), enemies_list[3], arrow_image, looted_chests[2])

        elif next_screen is 5:
            if prev_screen is 3:
                returned_info = western_forest(screen, clock, spritesheet, player, hud, (1120, 512), enemies_list[4], arrow_image, looted_chests[3])

        elif next_screen is 6:
            if prev_screen is 5:
                returned_info = cave(screen, clock, spritesheet, player, hud, (562, 608), enemies_list[5], arrow_image)

        elif next_screen is 7:
            if prev_screen is 6:

                screen.fill((0, 0, 0))

                victory_fanfare = pygame.mixer.Sound("Audio/fanfare.ogg")

                font = pygame.font.SysFont("calibri", 50, True)
                text = font.render("CONGRATULATIONS! YOU WIN!", True, (50, 255, 0))
                screen.blit(text, (250, 375))

                pygame.display.flip()

                victory_fanfare.play()
                pygame.time.delay(12000)

                returned_info = (7, 0)

        elif next_screen is 8:

            screen.fill((0, 0, 0))

            pygame.mixer.stop()

            font = pygame.font.SysFont("calibri", 50, True)
            text = font.render("YOU DIED...", True, (200, 0, 0))
            screen.blit(text, (475, 400))

            pygame.display.flip()

            pygame.time.delay(4000)

            player.health = player.total_health

            returned_info = (0, 1)

        if returned_info is -1:
            break

        prev_screen = returned_info[0]
        next_screen = returned_info[1]
        if not prev_screen in (0, 1, 6, 7, 8):
            looted_chests[prev_screen - 2] = returned_info[2]

    pygame.quit()
    print("Thanks for playing!")


if __name__ == "__main__":
    pygame.init()

    # call the screen handler function used to load screens
    screen_handler()
