def won(game):
    i=0
    j=0
    if game[i+1][j+1] == game[i][j+1] == game[i+2][j+1]:
        return check(game[i+1][j+1])

    elif game[i][j] == game[i+1][j+1] == game[i+2][j+2]:
        return check(game[i + 1][j + 1])

    elif game[i+1][j+1] ==game[i][j+2] == game[i+2][j]:
        return check(game[i + 1][j + 1])

    elif game[i+1][j+1] == game[i+1][j] ==game[i+1][j+2]:
        return check(game[i + 1][j + 1])

    else:
        return True

def check(num):
    if num ==2:
        print("Player 2 wins!!!")
        return False
    elif num==1:
        print("Player 1 wins!!!")
        return False
    else:
        return True


#game = [[0, 1, 0],[2, 1, 0],[2, 1, 1]]
#won(game)