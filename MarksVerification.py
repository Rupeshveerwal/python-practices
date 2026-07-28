Max = 100
Min = 0

S1 = Sub1 =  int(input("Enter English Marks: "))
S2 = Sub2 =  int(input("Enter Maths Marks: "))
S3 = Sub3 =  int(input("Enter Science Marks: "))
S4 = Sub4 =  int(input("Enter Hindi Marks: "))
S5 = Sub5 =  int(input("Enter Social Marks: "))

Total = S1+S2+S3+S4+S5

percentage = Total/500*100


if  Min <= S1 and S1 <= Max and Min <=S2 and S2 <= Max and Min <=S3 and S3 <= Max and Min <=S4 and S4 <= Max and Min <=S5 and S5 <= Max:  
        print("Sum : ",Total) 
        if percentage >= 60 and percentage <= 100 :
                print("Passed in 1st Division")


        elif percentage >= 45 and percentage <= 60 :
                print("Passed in 2nd Division")


        elif percentage >= 35 and percentage <= 45 :
                print("Passed in 3rd Division")

        else :
            print("Failed")
        
else :
                print("Invalid Marks Enter Again") 
                print("Sum : ",Total) 
    
print("Finished")
