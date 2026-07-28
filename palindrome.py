

def check_Palindrome(text):
    b = ""

    for i in text:
        b=  i + b
    print (b)


    if b == text:
        print("your word is palindrome")
    else:
        print("Not pelindrome")



text=input("enter Text: ")
check_Palindrome(text)