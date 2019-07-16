import random

generatedInt = random.randint(1000,9999)
stringInt = str(generatedInt)

print(generatedInt)
done = True

def cowsAndBulls(stringInt):
    inputNumber = input("Enter your number: ")

    cowCount = 0
    bullCount = 0

    for ele in stringInt:
        if ele in inputNumber:
            if (stringInt.index(ele) == inputNumber.index(ele)):
                cowCount = cowCount + 1
            else:
                bullCount = bullCount + 1
    print(str(cowCount), "Cows!!!", str(bullCount), "Bulls!!!")

    if cowCount==4:
        done = False
    else:
        done = True

    return done

while(done):
    done = cowsAndBulls(stringInt)