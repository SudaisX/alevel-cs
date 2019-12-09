
row = int(input("Enter how many students you'd like to add: ")) * 4
col = 2

students = [[0 for j in range(col)] for i in range(row)]

for heading in range(0, row, 4):
    students[heading][0] = "Student Name: "
    students[heading + 1][0] = "Email Address: "
    students[heading + 2][0] = "Date of Birth: "
    students[heading + 3][0] = "Student ID: "

count = 0
for each in range(0, row, 4):
    count += 1
    count2 = int(row/4)
    count3 = f"({count}/{count2})"
    students[each][1] = input(f"Enter Student's Name {count3} : ")
    students[each + 1][1] = input(f"Enter Student's Email Address {count3} : ")
    students[each + 2][1] = input(f"Enter Student's Date of Birth {count3} : ")
    students[each + 3][1] = input(f"Enter Student's ID {count3} : ")

for student in students:
    print(student)


def search(srch):
    Found = False
    for name in range(0, row, 4):
        if srch == students[name][1]:
            print(f"Student Name: {students[name][1]}")
            print(f"Student's Email Address: {students[name + 1][1]}")
            print(f"Student Date of Birth: {students[name + 2][1]}")
            print(f"Student's ID: {students[name + 3][1]}")
            Found = True
        else:
            pass
    if Found == False:
        print("Student not found.")

search(input("Enter a name to search: "))



