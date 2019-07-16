a = [5, 10, 15, 20, 25]

def firstLast(a):
    newList =[]
    newList.append(a[0])
    newList.append(a[len(a)-1])
    return newList

print(firstLast(a))