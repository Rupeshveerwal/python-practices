import json
try: 
    with open('data.json', 'r') as f:
        data = json.load(f)
        print(data)
except :
    data = {}

while True:
    print("1. Open bank account")
    print("2. Close bank account")
    print("3. Bank account details")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        data[name] = age
    elif choice == 2:
        name = input("Enter your name: ")
        if name in data:
            del data[name]
        else:
            print("Name not found")
    elif choice == 3:
        name = input("Enter your name: ")
        if name in data:
            print(f"Name: {name}, Age: {data[name]}")
        else:
            print("Name not found")
    elif choice == 4:
        break
    else:
        print("Invalid choice")

with open('data.json', 'w') as f:
    json.dump(data, f)