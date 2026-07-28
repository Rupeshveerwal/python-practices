Sub1 = int(input("Enter 1st Subject: "))
Sub2 = int(input("Enter 2nd Subject: "))
Sub3 = int(input("Enter 3rd Subject: "))
Sub4 = int(input("Enter 4th Subject: "))
Sub5 = int(input("Enter 5th Subject: "))

Total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5

percentage = Total/500*100

if percentage >= 60 and percentage <= 100 :
    print("Passed in 1st Division")


elif percentage >= 45 and percentage <= 60 :
    print("Passed in 2nd Division")


elif percentage >= 35 and percentage <= 45 :
    print("Passed in 3rd Division")

else :
    print("Failed")