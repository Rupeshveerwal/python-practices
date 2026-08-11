#ATM using constructor in python  
#4 bje 2 giftv for kitchen chetak madhuban 
import json
try: 
     with open("bank1.json","r")as file:
          bank = json.load(file)
except:
     bank = {}

def write():
     print("Succesfull")
     with open("bank1.json","w")as file:
          json.dump(bank, file, indent=4)


class ATM_Pin:
    def __init__(self):
        self.pin = bank[id]
        self.balance = bank[id]["balance"]
               
    def check(self):
            while True:
                check_pin = int(input("Enter your pin: ")) 
                if check_pin == self.pin:
                    self.check_Account()
                    break
                else:
                    print("Invalid Pin, Try Again\n")
            
    def check_Account(self):
            while True:
                print("\n1. Open New Account")
                print("2. Account details")
                print("3. Amount Deposit")
                print("4. Amount Withdraw")
                print("5. Exit")
                User_Choice = int(input("\nEnter your Choice: "))
                if User_Choice == 1:
                    self.user_name = input("Your Name: ")
                    self.user_pin = int(input("Your Pin: "))
                    self.balance = int(input("Your balance: "))
                    self.age = int(input("Your age: "))
                    if self.age > 18:
                        bank[self.user_pin]=dict(
                              name =  self.user_name,
                              pin = self.user_pin,
                              balance = self.balance,
                              age = self.age
                         )
                        write()
                    else:
                        print("sorry bade ho jao beta")
                    
                elif User_Choice == 2:
                    print("\nYour balance is ",self.balance)

                elif User_Choice == 3:
                    depo = int(input("\nEnter amount to deposit: "))
                    self.balance += depo 
                    print("Your balance is ",self.balance)

                elif User_Choice == 4:
                    wD = int(input("\nEnter amount to Wuthdraw: "))
                    if wD <= self.balance:
                        self.balance -= wD
                        print("\nYour balance is ",self.balance)
                    else:
                        print("\nInsufficient balance\n")

                elif User_Choice == 5:
                    print("Thank you!\n")
                    break
                else:
                    print("Invalid Choice\n")

obj = ATM_Pin()
obj.check()
