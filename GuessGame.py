import  random

randNum = random.randint(1,10)
print(randNum)

usrInput = input("Guess the number: ")

while usrInput!= "exit":
    guessNumber = int(usrInput)
    if(randNum<guessNumber):
        print("Too High!!!")
        usrInput = input("Guess the number: ")
    elif(randNum>guessNumber):
        print("Too Low!!!")
        usrInput = input("Guess the number: ")
    else:
        print("Correct!!!")
        randNum = random.randint(1, 10)
