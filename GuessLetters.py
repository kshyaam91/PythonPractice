print("Welcome to Hangman!!!")
empty = list("_"*9)
print(empty)

word = "EVAPORATE"

def hangman(guess, word):
    if guess in word:
        indi = [x for x, y in enumerate(word) if y == guess]
        for e in indi:
            empty[e] = guess
        print(empty)
    else:
        print("Guess again!!!")
    return empty


while True:
    guess = input("Guess your letter: ")
    guess = guess.upper()

    empty = hangman(guess,word)

    if empty == list(word):
        print("You have guessed the word!!!")
        break