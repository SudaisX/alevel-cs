
row = 4
col = 3
Data = [[0 for j in range(col)] for i in range(row)]

Data[0][0] = "Student Name: "
Data[1][0] = "Email Address: "
Data[2][0] = "Date of Birth: "
Data[3][0] = "Student ID: "

for x in range(col):
    if x == 0:
        pass
    else:
        Data[0][x] = input("Enter Student Name: ")
        Data[1][x] = input("Enter Email Address: ")
        Data[2][x] = input("Enter Date of Birth: ")
        Data[3][x] = input("Enter Student ID: ")

for x in Data:
    print(x)