string = input("Enter your string: ")
revString = string[::-1]

if revString==string:
    print("The given String is a palindrome")
else:
    print("The given string is not a palindrome")