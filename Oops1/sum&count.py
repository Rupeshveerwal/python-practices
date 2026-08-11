# enter digit in parent classand then count digit in child 1 class and sum of digits in child 2 class
 
class A:
    def value(self):
        self.a=int(input("enter: "))
    
class B1(A):
    def c(self):
        self.d = 0
        while self.a!=0:
            self.d += 1
            self.a = int((self.a) / 10)
        print(self.d)

class B2(A):
    def sum(self):
        self.total = 0
        while self.a!=0:

            total += self.a % 10
            self.a = int(self.a) // 10
        print(total)

obj1 = B1()
obj1.c()
obj2 = B2()
obj2.sum()
