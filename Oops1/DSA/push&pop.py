l = []
while True:
    print("1 . Push")
    print("2 . Pop")
    print("3 . Display")

    choice = int(input("Enter your Choice"))

    if choice==1:
        size = int(input("enter your size"))

        for i in range(size):
            element = input("Enter your element")
            l.append(element)


    elif choice == 2:
        l.pop()
        print("\nItem Removed\n")

    elif choice == 3:
        print(l)
        for i in l:
            print(i)
    else:
        print("Wrong choice, try again")        
        break

