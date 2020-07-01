import pygame
import pygame_menu
import time

# !/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
pantalla = pygame.display.set_mode((280, 550))

reloj = pygame.time.Clock()
hecho = False
imagen = pygame.image.load("img/menu.png")

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        pantalla.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), pantalla, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(pantalla, (255, 0, 0), button_1)
        pygame.draw.rect(pantalla, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        pantalla.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), pantalla, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        pantalla.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), pantalla, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
pygame.init()



font = pygame.font.SysFont("quando", 50)
pygame.display.set_caption("Harry Potter Quidditch")
text = font.render("Hola, Mundo", True, (0, 139, 139))

while not hecho:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hecho = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            hecho = True

    pantalla.fill((255, 255, 255))
    pantalla.blit(text, ((280 - text.get_width()) // 2, (550 - text.get_height()) // 3))
    pantalla.blit(imagen, (0, 0))
    pygame.display.update()
    time.sleep(5)

    def start_the_game():
        """
            Function that starts a game. This is raised by the menu button,
            here menu can be disabled, etc.
            """
        print('Do the job here !')


    menu = pygame_menu.Menu(height=280,
                            width=280,
                            title='Harry Potter')

    menu.add_button('Play', start_the_game)
    menu.add_button('Ranking', start_the_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    pygame.display.flip()
    if __name__ == '__main__':
        menu.mainloop(pantalla)
    reloj.tick(60)


