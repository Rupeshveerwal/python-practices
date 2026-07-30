#factorial of number using arbitary args
def fact(*num):
    for a in num:
         x = 1
    for i in range(1,a+1):
            x = x * i
    print(x)
fact(5)



