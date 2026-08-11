e = 2.718
x = float(input("Enter value of x : "))
p = -x
exp = e**-x

cal = 1 / (1+exp)

print(cal)

if cal < 0.5:
    print("\nFalse")
elif cal > 0.5:
    print("\nTrue")
else:
    Print("Confusion")

