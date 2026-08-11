# Using Lambda Function to create Calculator
 
n = lambda x,y : (x+y , x-y , x*y , x/y)

x = int(input("Enter x : "))
y = int(input("Enter y : "))

print(n(x,y))