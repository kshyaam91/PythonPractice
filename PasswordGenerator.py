import random


passLength = int(input("Enter the size of the password:"))
upperCaseLetters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowerCaseLetters = upperCaseLetters.lower()
symbols = "`~!@#$%^&*()_-+<>?,.\/"
numbers = "0123456789"
passwordChar = upperCaseLetters+lowerCaseLetters+symbols+numbers

password =""

for i in range(0, passLength):
    password = password + random.choice(passwordChar)

print(password)
