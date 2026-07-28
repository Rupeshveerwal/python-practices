x = {
        "Name"  :   "Admin",
        "Age"   :   18,
        "Marks" :   99.99,
        "Course":   "BCA"}
print("Name" in x) 
print("Age" in x) 
print("Marks" in x) 
print("Course" in x) 
print()
print("Name" not in x) 
print("Age" not in x) 
print("Marks" not in x) 
print("course" not in x) 


k = len(x)
print(k)

x.pop("Name")
print(x)

