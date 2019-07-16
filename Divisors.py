inputNum = int(input("Enter a number"))
divisors=[]

for element in range(2,inputNum):
    if inputNum% element==0:
        divisors.append(element)


print(divisors)