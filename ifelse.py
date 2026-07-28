#shopping cart, evenodd, masx between two no.


amount= int(input("Enter Amount: "))

Discount = 10

if amount >= 2000 :
    DA = amount/100*10
    amount = amount-DA
    print("discounted price ",amount)

else :
    print("you need to buy more than 2000rs to get discount")
