# Fibbonacci_series.py

n = 100
a, b = 0 ,1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b