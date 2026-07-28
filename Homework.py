# Enter data, View, Select, Remove, legth of List 
A = []
count = 1
while count <=10:
    
    print("Enter 1 to Enter Data")
    print("Enter 2 to View and Remove Data")
    print("Enter 3 to Data Length")
    Choice = int(input("Enter your Choice: "))


    if Choice == 1:
        size = int(input("Enter Size: "))
        for i in range(size):
            value = input("Enter value: ")
            A.append(value)
            # print("You Entered ",A[i])
        print("\nYou filled the data\n",)
        

    elif Choice == 2:
        j=1
        while(j<=3):
            print("\nShowing Existing data")
            print(A)
            for index in A:
                print()
            print("\nSelect 1 to remove data using Location" )
            print("Select 2 to remove data using Value" )
            selected = int(input("Enter your Selection: "))
            if selected==1:
                locate=int(input("enter Location to remove: "))
                A.pop(locate)  
                print(locate," is removed.\n")                               #removes the selected location value
            elif selected==2:
                data = input("Enter data value to remove: ")
                A.remove(data)                                          #removes the selected data value
                print(data," is removed.\n")
            else :
                print("\nTry again\n")
                break
            j+=1
        


    elif Choice == 3 :
        print("Finding length")
        length = len(A)
        print("\nTotal length : ",length)

    else :
        print("\nWrong Choice!!!")
    
    count += 1
print("\nTry again")


            

