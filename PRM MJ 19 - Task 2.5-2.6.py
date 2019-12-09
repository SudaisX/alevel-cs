with open("students2.txt", "w") as students:       #opens the file to write, and stores it in students, automatically closes the file too once out of indent.
    NOS = int(input("Enter number of students you'd like to add: "))   #Declare NOS : Integer
    for stds in range(NOS):

        ID = input(f"Enter Student ID ({stds + 1}/{NOS}) : ")          #Declare ID : String
        ID_True = False                                                #Declare ID_True : Boolean
        while not(ID_True):
            if len(ID) == 6 and ID[0:2].isupper() and ID[0:2].isalpha and ID[2:6].isnumeric():
                ID_True = True
            else:
                ID = input("Invalid ID, Re-enter: ")
        students.write(ID + "\n")

        EMAIL = input(f"Enter Student's Email Address ({stds + 1}/{NOS}) : ")       #Declare EMAIL : String
        EMAIL_True = False                                                          #Declare EMAIL_True : Boolean
        while not(EMAIL_True):
            if "@" and "." in EMAIL:
                EMAIL_True = True
            else:
                EMAIL = input("Invalid Email, Re-enter: ")
        students.write(EMAIL + "\n")

        ADDRESS = input(f"Enter Student's Home Address ({stds + 1}/{NOS}) : ")      #Declare ADDRESS : String
        students.write(ADDRESS + "\n")

        TUTOR = input(f"Enter Student's Tutor ({stds + 1}/{NOS}) : ")               #Declare Tutor : String
        students.write(TUTOR + "\n")

    print(f"{NOS} Student(s) added. ")



