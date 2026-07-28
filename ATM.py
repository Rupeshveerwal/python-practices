pin = 1212
bank_Balance = 1000

Pin_verify = int(input("Enter your ATM Pin"))

if Pin_verify==pin:
    print("Welcome to Our Bank")
    print("Press 1 to Deposit")
    print("Press 2 to Withdrawal")
    print("Press 3 to Check Balance")
    print("Press 4 to Change Pin")
    
    Button = int(input("Press Here: "))

    if Button==1:
        Deposited_Amount = int(input("Enter amount to Deposit: "))
        bank_Balance = bank_Balance + Deposited_Amount
        print("Your Amount is Deposted")
        print("Your Remaining Balance is :",bank_Balance)

    elif Button==2:
        Withdrawal_Amount = int(input("Enter amount to Withdraw: "))
        if Withdrawal_Amount <= bank_Balance:
            print("Your amount is withdrawn")
            bank_Balance -= Withdrawal_Amount
        else:
            print("Bank Balance is not Enough")

    elif Button==3:
        print(bank_Balance, " is your Bank Balance")

    elif Button==4:
        print("changed")
    

else:
    print("Wrong Pin Entered")