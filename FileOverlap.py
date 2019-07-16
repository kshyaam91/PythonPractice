with open("Happy.txt","r") as happy:
    text = happy.read()
    while text:
        happyList = text.split()
        text=happy.read()


with open("Prime.txt","r") as prime:
    text = prime.read()
    while text:
        primeList = text.split()
        text=prime.read()


for e in happyList:
    if e in primeList:
        print(e)



def marks_check(marks):
    if(marks>75):
        print('Excellent')
    elif(marks>50):
        print('Pass')
    else:
        print('Fail')