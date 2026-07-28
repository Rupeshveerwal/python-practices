Amount = int(input("Enter amount: "))

Note1 = int(input("How many notes of 500: "))
Note2 = int(input("How many notes of 200: "))
Note3 = int(input("How many notes of 100: "))

x = Note1 * 500
y = Note2 * 200
z = Note3 * 100

Sum = x+y+z
if Sum == Amount:
    print("your amount is deposited.")

else:
    print("Not deposited, Retry.")