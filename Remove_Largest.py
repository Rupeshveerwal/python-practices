# l = [1,2,3,4,5,6,7,8,55,42,12]

# l.sort()
# print(l[-3])


a = dict(
    name = "Rupesh",
    clas = "pyhton"
)

b = dict(
    sub =  "python",
    city  = "nmh"
)

z = dict(
    **a,**b
)

a.update(b)
print(a)

# print(x)
print(z)

# c = a|b
# print(c)

