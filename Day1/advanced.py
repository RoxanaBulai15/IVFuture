def dictionary():
    file = open("advanced.txt", "r")
    #am extras textul din file
    text = file.read()
    #am facut o lista cu liniile din fisier
    lines = text.split("\n")
    #print(lines)
    #am facut o lista de liste(o lista care contine alte liste cu cheia+valoarea)
    list = []
    for index in range(len(lines)):
        list.append(lines[index].split(":"))
    #print(list)
    #parcurg lista mare si formez o noua lista doar cu liste ce contin 2 elemente: cheie+valoare
    newlist = []
    for index in range(len(list)):
        if len(list[index]) >= 2:
            newlist.append(list[index])
    #print(newlist)

    dictionar = {}
    for i in range(len(newlist)):
        key = newlist[i][0]
        value = newlist[i][1]
        if len(newlist[i]) > 1:
            for j in range(2, len(newlist[i])):
                value = value + ":" +  newlist[i][j]
        dictionar[key] = value
    print("Dictionarul format are urmatoarele key cu valori: ")
    for key, value in dictionar.items():
        print("Key: " + key + "," + "Value: " + value)



dictionary()