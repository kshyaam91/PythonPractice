birthDict = {"Shyaam":"08/20/1991", "Dad":"07/09/1959", "Mom":"14/03/1963", "Shravan":"11/01/1997"}

print("We know the birthdays of :")
name = [ele for ele in birthDict.keys()]
print(name)

birthday = input("Please enter whose birthday you want to know?")

if birthday in name:
    print(birthDict.get(birthday))
