
class Board:
    def __init__(self):
        self.__board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

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
        i = 0
        while(i < 5 and self.__board[i+1][col] == 0):
            i = i+1
        self.__board[i][col] = idPlayer

    # Detecte si un joueur a gagné

    def detectWin(self):
        """
        Résultat : Verifie si il y a un gagnant
        Retourne 0 si il n'y a pas de gagnant, 1 si le joueur 1 a gagné, 2 si le joueur 2 a gagné
        """
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
    # Evalue le plateau

    def isOver(self):
        """
        Résultat : Retourne True si la partie est finie, False sinon
        """
        if(self.detectWin() != 0):
            return True
        elif(self.__board[0][0] != 0 and self.__board[0][1] != 0 and self.__board[0][2] != 0 and self.__board[0][3] != 0 and self.__board[0][4] != 0 and self.__board[0][5] != 0 and self.__board[0][6] != 0):
            return True
        else:
            return False

    def evaluation(self, idJoueur):
        """
        Pré-requis : L'entier assigné au joueur
        Résultat : Donne un score au plateau de jeu en fonction du joueur donné en argument.
        Le score est calculé par le nombre de pions alignés et si l'alignement peut être continué
        """
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
