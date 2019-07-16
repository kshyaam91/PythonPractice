

def fibonnaci(number):
    add=0
    while(number>=0):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return fibonnaci(number-2)+fibonnaci(number-1)


print(fibonnaci(9))