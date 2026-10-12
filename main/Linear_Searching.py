A = ["Rupesh","Ajay", "Manoj", "Mohit", "Vijay"]
f = 0
item = input("Enter Name to check: ")

for i in A:
    if item == i:
        f = 1
        break

if f==1:
    print("Found")
else:
    print("Not found")
