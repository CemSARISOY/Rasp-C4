from Player import *
from IAMinMax import *
from Game import *

# game = Game()  # Partie réelle contre IA
game = Game(commandLine=True)  # Partie terminal contre IA
# game = Game(commandLine=True, playerOnly=True) # Partie terminal contre Joueur
game.run()
