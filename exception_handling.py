# a = int(input("Enter value: "))
# b = int(input("Enter value: "))

# try:
#     c = a/b

# except ZeroDivisionError:
#     print("Invalid input")

# finally:
#     print("Try again")



a = int(input("Enter value: "))
b = int(input("Enter value: "))

try:
    c = a+b

except ValueError:
    print("Invalid input")

finally:
    print("Try again")

