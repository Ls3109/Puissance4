import sys
import time
import random

from GameFront import *
from Board import *


class Game:
    NUMBER_OF_CHIPS = 42

    def __init__(self):
        self.gamer = 1
        self.playedChips = 0
        self.potentialWinner = False
        self.gameFront = GameFront()

    def whoPlay(self):
        # Cette fonction retourne le numero du joueur qui doit jouer
        if self.playedChips % 2 == 0:
            color = Board.YELLOW
        else:
            color = Board.RED
        return color

    def display_winner(self):
        if self.gamer == "" or self.gamer is None:
            return "personne n'a gagne"
        else:
            return self.gamer + " won"

    def start(self):
        while self.potentialWinner != "yellow" \
                and self.potentialWinner != "red" \
                and self.playedChips < Game.NUMBER_OF_CHIPS:
            time.sleep(0.05)
            for event in self.gameFront.pyGame.event.get():

                self.gameFront.gameBoard.show()

                if event.type == self.gameFront.pyGame.MOUSEBUTTONUP:
                    x, y = self.gameFront.pyGame.mouse.get_pos()
                    gamer = self.whoPlay()
                    column = self.gameFront.determine_column(x)
                    self.gameFront.gameBoard.put_chip(column, 1)
                    self.playedChips = self.playedChips + 1
                    self.potentialWinner = self.gameFront.gameBoard.check_win()
                    print("Winner : " + str(self.potentialWinner))
                    check = True
                    while check:
                        x = random.randint(0, 6)
                        if self.gameFront.gameBoard.check_column_place(x):
                            self.gameFront.gameBoard.put_chip(x, -1)
                            check = False
                    self.potentialWinner = self.gameFront.gameBoard.check_win()
                    print("Winner : " + str(self.potentialWinner))
                    self.gameFront.render()
                    self.gameFront.pyGame.display.flip()

                if event.type == self.gameFront.pyGame.QUIT:
                    sys.exit(0)
