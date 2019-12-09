

with open("students.txt", "a") as students:
    NOS = int(input("Enter number of students you'd like to add: "))  # Number of Students
    for x in range(NOS):  #iterates for how many students there are
        ID = input("Enter student ID: ")
        ID_True = False
        while not (ID_True):  #Validates ID
            if ID[0:2].isalpha() and ID[0:2].isupper() and ID[2:6].isdigit() and len(ID) == 6:
                ID_True = True
            else:
                ID = input("Incorrect ID, Re-Enter: ")

        EMAIL = input("Enter student e-mail: ")
        EMAIL_True = False
        while not (EMAIL_True):  #Validates E-mail
            if "@" and "." in EMAIL:
                EMAIL_True = True
            else:
                EMAIL = input("Incorrect e-mail, Re-Enter: ")

        STRING = f"{ID}#{EMAIL}"
        students.write(STRING + "\n")
    print("Students added. ")