# class A:
#     def value(self):
#         self.a = 5
#         self.b = 10

# class B(A):
#     def add(self):
#         self.c = self.a + self.b
#         print(self.c)

# obj1=B()
# obj1.value()
# obj1.add()


class A:
    def value(self):
        self.a = int(input("Enter 1st value: "))
        self.b = int(input("enter 2nd value: "))

class B(A):
    def add(self):
        self.c = self.a + self.b
        print("answer is : ",self.c)

obj1=B()
obj1.value()
obj1.add()
