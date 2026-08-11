class A:
    def marks(self):
        self.a=int(input("Enter: "))
        self.b=int(input("Enter: "))
        self.c=int(input("Enter: "))
        self.d=int(input("Enter: "))

class B(A):
    def total(self):
        self.total=self.a+self.b+self.c+self.c+self.d
        print(self.total)

class C(B):
    def per(self):
        self.p = self.total/400*100
        print(self.p)

class D(C):
    def division(self):
        if self.p>=60:
            print("Div : A")
        elif self.p>=45 and self.p < 60:
            print("Div : B")
        elif self.p>=35 and self.p<45 :
            print("Div : C")
        else:
            print("Fail")

obj1=D()

obj1.marks()
obj1.total()
obj1.per()
obj1.division()

