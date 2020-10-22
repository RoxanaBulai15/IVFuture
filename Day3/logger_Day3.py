import xlwt
from xlwt import Workbook
import logging

logging.basicConfig(filename="log.txt",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)



wb = xlwt.Workbook()

sheet1 = wb.add_sheet("advanced")
font0 = xlwt.Font()
font0.name = "Times New Roman"
font0.colour_index = 2
font0.bold = True

style1 = xlwt.XFStyle()
style1.font = font0

style1 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')

first_col = sheet1.col(0)
first_col.width = 256 * 20  # 20 characters wide (-ish)


second_col = sheet1.col(1)
second_col.width = 256 * 70

sheet1.write(0, 0, "KEY", style1)
sheet1.write(0, 1, "VALUE", style1)

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
            logging.info("Lista are 2 sau mai multe elemente.")
        else:
            logging.warning("Aceasta lista are un singur element! - ")
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
    row = 1

    for key, value in dictionar.items():
        logging.info("Key: "+ str(key) + " , " + "Value: " + str(value) )
        column = 0
        sheet1.write(row,column, key)
        column = column + 1
        sheet1.write(row, column, value)
        row = row +1

    wb.save("advanced.xlsx")


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
