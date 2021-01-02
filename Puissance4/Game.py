from IAMinMax import *
from Player import *
from Board import *
import random


class Game:
    def __init__(self,  commandLine=False, playerOnly=False, iaDepth=5):
        self.__board = Board()
        if(playerOnly and not commandLine):
            raise NotImplementedError
        if(playerOnly):
            self.__players = [
                Player(1, commandLine),
                Player(2, commandLine)
            ]
        else:
            self.__players = [
                Player(1, commandLine),
                IAMinMax(2, iaDepth)
            ]
        self.__turn = random.randint(0, 1)
        self.__playing = True

    def run(self):
        """
        Résultat :
            Joue une partie de Puissance4
        """
        while(self.__playing):
            played = False
            col = 0
            while(not played):
                col = self.__players[self.__turn].play(self.__board)
                if(self.__board.isValid(col)):
                    played = True
            hasWon = self.__board.placePawn(
                self.__players[self.__turn].getId(), col)
            self.__board.printBoard()
            if(hasWon):
                print("Gagnant : ", self.__players[self.__turn].getId())
                self.__playing = False
            if(self.__turn == 0):
                self.__turn = 1
            else:
                self.__turn = 0
