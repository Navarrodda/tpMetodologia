import pygame
import pygame_menu
import time

pygame.init()

pantalla = pygame.display.set_mode((280, 550))
reloj = pygame.time.Clock()
hecho = False
imagen = pygame.image.load("img/menu.png")

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


