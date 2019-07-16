number = int(input("Enter the number : "))

if number%2==0:
    print("The given number is an even number")
    if number%4==0:
        print("The given number is divisible by 4")
else:
    print("The given number is an odd number")