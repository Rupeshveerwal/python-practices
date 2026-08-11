# Largest of Two Numbers
# Take two numbers and print the larger number.

a = int(input("enter 1st no."))
b = int(input("enter 2nd no."))
c = int(input("enter 2nd no."))

if a > b and a > c:
    print(f"{a} is greater")
elif b > a and b > c :
    print(f"{b} is greater")
else :
    print(f"{c} is greater")
