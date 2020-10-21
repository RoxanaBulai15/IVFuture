from math import *

print("_____________")
print("!!! Liste !!!")
print("_____________")
students = ["Maria", "Matei", "Roxana"]
note = [10, 9.9, 5]
print(students[0])
print(students[1:])
print(students[2:])
print(students[0:2])
students.insert(1, "Paul")
print(students)
students.remove("Roxana")
print(students)
students.pop()
print(students)
students.append("Alina")
students.append("Kevin")
students.sort()
print(students)
note.sort()
print(note)
note.reverse()
print(note)
students2 = students.copy()
print(students2)

coordonate = [(1, 2), (2.4, 3), (1.8, 2)]
print(coordonate[0])
print(coordonate[1][0])


def say_hi():
    print("Hello")


say_hi()

print("_________________")
print("!!! DICTIONAR !!!")
print("_________________")
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
for i in range(4):
    key = input("Introduceti materia: ")
    faculty[key] = input("Introduceti nota de la examen: ")
print("Noul dictionar creat este: ")
for materie, nota in faculty.items():
  print(materie, nota)


print("____________")
print("!!! TEMA !!!")
print("____________")


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
    # close a file
    file.close()


liste()


