class A:

    def Add(*args):
        total = 0
        for i in args:
            total += i
            print(total)

    def Add(*args):
        total = 0
        for i in args:
            total -= i
            print(total)

    def Add(*args):
        total = 0
        for i in args:
            total *= i
            print(total)



obj=A
obj.Add(13)
obj.Add(10,20)
obj.Add(10,20,30)

