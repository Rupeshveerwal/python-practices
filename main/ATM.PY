bank = []

for i in range(5):
    amount = int(input("Enter Amount : "))
    bank.append(amount)
    # amount.append(bank[i])
    i = i +1

print(bank)

bank.pop()
print(bank)



