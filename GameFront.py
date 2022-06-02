import os

import pygame

from Board import *


class GameFront:
    IMAGE_DIRECTORY = "images"

    def __init__(self):
        self.gamer = 1
        self.gameBoard = Board()
        self.gameBoard.feed_board()

        self.pyGame = pygame

        pygame.init()

        self.board_picture = pygame.image.load(os.path.join(GameFront.IMAGE_DIRECTORY, "plateau.png"))

        taille_plateau_de_jeu = self.board_picture.get_size()
        self.size = (taille_plateau_de_jeu[0] * 1, taille_plateau_de_jeu[1])
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.board_picture, (0, 0))
        pygame.display.flip()

        self.yellowChip = pygame.image.load(os.path.join(GameFront.IMAGE_DIRECTORY, "pion_jaune.png"))
        self.redChip = pygame.image.load(os.path.join(GameFront.IMAGE_DIRECTORY, "pion_rouge.png"))
        # self.font = pygame.font.Font("freesansbold.ttf", 15)

    def determine_column(self, x):

        column = x - 16
        column = column / 97
        if column in range(0, 7):
            if self.gameBoard.board[5][int(column)] == 0:
                game_board_state = False
        return int(column)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.board_picture, (0, 0))
        game_board_game_state = self.gameBoard.reverse_game_board()

        self.gameBoard.show()

        for i in range(len(game_board_game_state)):
            for j in range(len(game_board_game_state[i])):
                if game_board_game_state[i][j] == Board.YELLOW:
                    self.screen.blit(self.yellowChip, (16 + 97 * j, 13 - 97.5 * i + 486))
                pygame.display.flip()
                if game_board_game_state[i][j] == Board.RED:
                    self.screen.blit(self.redChip, (16 + 97 * j, 13 - 97.5 * i + 486))
                pygame.display.flip()
