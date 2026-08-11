class papa():
    def parent():
        print("Me hu papa")

class beta1(papa):
    def child1():
        print("me hu beta no. 1")

class beta2(papa):
    def child2():
        print("me hu chota beta")

obj1=beta1
obj2=beta2


obj2.parent()
obj2.child2()

obj1.child1()
obj1.parent()
