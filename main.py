from Player import Player
from IAMinMax import IAMinMax
from Game import Game

p1 = Player(1)
p2 = Player(2)
p3 = IAMinMax(2, 4)

game = Game(p1, p3)
game.run()
