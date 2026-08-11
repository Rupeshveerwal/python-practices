class A:
    def parent():
        print("i am parent")

class B(A): 
    def child():
        print("i am child")


o=B
o.parent()
o.child()
