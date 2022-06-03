from Game import *
import pygame
import pygame_menu
from Menu import *

pygame.init()
surface = pygame.display.set_mode((600, 400))

def refresh_and_lunch():
    print("im in")
    game = Game()
    game.start()


def main():
    menu = pygame_menu.Menu('Welcome', 600, 400,
                            theme=pygame_menu.themes.THEME_DARK)
    menu.add.text_input('Name : ')
    menu.add.button('Play', refresh_and_lunch)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    # game = Game()
    # game.start()
    menu.mainloop(surface)


if __name__ == "__main__":
    main()
