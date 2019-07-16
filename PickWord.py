import random
with open("SOWPODS.txt","r") as pick:
    text = pick.read()
    word=[]
    while text:
        word = text.split("\n")
        text=pick.read()

    pickRand = word[random.randint(1,len(word))]
    print(pickRand)