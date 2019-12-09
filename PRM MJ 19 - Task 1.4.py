
NOS = int(input("Enter number of Students: \n"))
Data = [0 for i in range(NOS)]

for x in range(NOS):
    Name = input("Enter a Name: \n")
    Email = input("Enter an Email: \n")
    Data[x] = f"{Name}#{Email}"

print("<Name>#<Email>")
for n in Data:
    if n != "" and n != "#":  #Checks if an element is empty or not
        print(n)

def search(srch):
    for element in Data:
        if element != "":
            hash = int(element.index("#"))
            name = element[0:hash]
            email = element[hash + 1 : len(element) + 1]
            if srch in name:
                print(f"Name: {name}")
                print(f"E-mail: {email}")

search(input("\nEnter part, or the whole, of a name to SEARCH:  \n"))

