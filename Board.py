
class Board:
    def __init__(self):
        self.__board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.__isOver = False
        self.__evaluation = 0

    def getEvaluation(self):
        return self.__evaluation

    def isOver(self):
        """
        Résultat : Retourne True si la partie est finie, False sinon
        """
        return self.__isOver

    def __returnEval(self, count):
        """
        Pré-requis : 
            count (Int) : Représente la taille de l'alignement
        Résultat : 
            Retourne l'evaluation assignée a la taille de l'alignement
        """
        options = {1: 1, 2: 5, 3: 50, 4: 1000}
        return options[count]

    def printBoard(self):
        """
        Résultat : Affiche le plateau
        """
        print("\n")
        for i in range(6):
            print(self.__board[i])

    def isValid(self, col):
        """
        Pré-requis : 
            col (Int) : Représente une colonne du plateau
        Résultat :
            Retourne true si un pion peut être placé dans la colonne, false sinon
        """
        return self.__board[0][col] == 0

    def placePawn(self, idPlayer, col):
        """
        Pré-requis : 
            idPlayer (Int) : Représente l'id du joueur qui place son pion
            col (Int) : Représente la colonne dans laquelle le pion va être placée
        Résultat : 
            Place le pion du joueur donné dans la colonne donnée, puis retourne l'état de la partie :
            True si la partie est terminée et donc que le joueur a gagné, false sinon
        """
        i = 5
        while(i >= 0 and self.__board[i][col] != 0):
            i = i-1

        self.__board[i][col] = idPlayer

        # Detecte si ya une victoire
        hasWon = self.detectWin(idPlayer, col, i)

        return hasWon

    def compare(self, boardTab):
        """
        Pré-requis :
            boardTab ( [[int]] ) : Représente la liste à 2 dimensions à comparer
        Résultat :
            Compare le plateau de jeu en mémoire avec le plateau de jeu donné en paramètre et retourne la liste des différences (Liste vide si aucune différence)
        """
        tabDiff = []
        for i in range(6):
            for j in range(7):
                if(self.__board[i][j] != boardTab[i][j]):
                    tabDiff.append((i, j))
        return tabDiff

    # Test l'alignement possible dans la direction donné
    def alignement(self, idPlayer, col, ligne, pasLigne, pasCol):
        """
        Pré-requis:
            idPlayer (Int) : Représente l'id du joueur
            col (Int) : Représente la colonne de début
            ligne (Int) : Représente la ligne de début
            pasLigne (Int) : Représente le pas à effectuer en ligne
            pasCol (Int) : Représente le pas à effectuer en colonne
        Résultat :
            Retourne le couple représentant l'alignement ainsi que si la case suivante est vide
        """
        i = pasLigne
        j = pasCol
        count = 0
        while(i + ligne < 6 and i + ligne >= 0 and j + col < 7 and j + col >= 0 and self.__board[ligne + i][col + j] == idPlayer):
            i = i + pasLigne
            j = j + pasCol
            count = count + 1
        offsetLigne = ligne + i + pasLigne
        offsetCol = col + i + pasCol
        # test si case vide
        if(offsetLigne >= 0 and offsetLigne < 6 and offsetCol >= 0 and offsetCol < 7 and self.__board[offsetLigne][offsetCol] == 0):
            return (count, True)
        else:
            return (count, False)

    def detectWin(self, idPlayer, col, ligne):
        """
        Pré-requis :
            idPlayer (Int) : Représente l'id du joueur qui à nouvellement placé un pion
            col (Int) : Représente la colonne du nouveau pion
            ligne (Int) : Représente la ligne du nouveau pion
        Résultat :
            Retourne True si le nouveau pion placé termine la partie, False sinon.
        """

        countLigne = 1
        countCol = 1
        countDiag1 = 1
        countDiag2 = 1

        aliL1 = self.alignement(idPlayer, col, ligne, 0, 1)  # droite
        aliL2 = self.alignement(idPlayer, col, ligne, 0, -1)  # gauche

        aliC1 = self.alignement(idPlayer, col, ligne, 1, 0)  # bas
        aliC2 = self.alignement(idPlayer, col, ligne, -1, 0)  # haut

        aliD11 = self.alignement(idPlayer, col, ligne, 1, 1)  # bas droite
        aliD12 = self.alignement(
            idPlayer, col, ligne, -1, -1)  # haut gauche

        aliD21 = self.alignement(idPlayer, col, ligne, 1, -1)  # bas gauche
        aliD22 = self.alignement(idPlayer, col, ligne, -1, 1)  # haut droite

        countLigne = countLigne + aliL1[0] + aliL2[0]
        countCol = countCol + aliC1[0] + aliC2[0]
        countDiag1 = countDiag1 + aliD11[0] + aliD12[0]
        countDiag2 = countDiag2 + aliD21[0] + aliD22[0]

        if(aliL1[1] or aliL2[1]):
            if(idPlayer == 2):
                self.__evaluation = self.__evaluation + \
                    self.__returnEval(countLigne)
            else:
                self.__evaluation = self.__evaluation - \
                    self.__returnEval(countLigne)
        if(aliC1[1] or aliC2[1]):
            if(idPlayer == 2):
                self.__evaluation = self.__evaluation + \
                    self.__returnEval(countCol)
            else:
                self.__evaluation = self.__evaluation - \
                    self.__returnEval(countCol)
        if(aliD11[1] or aliD12[1]):
            if(idPlayer == 2):
                self.__evaluation = self.__evaluation + \
                    self.__returnEval(countDiag1)
            else:
                self.__evaluation = self.__evaluation - \
                    self.__returnEval(countDiag1)
        if(aliD21[1] or aliD22[1]):
            if(idPlayer == 2):
                self.__evaluation = self.__evaluation + \
                    self.__returnEval(countDiag2)
            else:
                self.__evaluation = self.__evaluation - \
                    self.__returnEval(countDiag2)

        if(countCol >= 4 or countLigne >= 4 or countDiag1 >= 4 or countDiag2 >= 4):
            self.__isOver = True
            return True
        else:
            return False
