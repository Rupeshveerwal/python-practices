a = {
    "name" : "Rupesh",
    "age"   : 25,
    "class" : "BCA",
}

b = dict(
    marks = 99.99,
    city = "Udaipur"
)


c = a | b

# c = a.update(b)

print(c)

for key in c:
    print(key," : ",c[key],"\n")
    