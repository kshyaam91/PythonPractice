import random


with open("SOWPODS.txt","r") as pick:
    text = pick.read()
    word1=[]
    while text:
        word1= text.split("\n")
        text=pick.read()

    word = word1[random.randint(1,len(word1))]
    print(word)

print("Welcome to Hangman!!!")
empty = list("_"*len(word))

def hangman(guess, word):
    if guess in word:
        indi = [x for x, y in enumerate(word) if y == guess]
        for e in indi:
            empty[e] = guess
        print(empty)
    else:
        print("Guess again!!!")
    return empty

count =6
guessList =[]
while count>0:
    guess = input("Guess your letter: ")
    guess = guess.upper()

    if guess in guessList:
        print("Letter already guessed!!!")

    guessList.append(guess)

    empty = hangman(guess,word)
    count -= 1
    print("You have ", count, "tries left")

    if empty == list(word):
        print("You have guessed the word!!!")
        break
    elif count==0:
        print("Game Over!!!")