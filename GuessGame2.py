import random
mind = 88
count=0
guess = 50
while True:

    print(guess)
    if guess>mind:
        print("High!!!")
        guess-=1
        count+=1
    elif guess<mind:
        print("Low!!!")
        guess += 1
        count += 1
    elif guess==mind:
        print("Correct!!!")
        print("It took ",  count, "tries to guess!!!")
        break