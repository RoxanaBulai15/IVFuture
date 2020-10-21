import os
from math import *

print(20*"_")
print("!!! Liste !!!")
print(20*"_")
students = ["Maria", "Matei", "Roxana"]
note = [10, 9.9, 5]
print("Primul student este: "+ students[0])
print(students[1:])
print(students[2:])

print("A fost adaugat un student in lista: ")
students.insert(1, "Paul")
print(students)
print("A fost sters un student din lista: ")
students.remove("Roxana")
print(students)
print("A fost sters ultimul student din lista: ")
students.pop()
print(students)
print("Sunt adaugati doi studenti si este sortata lista: ")
students.append("Alina")
students.append("Kevin")
students.sort()
print(students)
print("Lista cu note este sortata crescator: ")
note.sort()
print(note)
print("Lista cu note este sortata descrescator: ")
note.reverse()
print(note)
students2 = students.copy()
print("Studentii au fost copiati intr-o lista noua: ")
print(students2)

coordonate = [(1, 2), (2.4, 3), (1.8, 2)]
print(coordonate[0])
print(coordonate[1][0])


def say_hi():
    print("Hello")


say_hi()

print(20*"_")
print("!!! DICTIONAR !!!")
print(20*"_")
exams = {"Paul": 10, "Alina": 7, "Roxana": 9, "Geralt": 10}
x = exams["Paul"]
print("Nota studentului este: "+ str(x))
y = exams.get("Paul")
print("Nota studentului este: " + str(y))
exams["Alina"] = 6
z = exams["Alina"]
print("Nota studentului este: " + str(z))
print("Cheile din dictionar: ")
for student in exams:
    print(student)
print("Valorile cheilor din dictionar: ")
for student in exams:
    print(exams[student])
print("Toate perechile cheie-valoare din dictionar: ")
for student, note in exams.items():
  print(student, note)
ok = 0
if "Kevin" in exams:
    ok = 1
if ok == 0:
  print("No, 'Kevin' isn't a key in exams dictionary. ")
print("Este adaugat un student: ")
exams["Andreea"] = 9
for student, note in exams.items():
  print(student, note)
print("Este sters un student: ")
exams.pop("Alina")
for student, note in exams.items():
  print(student, note)
print("Lungimea dictionarului este: " + str(len(exams)))
# sterge dictionarul
del(exams)
faculty = {}
#for i in range(4):
  #  key = input("Introduceti materia: ")
  #  faculty[key] = input("Introduceti nota de la examen: ")
#print("Noul dictionar creat este: ")
#for materie, nota in faculty.items():
 # print(materie, nota)


print(20*"_")
print("!!! TEMA !!!")
print(20*"_")


def liste():
    link = "https://chromedriver.chromium.org/downloads"
    newlist = link.split(".")
    print(newlist)
    for i in range(len(newlist)):
        if newlist[i].find("org", 0, len(newlist[i])) != -1:
            print("Item-ul cautat este: " + newlist[i])
    # create and open a file
    file = open("link.txt", "w+")

    file.write(link)
    file = open("link.txt", "r")
    number_of_lines = len(open('link.txt').readlines())
    print(number_of_lines)
    a = file.read()
    print(type(a))
    nr_cuvinte = 0
    nr_litere = 0
    for i in range(len(a)):
        if a[i] ==" ":
            nr_cuvinte = nr_cuvinte + 1
        elif a[i].isalpha() == True:
            nr_litere = nr_litere +1
    print("Numarul cuvintelor este: " + str(nr_cuvinte+1))
    print("Numarul literelor este: " + str(nr_litere))
    file.close()

    # open file for reading
    f = open('link.txt')
    # move file cursor to end
    f.seek(0, os.SEEK_END)
    # get the current cursor position
    print('Size of file is', f.tell(), 'bytes')


liste()


