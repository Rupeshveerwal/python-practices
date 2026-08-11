# Non paramterized constructor

# class A:
#     def __init__(self):
#         print("Non parameterized constructor")

#     def show(self,name):
#         print(name)

# obj = A()
# obj.show("Rupesh")


# Parameterized Constructor

class A:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def show(self):
        print(self.name,self.id)

obj = A("admin",101)
obj.show()

username = input("Enter your name: ")
userid = int(input("Enter your ID: "))

class B(A):
    def __init__(self,name,id):
        super().__init__(name,id)

    def display(self):
        print("Name: ",self.name)
        print("ID: ",self.id)

obj2 = B(username,userid)
obj2.display()