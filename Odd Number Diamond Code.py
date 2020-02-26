#Diamond Code

integer = False
num = int(input("Enter an odd number for the diamond. \n"))
while not(integer):
    if num % 2 == 0:
        num = int(input("Wrong Input, Enter an odd number.  \n"))
    else:
        integer = True

maxspace = int(num/2)

for i in range(maxspace):
    stars = "*" * ((2*i) + 1)
    spaces = " " * (maxspace - i)
    print(f"{spaces}{stars}")

for j in range(maxspace + 1):
    stars = "*" * (((maxspace - j) * 2) + 1)
    spaces = " " * j
    print(f"{spaces}{stars}")





