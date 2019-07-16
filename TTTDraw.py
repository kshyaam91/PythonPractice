from  CheckTTT.checkTTT import won
import random
game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

def askPlayer1(x,y,game):
    game[x][y] = "X"
    print(game[0])
    print(game[1])
    print(game[2])
    print()


def askPlayer2(x,y,game):
    game[x][y] = "O"
    print(game[0])
    print(game[1])
    print(game[2])
    print()


for i in range (0,3):
    while won(game):
        askPlayer1(random.randint(0,2), random.randint(0,2), game)
        askPlayer2(random.randint(0,2), random.randint(0,2), game)

        won(game)
        #break
