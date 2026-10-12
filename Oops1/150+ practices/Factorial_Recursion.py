# Factorial_Recursion.py
n = int(input("enter no: "))
def factorial (n):
    return 1 if n <= 1 else n * factorial (n-1)
print(factorial(n)) 