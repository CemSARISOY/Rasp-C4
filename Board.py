
class Board:
    def __init__(self):
        self.__board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.__isOver = False
        self.__evaluation = 0

    def isValid(self, col):
        """
        Pré-requis : Un entier représentant une colonne du plateau
        Résultat : Retourne si true si un pion peut être placé dans la colonne, false sinon
        """
        return self.__board[0][col] == 0

    def placePawn(self, idPlayer, col):
        """
        Pré-requis : Un joueur et un entier représentant une colonne du plateau
        Résultat : Place le pion du joueur donné dans la colonne donnée
        """
        i = 5
        while(i >= 0 and self.__board[i][col] != 0):
            i = i-1

        self.__board[i][col] = idPlayer

        # Detecte si ya une victoire
        hasWon = self.detectWin(idPlayer, col, i)

        return hasWon

    # Test l'alignement possible dans la direction donné
    def alignement(self, idPlayer, col, ligne, pasLigne, pasCol):
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
                    self.returnEval(countLigne)
            else:
                self.__evaluation = self.__evaluation - \
                    self.returnEval(countLigne)
        if(aliC1[1] or aliC2[1]):
            if(idPlayer == 2):
                self.__evaluation = self.__evaluation + \
                    self.returnEval(countCol)
            else:
                self.__evaluation = self.__evaluation - \
                    self.returnEval(countCol)
        if(aliD11[1] or aliD12[1]):
            if(idPlayer == 2):
                self.__evaluation = self.__evaluation + \
                    self.returnEval(countDiag1)
            else:
                self.__evaluation = self.__evaluation - \
                    self.returnEval(countDiag1)
        if(aliD21[1] or aliD22[1]):
            if(idPlayer == 2):
                self.__evaluation = self.__evaluation + \
                    self.returnEval(countDiag2)
            else:
                self.__evaluation = self.__evaluation - \
                    self.returnEval(countDiag2)

        if(countCol >= 4 or countLigne >= 4 or countDiag1 >= 4 or countDiag2 >= 4):
            self.__isOver = True
            return True
        else:
            return False

    def getEvaluation(self):
        return self.__evaluation
    """
    def detectWin(self):
        Résultat : Verifie si il y a un gagnant
        Retourne 0 si il n'y a pas de gagnant, 1 si le joueur 1 a gagné, 2 si le joueur 2 a gagné
        gagnant = 0
        gagne = False
        i = 5
        while(i >= 0 and not gagne):
            j = 0
            while (j < 7 and not gagne):
                if(self.__board[i][j] != 0):
                    m = 1
                    count = 0
                    # en ligne
                    while(j < 4 and m < 4 and not gagne):
                        if(self.__board[i][j] == self.__board[i][j+m]):
                            count = count + 1
                        m = m + 1
                    if(count == 3):
                        gagne = True
                        gagnant = self.__board[i][j]
                    # en colonne
                    m = 1
                    count = 0
                    while(i > 2 and m < 4 and not gagne):
                        if(self.__board[i][j] == self.__board[i-m][j]):
                            count = count + 1
                        m = m + 1
                    if(count == 3):
                        gagne = True
                        gagnant = self.__board[i][j]
                    # en diagonale
                    m = 1
                    count = 0
                    while(j < 4 and i > 2 and m < 4 and not gagne):
                        if(self.__board[i][j] == self.__board[i-m][j+m]):
                            count = count + 1
                        m = m + 1
                    if(count == 3):
                        gagne = True
                        gagnant = self.__board[i][j]
                    # en diagonale inverse
                    m = 1
                    count = 0
                    while(i > 2 and j > 2 and m < 4 and not gagne):
                        if(self.__board[i][j] == self.__board[i-m][j-m]):
                            count = count + 1
                        m = m + 1
                    if(count == 3):
                        gagne = True
                        gagnant = self.__board[i][j]
                j = j + 1
            i = i - 1
        return gagnant
    # Evalue le plateau"""

    def isOver(self):
        """
        Résultat : Retourne True si la partie est finie, False sinon
        """
        return self.__isOver

    """
    def evaluate(self, idJoueur):
       
        Pré-requis: L'entier assigné au joueur
        Résultat: Donne un score au plateau de jeu en fonction du joueur donné en argument.
        Le score est calculé par le nombre de pions alignés et si l'alignement peut être continué
       
        somme = 0

        # Evaluation des colonnes
        for j in range(7):
            i = 5
            while (i >= 0):
                count = 1
                if(self.__board[i][j] != 0):
                    while(i-count >= 0 and count < 4 and self.__board[i-count][j] == self.__board[i][j]):
                        count = count + 1
                    if(self.__board[i][j] == idJoueur):
                        if(count == 4 or (i-count >= 0 and self.__board[i-count][j] == 0)):
                            somme = somme + self.returnEval(count)
                    else:
                        if(count == 4 or (i-count >= 0 and self.__board[i-count][j] == 0)):
                            somme = somme - self.returnEval(count)
                i = i - count

        # Evaluation des lignes
        for i in range(5, -1, -1):
            j = 0
            while(j < 7):
                count = 1
                if(self.__board[i][j] != 0):
                    while(j+count < 7 and count < 4 and self.__board[i][j+count] == self.__board[i][j]):
                        count = count + 1
                    if(self.__board[i][j] == idJoueur):
                        if(count == 4 or (j-1 >= 0 and self.__board[i][j-1] == 0 and (i == 5 or self.__board[i+1][j-1] != 0)) or (j+count < 7 and self.__board[i][j+count] == 0 and (i == 5 or self.__board[i+1][j+count] != 0))):
                            somme = somme + self.returnEval(count)
                    else:
                        if(count == 4 or (j-1 >= 0 and self.__board[i][j-1] == 0 and (i == 5 or self.__board[i+1][j-1] != 0)) or (j+count < 7 and self.__board[i][j+count] == 0 and (i == 5 or self.__board[i+1][j+count] != 0))):
                            somme = somme - self.returnEval(count)
                j = j + count

        # Evaluation de la diagonale haut droite
        for i in range(5, -1, -1):
            for j in range(7):
                count = 1
                if(self.__board[i][j] != 0):
                    while(j+count < 7 and i-count >= 0 and count < 4 and self.__board[i-count][j+count] == self.__board[i][j]):
                        count = count + 1
                    if(self.__board[i][j] == idJoueur):
                        if(count == 4 or (j-1 >= 0 and i+1 < 6 and self.__board[i+1][j-1] == 0 and (i == 4 or self.__board[i+2][j-1] != 0)) or (j+count < 7 and i-count >= 0 and self.__board[i-count][j+count] == 0 and (self.__board[i-count+1][j+count] != 0))):
                            somme = somme + self.returnEval(count)
                    else:
                        if(count == 4 or (j-1 >= 0 and i+1 < 6 and self.__board[i+1][j-1] == 0 and (i == 4 or self.__board[i+2][j-1] != 0)) or (j+count < 7 and i-count >= 0 and self.__board[i-count][j+count] == 0 and (self.__board[i-count+1][j+count] != 0))):
                            somme = somme - self.returnEval(count)

        # Evaluation de la diagonale haut gauche
        for i in range(5, -1, -1):
            for j in range(6, -1, -1):
                count = 1
                if(self.__board[i][j] != 0):
                    while(j-count >= 0 and i-count >= 0 and count < 4 and self.__board[i-count][j-count] == self.__board[i][j]):
                        count = count + 1
                    if(self.__board[i][j] == idJoueur):
                        if(count == 4 or (j+1 < 7 and i+1 < 6 and self.__board[i+1][j+1] == 0 and (i == 4 or self.__board[i+2][j+1] != 0)) or (j-count >= 0 and i-count >= 0 and self.__board[i-count][j-count] == 0 and (self.__board[i-count+1][j-count] != 0))):
                            somme = somme + self.returnEval(count)
                    else:
                        if(count == 4 or (j+1 < 7 and i+1 < 6 and self.__board[i+1][j+1] == 0 and (i == 4 or self.__board[i+2][j+1] != 0)) or (j-count >= 0 and i-count >= 0 and self.__board[i-count][j-count] == 0 and (self.__board[i-count+1][j-count] != 0))):
                            somme = somme - self.returnEval(count)

        return somme
    """

    def returnEval(self, count):
        """
        Pré-requis : la taille de l'alignement
        Résultat : Retourne l'evaluation assigné a la taille de l'alignement
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
