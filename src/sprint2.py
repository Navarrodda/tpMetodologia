
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

background_button= pygame_menu.baseimage.BaseImage(
    image_path="img/StartGame.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

background_instructions= pygame_menu.baseimage.BaseImage(
    image_path="img/Instrucciones.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

background_game= pygame_menu.baseimage.BaseImage(
    image_path="img/fondoGame.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

background_button_goback= pygame_menu.baseimage.BaseImage(
    image_path="img/GoBack.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

background_button_continue= pygame_menu.baseimage.BaseImage(
    image_path="img/Continue.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)


def main_background():

    background_image.draw(surface)

def main(test=False):

    # -------------------------------------------------------------------------
    # Global
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
    # Start Game
    # -------------------------------------------------------------------------
    game_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    game_theme.set_background_color_opacity(0.0)  # 50% opacity
    game_theme.background_color = background_game

    game_submenu = pygame_menu.Menu(
        height=550,
        theme=game_theme,
        title='',
        center_content=True,
        width=280,
    )

    # -------------------------------------------------------------------------
    # Create menu: Instructions
    # -------------------------------------------------------------------------
    instructions_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    instructions_theme.set_background_color_opacity(0.0)  # 50% opacity
    instructions_theme.background_color=background_instructions

    instructions_menu = pygame_menu.Menu(
        height=550,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        theme=instructions_theme,
        title='',
        center_content=True,
        columns=2,
        rows=9,
        width=280,
    )

    #   COLUMNA 1
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button('           ', pygame_menu.events.BACK , background_color=background_button_goback)

    #   COLUMNA 2
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button(' ', None)
    instructions_menu.add_button('           ', game_submenu , background_color=background_button_continue)

    # -------------------------------------------------------------------------
    # Create menus: Main menu
    # -------------------------------------------------------------------------

    main_menu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    main_menu_theme.set_background_color_opacity(0.0)  # 50% opacity

    main_menu = pygame_menu.Menu(
        height=550,
        width=280,
        onclose=pygame_menu.events.DISABLE_CLOSE,  # User press ESC button
        title='  ',
        mouse_enabled=True,
        theme=main_menu_theme,
    )

    main_menu.add_button('                  ', instructions_menu, background_color=background_button)#StartGameButton

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
