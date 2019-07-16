counter_dict={}

with open("sun.txt", "r") as file:
    altText = file.read()
    while altText:
        altText = altText[3:-26]
        list = altText.split("/")
        for ele in list:
            if ele in counter_dict:
                counter_dict[ele] += 1
            else:
                counter_dict[ele] = 1
        altText = file.read()

    print(counter_dict)