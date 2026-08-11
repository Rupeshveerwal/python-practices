# Bubble_Sorting.py

size = int(input("Enter the size of the list: "))
a = []

for i in range(size):
    loc = int(input("Enter data "))
    a.append(loc)

print("List Created: ",a)

for i in range(size):
    for j in range(0,size-1-i):
        if a [j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
l = int(input("which largest to find: "))
print(f" {l} largest is {a[-l]}")

total = 0
for i in a:
    total += i 

print(f"sum of full list is {total}")

