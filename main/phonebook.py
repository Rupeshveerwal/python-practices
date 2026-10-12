d = {}

# data = ()

for i in range(2):
    name = input("Enter name : ")
    number = int(input("Enter no. : "))

    phonebook = {name : number}
    d.update(phonebook)

print(d)

find = input("Enter name or number to find : ")

if find in phonebook:
    print('found')

else:
    print("Not found")
    print(phonebook[find])






