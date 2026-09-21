B = [1,2,6,3,2,7,8,9,4,5,0,66,77,88,99,33,44,55,22,11]
B = sorted(B)
print(B)
A= [1,2,3,4,5,6,7,8,9,10]
F = 0
L = len(B)-1
item = int(input("Enter Element: "))
while F <= L:
    mid = (F+L)//2
    print(mid)
    
    if item == B[mid]:
        F = 1
        print("Found")
        break
        
    elif item > B[mid]:
        F = mid + 1
        print("Not found")

    else:
        L = mid -1 
        print("Not found")


# if F==1:
#     print("Item Found")
# else:
#     print("Item not Found")

