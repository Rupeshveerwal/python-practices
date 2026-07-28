r=[]
for i in range(5):
    a=input("enter string")
    print(a)
    r.append(a)

r.extend(["udaipur","jaipur"])
print(r)