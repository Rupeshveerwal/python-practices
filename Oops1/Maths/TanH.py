x = float(input("Enter Value: "))

e = 2.718
v = float(e**x)
b = float(e**(-x))
# top =  e**x - e**-x
# ---------------------
# bottom = e**x + e**-x
top = v-b
bottom = v+b

answer = top/bottom

print("e^x: ",v)   
print("e^-x: ",b)

print("top",top)
print("bottom",bottom)
print(answer)
