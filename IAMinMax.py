import math
import copy
import random


class IAMinMax:
    def __init__(self, id, depth):
        self.__id = id
        self.__depth = depth

    def getId(self):
        return self.__id

    def play(self, board):
        bestScore = -math.inf
        colToPlay = 0
        for i in range(7):
            if(board.isValid(i)):
                copyBoard = copy.deepcopy(board)
                copyBoard.placePawn(self, i)
                score = self.minmax(copyBoard, self.__depth, False)
                if(score > bestScore):
                    bestScore = score
                    colToPlay = i
        return colToPlay

    def minmax(self, board, depth, maximizing):
        if(depth == 0 or board.isOver()):
            return board.evaluation(self.__id)

        if(maximizing):
            maxEval = -math.inf
            for i in range(7):
                if(board.isValid(i)):
                    copyBoard = copy.deepcopy(board)
                    copyBoard.placePawn(self, i)
                    newEval = self.minmax(copyBoard, depth - 1, False)
                    maxEval = max(maxEval, newEval)
            return maxEval
        else:
            minEval = math.inf
            for i in range(7):
                if(board.isValid(i)):
                    copyBoard = copy.deepcopy(board)
                    copyBoard.placePawn(self, i)
                    newEval = self.minmax(copyBoard, depth - 1, True)
                    minEval = min(minEval, newEval)
            return minEval
