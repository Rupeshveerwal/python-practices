#Largest no between 3 no.

# def large_no(a,b,c):
#     if a > b and a > c:
#         print(a," is largest.")
#     elif b > a and b > c:
#         print(b," is largest.")
#     else:
#         print(c," is largest")

# a = int(input("type 1st : "))
# b = int(input("type 2nd : "))
# c = int(input("type 3rd : "))
# large_no(a,b,c)

# Marksheet 

# def Marksheet(Marks):
#     if Marks >= 60:
#         print("Grade A")
#     elif Marks >= 45 and Marks < 60:
#         print("Grade B")
#     elif Marks >= 35 and Marks < 45:
#         print("Grade C")
#     else:
#         print("Grade D")

# marks = int(input("enter marks: "))
# Marksheet(marks)


# Even or Odd

# def Check(n):
#     if n%2 == 0:
#         print("your no. is Even")
#     else:
#         print("Your no. is Odd")

# n = int(input("enter no. : "))
# Check(n)


# Check  char or numbers

def char(c):
    if c >='0' and c<='9':
        print("it is no.")
    elif c>='a' and c<='z' or c>='A' and c<='Z' :
        print("it is char")
    else:
        print("it is symbol")

c = input("enter 1 char")
char(c)



    
        