# Main Game Screens
# Mason Kury

from Level import *
from Entity import *


def forest_entrance(screen, clock, spritesheet, player, spawnpoint):
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

    # the foreground tileset to be drawn after the player (includes any interactive blocks, trees, rocks, etc.)
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

    # create a level object, and give it the two arrays created above
    forest_entrance = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = forest_entrance.get_collision_list()

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction

    # pygame timer event ID's used for activating events like animation and movement
    walking_animation_timer = pygame.USEREVENT + 1  # timer for walking frame animation
    walking_movement_timer = pygame.USEREVENT + 2   # timer for walking movement
    check_keypresses_timer = pygame.USEREVENT + 3   # timer for checking user keyboard input

    pygame.time.set_timer(check_keypresses_timer, 5)  # set the keypress check timer to run every 5 milliseconds

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False  # used to tell the screen when it is done (go back to screen_handler function)

    # MAIN GAME SCREEN LOOP
    while not done:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                done = True  # done with the screen

            # advance walking animation
            if event.type == walking_animation_timer:
                # get the next frame of the animation
                current_frame = player.animate()

            # advance actual positional movement
            if event.type == walking_movement_timer:
                # move the player based on their movement speed
                player.move()

            # check keypresses
            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()  # get the currently pressed keypresses

                # up is pressed
                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["up"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["up"] = True                              # set the up arrow state to True (pressed)

                # down is pressed
                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["down"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["down"] = True                            # set the down arrow state to True

                # right is pressed
                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["right"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["right"] = True                           # set the right arrow state to True

                # left is pressed
                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["left"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["left"] = True                            # set the right arrow state to True

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

                    pygame.time.set_timer(walking_movement_timer, 0)   # shut down the movement timer
                    pygame.time.set_timer(walking_animation_timer, 0)  # shut down the animation timer
                    current_frame = player.animate(True)               # set the current frame to the standing frame

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        # check for player collisions with the environment
        collided_with = player.hitbox.collidelist(collision_list)

        # player is colliding with a block
        if collided_with is not -1:
            player.collide(collision_list[collided_with])  # call the player collision function with the collided block

        screen.fill((255, 255, 255))  # (reset the screen with white)

        # draw the background layer, then the player, then the foreground layer
        forest_entrance.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        forest_entrance.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def southwestern_forest(screen, clock, spritesheet, player, spawnpoint):
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

    # create a level object, and give it the two arrays created above
    southwestern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = southwestern_forest.get_collision_list()

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction

    # pygame timer event ID's used for activating events like animation and movement
    walking_animation_timer = pygame.USEREVENT + 1  # timer for walking frame animation
    walking_movement_timer = pygame.USEREVENT + 2   # timer for walking movement
    check_keypresses_timer = pygame.USEREVENT + 3   # timer for checking user keyboard input

    pygame.time.set_timer(check_keypresses_timer, 5)  # set the keypress check timer to run every 5 milliseconds

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False  # used to tell the screen when it is done (go back to screen_handler function)

    # MAIN GAME SCREEN LOOP
    while not done:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                done = True  # done with the screen

            # advance walking animation
            if event.type == walking_animation_timer:
                # get the next frame of the animation
                current_frame = player.animate()

            # advance actual positional movement
            if event.type == walking_movement_timer:
                # move the player based on their movement speed
                player.move()

            # check keypresses
            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()  # get the currently pressed keypresses

                # up is pressed
                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["up"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["up"] = True                              # set the up arrow state to True (pressed)

                # down is pressed
                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["down"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["down"] = True                            # set the down arrow state to True

                # right is pressed
                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["right"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["right"] = True                           # set the right arrow state to True

                # left is pressed
                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["left"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["left"] = True                            # set the right arrow state to True

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

                    pygame.time.set_timer(walking_movement_timer, 0)   # shut down the movement timer
                    pygame.time.set_timer(walking_animation_timer, 0)  # shut down the animation timer
                    current_frame = player.animate(True)               # set the current frame to the standing frame

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        # check for player collisions with the environment
        collided_with = player.hitbox.collidelist(collision_list)

        # player is colliding with a block
        if collided_with is not -1:
            player.collide(collision_list[collided_with])  # call the player collision function with the collided block

        screen.fill((255, 255, 255))  # (reset the screen with white)

        # draw the background layer, then the player, then the foreground layer
        southwestern_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        southwestern_forest.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def eastern_forest(screen, clock, spritesheet, player, spawnpoint, has_bow):
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

        has_bow: must be a boolean; tells the screen whether to draw the rock barrier in the West, to prevent
        the player from advancing without collecting and practicing with the bow.

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

    # if the player has acquired the bow and arrow, remove the blockade of rocks
    if has_bow:
        fg_array[15][2] = 11
        fg_array[16][2] = 0
        fg_array[17][2] = 4

    # create a level object, and give it the two arrays created above
    eastern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = eastern_forest.get_collision_list()

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction

    # pygame timer event ID's used for activating events like animation and movement
    walking_animation_timer = pygame.USEREVENT + 1  # timer for walking frame animation
    walking_movement_timer = pygame.USEREVENT + 2   # timer for walking movement
    check_keypresses_timer = pygame.USEREVENT + 3   # timer for checking user keyboard input

    pygame.time.set_timer(check_keypresses_timer, 5)  # set the keypress check timer to run every 5 milliseconds

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False  # used to tell the screen when it is done (go back to screen_handler function)

    # MAIN GAME SCREEN LOOP
    while not done:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                done = True  # done with the screen

            # advance walking animation
            if event.type == walking_animation_timer:
                # get the next frame of the animation
                current_frame = player.animate()

            # advance actual positional movement
            if event.type == walking_movement_timer:
                # move the player based on their movement speed
                player.move()

            # check keypresses
            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()  # get the currently pressed keypresses

                # up is pressed
                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["up"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["up"] = True                              # set the up arrow state to True (pressed)

                # down is pressed
                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["down"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["down"] = True                            # set the down arrow state to True

                # right is pressed
                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["right"]:
                        current_frame = player.animate()                      # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)     # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer,  200)  # set the animation timer for every 200 ms
                        arrow_keys["right"] = True                            # set the right arrow state to True

                # left is pressed
                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["left"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["left"] = True                            # set the right arrow state to True

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

                    pygame.time.set_timer(walking_movement_timer, 0)   # shut down the movement timer
                    pygame.time.set_timer(walking_animation_timer, 0)  # shut down the animation timer
                    current_frame = player.animate(True)               # set the current frame to the standing frame

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        # check for player collisions with the environment
        collided_with = player.hitbox.collidelist(collision_list)

        # player is colliding with a block
        if collided_with is not -1:
            player.collide(
                collision_list[collided_with])  # call the player collision function with the collided block

        screen.fill((255, 255, 255))  # (reset the screen with white)

        # draw the background layer, then the player, then the foreground layer
        eastern_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        eastern_forest.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def northern_forest(screen, clock, spritesheet, player, spawnpoint):
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

    # create a level object, and give it the two arrays created above
    northern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = northern_forest.get_collision_list()

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction

    # pygame timer event ID's used for activating events like animation and movement
    walking_animation_timer = pygame.USEREVENT + 1  # timer for walking frame animation
    walking_movement_timer = pygame.USEREVENT + 2  # timer for walking movement
    check_keypresses_timer = pygame.USEREVENT + 3  # timer for checking user keyboard input

    pygame.time.set_timer(check_keypresses_timer, 5)  # set the keypress check timer to run every 5 milliseconds

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False  # used to tell the screen when it is done (go back to screen_handler function)

    # MAIN GAME SCREEN LOOP
    while not done:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                done = True  # done with the screen

            # advance walking animation
            if event.type == walking_animation_timer:
                # get the next frame of the animation
                current_frame = player.animate()

            # advance actual positional movement
            if event.type == walking_movement_timer:
                # move the player based on their movement speed
                player.move()

            # check keypresses
            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()  # get the currently pressed keypresses

                # up is pressed
                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["up"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["up"] = True                              # set the up arrow state to True (pressed)

                # down is pressed
                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["down"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["down"] = True                            # set the down arrow state to True

                # right is pressed
                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["right"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["right"] = True                           # set the right arrow state to True

                # left is pressed
                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["left"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["left"] = True                            # set the right arrow state to True

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

                    pygame.time.set_timer(walking_movement_timer, 0)   # shut down the movement timer
                    pygame.time.set_timer(walking_animation_timer, 0)  # shut down the animation timer
                    current_frame = player.animate(True)               # set the current frame to the standing frame

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        # check for player collisions with the environment
        collided_with = player.hitbox.collidelist(collision_list)

        # player is colliding with a block
        if collided_with is not -1:
            player.collide(collision_list[collided_with])  # call the player collision function with the collided block

        screen.fill((255, 255, 255))  # (reset the screen with white)

        # draw the background layer, then the player, then the foreground layer
        northern_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        northern_forest.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def western_forest(screen, clock, spritesheet, player, spawnpoint):
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

    # create a level object, and give it the two arrays created above
    western_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = western_forest.get_collision_list()

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction

    # pygame timer event ID's used for activating events like animation and movement
    walking_animation_timer = pygame.USEREVENT + 1  # timer for walking frame animation
    walking_movement_timer = pygame.USEREVENT + 2  # timer for walking movement
    check_keypresses_timer = pygame.USEREVENT + 3  # timer for checking user keyboard input

    pygame.time.set_timer(check_keypresses_timer, 5)  # set the keypress check timer to run every 5 milliseconds

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False  # used to tell the screen when it is done (go back to screen_handler function)

    # MAIN GAME SCREEN LOOP
    while not done:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                done = True  # done with the screen

            # advance walking animation
            if event.type == walking_animation_timer:
                # get the next frame of the animation
                current_frame = player.animate()

            # advance actual positional movement
            if event.type == walking_movement_timer:
                # move the player based on their movement speed
                player.move()

            # check keypresses
            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()  # get the currently pressed keypresses

                # up is pressed
                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["up"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["up"] = True                              # set the up arrow state to True (pressed)

                # down is pressed
                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["down"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["down"] = True                            # set the down arrow state to True

                # right is pressed
                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["right"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["right"] = True                           # set the right arrow state to True

                # left is pressed
                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["left"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["left"] = True                            # set the right arrow state to True

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

                    pygame.time.set_timer(walking_movement_timer, 0)   # shut down the movement timer
                    pygame.time.set_timer(walking_animation_timer, 0)  # shut down the animation timer
                    current_frame = player.animate(True)               # set the current frame to the standing frame

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        # check for player collisions with the environment
        collided_with = player.hitbox.collidelist(collision_list)

        # player is colliding with a block
        if collided_with is not -1:
            player.collide(collision_list[collided_with])  # call the player collision function with the collided block

        screen.fill((255, 255, 255))  # (reset the screen with white)

        # draw the background layer, then the player, then the foreground layer
        western_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        western_forest.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def cave(screen, clock, spritesheet, player, spawnpoint):
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

    # create a level object, and give it the two arrays created above
    cave = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = cave.get_collision_list()

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    current_frame = player.animate(True)  # get a still frame of the player standing in the current direction

    # pygame timer event ID's used for activating events like animation and movement
    walking_animation_timer = pygame.USEREVENT + 1  # timer for walking frame animation
    walking_movement_timer = pygame.USEREVENT + 2  # timer for walking movement
    check_keypresses_timer = pygame.USEREVENT + 3  # timer for checking user keyboard input

    pygame.time.set_timer(check_keypresses_timer, 5)  # set the keypress check timer to run every 5 milliseconds

    # create a dictionary that will be used to tell which keys are currently being pressed.
    # this is used because I want the player to orient himself and set movement/animation timers only once, but
    # keep setting his direction while the key is pressed. This also helps to determine when no arrow keys are pressed,
    # so that the player movement/animation timers can be stopped, as well as the animation and movement itself.
    arrow_keys = {"up": False, "down": False, "right": False, "left": False}

    done = False  # used to tell the screen when it is done (go back to screen_handler function)

    # MAIN GAME SCREEN LOOP
    while not done:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                done = True  # done with the screen

            # advance walking animation
            if event.type == walking_animation_timer:
                # get the next frame of the animation
                current_frame = player.animate()

            # advance actual positional movement
            if event.type == walking_movement_timer:
                # move the player based on their movement speed
                player.move()

            # check keypresses
            if event.type == check_keypresses_timer:

                keys_pressed = pygame.key.get_pressed()  # get the currently pressed keypresses

                # up is pressed
                if keys_pressed[pygame.K_UP]:
                    player.direction = "up"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["up"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["up"] = True                              # set the up arrow state to True (pressed)

                # down is pressed
                elif keys_pressed[pygame.K_DOWN]:
                    player.direction = "down"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["down"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["down"] = True                            # set the down arrow state to True

                # right is pressed
                elif keys_pressed[pygame.K_RIGHT]:
                    player.direction = "right"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["right"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["right"] = True                           # set the right arrow state to True

                # left is pressed
                elif keys_pressed[pygame.K_LEFT]:
                    player.direction = "left"  # update the player direction

                    # only run on the actual keypress:
                    if not arrow_keys["left"]:
                        current_frame = player.animate()                     # orient the player with a new frame
                        pygame.time.set_timer(walking_movement_timer, 50)    # set the movement timer for every 50 ms
                        pygame.time.set_timer(walking_animation_timer, 200)  # set the animation timer for every 200 ms
                        arrow_keys["left"] = True                            # set the right arrow state to True

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

                    pygame.time.set_timer(walking_movement_timer, 0)   # shut down the movement timer
                    pygame.time.set_timer(walking_animation_timer, 0)  # shut down the animation timer
                    current_frame = player.animate(True)               # set the current frame to the standing frame

            # keys that should only register once when pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    player.dodge()

        # check for player collisions with the environment
        collided_with = player.hitbox.collidelist(collision_list)

        # player is colliding with a block
        if collided_with is not -1:
            player.collide(collision_list[collided_with])  # call the player collision function with the collided block

        screen.fill((255, 255, 255))  # (reset the screen with white)

        # draw the background layer, then the player, then the foreground layer
        cave.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        cave.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def screen_handler(screen, clock, spritesheet, player):
    """Handles which screens should be called, and anything that goes on in between."""

    # stop any music that is playing, and play the forest music in a loop
    pygame.mixer.stop()
    scarlet_forest = pygame.mixer.Sound("Audio/scarlet_forest.ogg")
    scarlet_forest.play(-1)

    # currently for debugging purposes -- draws the next logical screen after one has been closed
    forest_entrance(screen, clock, spritesheet, player, (704, 608))
    southwestern_forest(screen, clock, spritesheet, player, (1120, 256))
    forest_entrance(screen, clock, spritesheet, player, (0, 256))
    eastern_forest(screen, clock, spritesheet, player, (704, 608), False)
    northern_forest(screen, clock, spritesheet, player, (416, 608))
    eastern_forest(screen, clock, spritesheet, player, (416, 0), True)
    western_forest(screen, clock, spritesheet, player, (1120, 512))

    # stop any misc that is playing, and play some boss music! (in a loop)
    pygame.mixer.stop()
    rude_buster = pygame.mixer.Sound("Audio/rude_buster.ogg")
    rude_buster.play(-1)

    cave(screen, clock, spritesheet, player, (562, 608))


if __name__ == "__main__":
    pygame.init()

    # set the screen size and create a surface
    size = (1152, 850)
    screen = pygame.display.set_mode(size)

    # load the tileset and entity spritesheet
    spritesheet = pygame.image.load("Images/spritesheet.png").convert_alpha()

    pygame.display.set_caption("Forest Adventure")  # set the caption on the top of the window
    # SET ICON

    clock = pygame.time.Clock()  # create a clock object used to control the drawing rate

    # load animation strips from the spritesheet
    player_south_sword_walking = get_frames(spritesheet, (0, 128, 128, 32), 32)
    player_north_sword_walking = get_frames(spritesheet, (128, 128, 128, 32), 32)
    player_east_sword_walking = get_frames(spritesheet, (0, 160, 128, 32), 32)
    player_west_sword_walking = get_frames(spritesheet, (128, 160, 128, 32), 32)

    # put the animations into a list
    animations = [player_north_sword_walking, player_south_sword_walking,
                  player_west_sword_walking, player_east_sword_walking]

    # create the player using the animations as well as a bunch of other stats
    player = Player(7, 20, pygame.Rect(16, 16, 32, 32), pygame.Rect(0, 0, 64, 64), "up", 5, animations)

    # call the screen handler function used to load screens
    screen_handler(screen, clock, spritesheet, player)
