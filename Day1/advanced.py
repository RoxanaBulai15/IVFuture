workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet()
workbook.save()


def dictionary():
    file = open("advanced.txt", "r")
    # am extras textul din file
    text = file.read()
    # am facut o lista cu liniile din fisier
    lines = text.split("\n")
    # print(lines)
    # am facut o lista de liste(o lista care contine alte liste cu cheia+valoarea)
    list = []
    for index in range(len(lines)):
        list.append(lines[index].split(":"))
    # print(list)
    # parcurg lista mare si formez o noua lista doar cu liste ce contin 2 elemente: cheie+valoare
    newlist = []
    for index in range(len(list)):
        if len(list[index]) >= 2:
            newlist.append(list[index])
    # print(newlist)

    dictionar = {}
    for i in range(len(newlist)):
        key = newlist[i][0]
        value = newlist[i][1]
        if len(newlist[i]) > 1:
            for j in range(2, len(newlist[i])):
                value = value + ":" + newlist[i][j]
        dictionar[key] = value
    print("Dictionarul format are urmatoarele key cu valori: ")
    for key, value in dictionar.items():
        print("Key: " + key + "," + "Value: " + value)


dictionary()

#file1 = open('advanced.txt', 'r')
#lines = file1.readlines()

#dictionary = {}
#for i in lines:
    #split = i.split(":", 1)
    #if len(split) > 1:
        #dictionary[split[0]] = split[1].replace("\n", "")
    #else:
        #print("The ", split, " was excluded")

#count = 0
#for key, value in dictionary.items():
    #count += 1
    #print(count, "  Key: " + key + "," + "Value: " + value)
