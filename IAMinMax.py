import copy
import time
from Player import Player

from lib_grovepi.LCD import *


class IAMinMax(Player):
    def __init__(self, id, depth):
        super().__init__(id)
        self.__depth = depth

    def play(self, board):
        """
        Pré-requis :
            board (Board) : Représente le plateau dans lequel l'IA doit jouer
        Résultat :
            Retourne la colonne choisie par l'IA grâce à un algorithme MinMax
        """
        bestScore = -10000
        colToPlay = 0
        start = time.time()
        for i in range(7):
            if(board.isValid(i)):
                copyBoard = copy.deepcopy(board)
                copyBoard.placePawn(self.getId(), i)
                score = self.__minmax(
                    copyBoard, self.__depth, -10000, 10000, False)
                if(score > bestScore):
                    bestScore = score
                    colToPlay = i
        end = time.time()
        print("Temps d'éxécution IA : ", round(end - start, 2), " secondes")
        colString = "L'IA joue la\ncolonne : " + str(colToPlay + 1)
        setText(colString)
        time.sleep(1)
        return colToPlay

    def __minmax(self, board, depth, alpha, beta, maximizing):
        if(depth == 0 or board.isOver()):
            return board.getEvaluation()

        if(maximizing):
            maxEval = -10000
            for i in range(7):
                if(board.isValid(i)):
                    copyBoard = copy.deepcopy(board)
                    copyBoard.placePawn(self.getId(), i)
                    newEval = self.__minmax(
                        copyBoard, depth - 1, alpha, beta, False)
                    maxEval = max(maxEval, newEval)
                    alpha = max(alpha, newEval)
                    if (beta <= alpha):
                        break
            return maxEval
        else:
            minEval = 10000
            for i in range(7):
                if(board.isValid(i)):
                    copyBoard = copy.deepcopy(board)
                    copyBoard.placePawn(1, i)
                    newEval = self.__minmax(
                        copyBoard, depth - 1, alpha, beta, True)
                    minEval = min(minEval, newEval)
                    beta = min(beta, newEval)
                    if(beta <= alpha):
                        break
            return minEval
