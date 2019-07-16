def gameBoard(number):
    for k in range(0, number):
        print("\t---\t" * number)

        print("|\t\t"* (number+1))
    print("\t---\t"* (number))

gameBoard(5)