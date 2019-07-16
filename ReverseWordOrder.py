
def reverseWord(testString):
    testString = testString.split()

    testString = testString[::-1]
    testString = " ".join(testString)

    print(testString)


reverseWord("My name is Shyaam")