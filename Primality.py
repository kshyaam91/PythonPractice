number = int(input("Enter a number to test for primality: "))

def findPrime():
    count = 0
    for ele in range(1,number):
        if number%ele==0:
            count +=1

    if count>2:
        print("The number is not a prime number")
    else:
        print("The number is a prime number")


findPrime()