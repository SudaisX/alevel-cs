


with open("students.txt", "r") as students:

    def search(srch):
        EOF = False
        Found = False
        while not (EOF) and not(Found):
            line = students.readline()
            if line != "":
                id = line[0:6]
                email = line[7:len(line)]
                if srch in id:
                    print(f"ID {id}'s e-mail address is {email}")
                    Found = True
            else:
                print("Student ID not found. ")
                EOF = True


    search(input("Enter ID: "))