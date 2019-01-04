# Main Game Screens
# Mason Kury

from Level import *
from Entity import *


def forest_entrance(screen, clock, spritesheet, player, hud, spawnpoint):
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

    # MAIN GAME SCREEN LOOP
    while True:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                return -1

            # advance walking animation
            if event.type == walking_animation_timer and not showing_sign:
                # get the next frame of the animation
                current_frame = player.animate()

            # advance actual positional movement
            if event.type == walking_movement_timer and not showing_sign:
                # move the player based on their movement speed
                player.move()

            # check keypresses
            if event.type == check_keypresses_timer and not showing_sign:

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
                if event.key == pygame.K_LCTRL and not showing_sign:
                    player.dodge()

                elif event.key == pygame.K_ESCAPE:
                    showing_sign = False

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

                elif block_type is 4:
                    return 1, 2  # go to screen 2
                elif block_type is 5:
                    return 1, 3  # go to screen 3
                else:
                    player.collide(collision_list[block])

        screen.fill((255, 255, 255))  # (reset the screen with white)

        hud.draw(screen, (0, 640))

        # draw the background layer, then the player, then the foreground layer
        forest_entrance.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        forest_entrance.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        if showing_sign:
            pygame.draw.rect(screen, (100, 100, 25), (100, 50, 950, 500))
            for line in sign_text:
                current_text = font.render(line, True, (0, 0, 0))
                screen.blit(current_text, (120, 100 + (50 * sign_text.index(line))))

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def southwestern_forest(screen, clock, spritesheet, player, hud, spawnpoint):
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

    # rectangles touching the borders of the game screen; used to stop the player from getting out of the map
    screen_boundaries = [pygame.Rect(0, -32, 1152, 32), pygame.Rect(0, 640, 1152, 32),
                         pygame.Rect(-32, 0, 32, 640), pygame.Rect(1152, 0, 32, 640)]

    # create a level object, and give it the two arrays created above
    southwestern_forest = Level(spritesheet, 32, 256, bg_array, fg_array)
    # get a list of rectangles, corresponding to collideable blocks
    collision_list = southwestern_forest.get_collision_list()

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    entered_screen = False

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

    # MAIN GAME SCREEN LOOP
    while True:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                return -1

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
                if event.key == pygame.K_LCTRL:
                    player.dodge()

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

        for block in range(len(collision_list) - 1):
            if collision_list[block] is not None and player.hitbox.colliderect(collision_list[block]):

                row = block // len(southwestern_forest.collision_array[0])
                column = block % len(southwestern_forest.collision_array[0])

                block_type = southwestern_forest.collision_array[row][column]

                if block_type is 4:
                    return 2, 1 # go to screen 1
                else:
                    player.collide(collision_list[block])

        screen.fill((255, 255, 255))  # (reset the screen with white)

        hud.draw(screen, (0, 640))

        # draw the background layer, then the player, then the foreground layer
        southwestern_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        southwestern_forest.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def eastern_forest(screen, clock, spritesheet, player, hud, spawnpoint, has_bow):
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

    # rectangles touching the borders of the game screen; used to stop the player from getting out of the map
    screen_boundaries = [pygame.Rect(0, -32, 1152, 32), pygame.Rect(0, 640, 1152, 32),
                         pygame.Rect(-32, 0, 32, 640), pygame.Rect(1152, 0, 32, 640)]

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

    entered_screen = False

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

    # MAIN GAME SCREEN LOOP
    while True:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                return -1

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
                if event.key == pygame.K_LCTRL:
                    player.dodge()

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

        for block in range(len(collision_list) - 1):
            if collision_list[block] is not None and player.hitbox.colliderect(collision_list[block]):

                row = block // len(eastern_forest.collision_array[0])
                column = block % len(eastern_forest.collision_array[0])

                block_type = eastern_forest.collision_array[row][column]

                if block_type is 4:
                    return 3, 1  # go to screen 1
                elif block_type is 5:
                    return 3, 4  # go to screen 4
                elif block_type is 6:
                    return 3, 5  # go to screen 5
                else:
                    player.collide(collision_list[block])

        screen.fill((255, 255, 255))  # (reset the screen with white)

        hud.draw(screen, (0, 640))

        # draw the background layer, then the player, then the foreground layer
        eastern_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        eastern_forest.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def northern_forest(screen, clock, spritesheet, player, hud, spawnpoint):
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

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    entered_screen = False

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

    # MAIN GAME SCREEN LOOP
    while True:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                return -1

            # advance walking animation
            if event.type == walking_animation_timer and not showing_sign:
                # get the next frame of the animation
                current_frame = player.animate()

            # advance actual positional movement
            if event.type == walking_movement_timer and not showing_sign:
                # move the player based on their movement speed
                player.move()

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
                if event.key == pygame.K_LCTRL and not showing_sign:
                    player.dodge()

                elif event.key == pygame.K_ESCAPE:
                    showing_sign = False

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

                elif block_type is 4:
                    return 4, 3  # go to screen 3
                else:
                    player.collide(collision_list[block])

        screen.fill((255, 255, 255))  # (reset the screen with white)

        hud.draw(screen, (0, 640))

        # draw the background layer, then the player, then the foreground layer
        northern_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        northern_forest.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        if showing_sign:
            pygame.draw.rect(screen, (100, 100, 25), (100, 50, 950, 500))
            for line in sign_text:
                current_text = font.render(line, True, (0, 0, 0))
                screen.blit(current_text, (120, 100 + (50 * sign_text.index(line))))

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def western_forest(screen, clock, spritesheet, player, hud, spawnpoint):
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

    # spawn in the player at the specified coordinates
    player.hitbox.x = spawnpoint[0]
    player.hitbox.y = spawnpoint[1]
    player.align_sword_swing()  # align the secondary sword hitbox to be centered with the player hitbox

    entered_screen = False

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

    # MAIN GAME SCREEN LOOP
    while True:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                return -1

            # advance walking animation
            if event.type == walking_animation_timer and not showing_sign:
                # get the next frame of the animation
                current_frame = player.animate()

            # advance actual positional movement
            if event.type == walking_movement_timer and not showing_sign:
                # move the player based on their movement speed
                player.move()

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
                if event.key == pygame.K_LCTRL and not showing_sign:
                    player.dodge()

                elif event.key == pygame.K_ESCAPE:
                    showing_sign = False

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

                elif block_type is 4:
                    return 5, 3  # go to screen 3
                elif block_type is 5:
                    return 5, 6  # go to screen 6
                else:
                    player.collide(collision_list[block])

        screen.fill((255, 255, 255))  # (reset the screen with white)

        hud.draw(screen, (0, 640))

        # draw the background layer, then the player, then the foreground layer
        western_forest.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        western_forest.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        if showing_sign:
            pygame.draw.rect(screen, (100, 100, 25), (100, 50, 950, 500))
            for line in sign_text:
                current_text = font.render(line, True, (0, 0, 0))
                screen.blit(current_text, (120, 100 + (50 * sign_text.index(line))))

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def cave(screen, clock, spritesheet, player, hud, spawnpoint):
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

    # MAIN GAME SCREEN LOOP
    while True:

        # parse pygame events
        for event in pygame.event.get():

            # user clicked exit
            if event.type == pygame.QUIT:
                return -1

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
                if event.key == pygame.K_LCTRL:
                    player.dodge()

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

        for boundary in screen_boundaries:
            if player.hitbox.colliderect(boundary):
                player.collide(boundary)

        for block in range(len(collision_list) - 1):
            if collision_list[block] is not None and player.hitbox.colliderect(collision_list[block]):

                row = block // len(cave.collision_array[0])
                column = block % len(cave.collision_array[0])

                block_type = cave.collision_array[row][column]

                player.collide(collision_list[block])

        screen.fill((255, 255, 255))  # (reset the screen with white)

        hud.draw(screen, (0, 640))

        # draw the background layer, then the player, then the foreground layer
        cave.draw_bg(screen)
        screen.blit(current_frame, (player.hitbox.x, player.hitbox.y))
        cave.draw_fg(screen)

        # (FOR DEBUGGING PURPOSES) draw the player hitbox, and the player sword swing
        pygame.draw.rect(screen, (255, 0, 0), player.hitbox, 2)
        pygame.draw.rect(screen, (0, 255, 0), player.sword_swing, 2)

        clock.tick(60)  # limit screen updates to 60 fps

        pygame.display.flip()  # update the screen with what has just been drawn


def screen_handler(screen, clock, spritesheet, hud_elements, player, hud):
    """Handles which screens should be called, and anything that goes on in between."""

    # stop any music that is playing, and play the forest music in a loop
    pygame.mixer.stop()
    scarlet_forest = pygame.mixer.Sound("Audio/scarlet_forest.ogg")
    scarlet_forest.play(-1)

    returned_info = (0, 1)
    prev_screen = returned_info[0]
    next_screen = returned_info[1]

    while True:

        if next_screen is 1:
            if prev_screen is 0:
                returned_info = forest_entrance(screen, clock, spritesheet, player, hud, (704, 608))
            elif prev_screen is 2:
                returned_info = forest_entrance(screen, clock, spritesheet, player, hud, (0, 256))
            elif prev_screen is 3:
                returned_info = forest_entrance(screen, clock, spritesheet, player, hud, (704, 0))

        elif next_screen is 2:
            if prev_screen is 1:
                returned_info = southwestern_forest(screen, clock, spritesheet, player, hud, (1120, 256))

        elif next_screen is 3:
            if prev_screen is 1:
                returned_info = eastern_forest(screen, clock, spritesheet, player, hud, (704, 608), False)
            elif prev_screen is 4:
                returned_info = eastern_forest(screen, clock, spritesheet, player, hud, (416, 0), True)
            elif prev_screen is 5:
                returned_info = eastern_forest(screen, clock, spritesheet, player, hud, (0, 512), True)

        elif next_screen is 4:
            if prev_screen is 3:
                returned_info = northern_forest(screen, clock, spritesheet, player, hud, (416, 608))

        elif next_screen is 5:
            if prev_screen is 3:
                returned_info = western_forest(screen, clock, spritesheet, player, hud, (1120, 512))

        elif next_screen is 6:
            if prev_screen is 5:
                returned_info = cave(screen, clock, spritesheet, player, hud, (562, 608))

        if returned_info is -1:
            break

        prev_screen = returned_info[0]
        next_screen = returned_info[1]

    pygame.quit()
    print("Thanks for playing!")


if __name__ == "__main__":
    pygame.init()

    # set the screen size and create a surface
    size = (1152, 850)
    screen = pygame.display.set_mode(size)

    # load the tileset and entity spritesheet
    spritesheet = pygame.image.load("Images/spritesheet.png").convert_alpha()
    hud_elements = pygame.image.load("Images/hud_elements.png").convert_alpha()

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

    # create a hud using the hud_elements spritesheet and stats from the player
    hud = HUD(hud_elements, pygame.Rect(0, 0, 1152, 210), player.inventory.inventory_dict,
              player.inventory.current_item, "SAMPLE TEXT", player.health)

    # call the screen handler function used to load screens
    screen_handler(screen, clock, spritesheet, hud_elements, player, hud)
