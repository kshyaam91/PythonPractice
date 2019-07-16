
counter_dict = {}

with open("readFile.txt","r") as read_file:
    line = read_file.read()
    while line:
        list = line.split("\n")
        for ele in list:
            if ele in counter_dict:
                counter_dict[ele] +=1
            else:
                counter_dict[ele] = 1
        line=read_file.read()

print(counter_dict)