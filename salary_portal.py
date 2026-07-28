SALARY = int(input("Enter basic salary ="))
HRA = int(input("Enter HRA ="))
TA = int(input("Enter TA ="))
DA = int(input("Enter DA ="))
PF = int(input("Enter PF ="))
LIC = int(input("Enter LIC ="))
TAX = int(input("Enter tax ="))
DEDUCT = LIC+TAX+PF

GROSS = SALARY+HRA+TA+DA
print("gross = ",GROSS) 

NET_SALARY = GROSS-DEDUCT
print("Net salary = ", NET_SALARY)