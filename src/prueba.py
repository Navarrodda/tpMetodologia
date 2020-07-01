
import sys

sys.path.insert(0, '../../')

import os
import pygame
import pygame_menu

FPS = 60.0
WINDOW_SIZE = (280, 550)

sound = None  # type: pygame_menu.sound.Sound
surface = None  # type: pygame.Surface
main_menu = None  # type: pygame_menu.Menu


background_image = pygame_menu.baseimage.BaseImage(
    image_path="img/menu.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

def main_background():
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.

    :return: None
    """
    background_image.draw(surface)


def main(test=False):
    """
    Main program.

    :param test: Indicate function is being tested
    :type test: bool
    :return: None
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global main_menu
    global sound
    global surface

    # -------------------------------------------------------------------------
    # Init pygame
    # -------------------------------------------------------------------------
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Create pygame screen and objects
    surface = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Menu')
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus: Main menu
    # -------------------------------------------------------------------------
    main_menu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    main_menu_theme.set_background_color_opacity(0.0)  # 50% opacity

    main_menu = pygame_menu.Menu(
        height=550,
        width=280,
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        title='Epic Menu',
        theme=main_menu_theme,
    )

    main_menu.add_button('Start Game', None)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Main menu
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()
