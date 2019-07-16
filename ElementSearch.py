def BinarySearch(list,number):
    start =0
    end = len(list)-1
    middle = int((end-start)/2)

    mid = list[middle]

    if mid>number:
        start=0
        end = middle
        print("Greater")
        print(start)
        print(end)
    elif mid<number:
        start=middle+1
        print("Lesser")
        print(start)
        print(end)

a = [1,2,3,4,5,6,7,8,9]
BinarySearch(a,13)