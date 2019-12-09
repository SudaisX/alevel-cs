

with open("students.txt", "r") as students:
    def search(srch):
        Found = 0
        EOF = False
        while not(EOF):
            line = students.readline()
            if line != "":
                AB = line[0:2]
                if AB == "AB":
                    Found += 1
                    print(line)
            elif line == "":
                EOF = True
                if Found == 0:
                    print("No Student ID starting with AB found: ")

        if Found != 0:
            print(f"{Found} Student ID(s) starting with AB found.")

    search(students)