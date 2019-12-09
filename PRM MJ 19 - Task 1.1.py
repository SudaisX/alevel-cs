
#Declare Data Array[1:NOS] : String
#Declare NOS : Integer
#Declare Name : String
#Declare Email : String

NOS = int(input("Enter number of Students: \n"))
Data = [0 for i in range(NOS)]  #Creates a list with NOS number of indexes

for x in range(NOS):
    Name = input("Enter a Name: \n")
    Email = input("Enter an Email: \n")
    Data[x] = f"{Name}#{Email}"

print("<Name>#<Email>")   #used as a heading
for n in Data:
    print(n)

