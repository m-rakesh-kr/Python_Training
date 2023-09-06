"""
#method 1 (To check palindrome for characters)
#taking characters from user
num=input("\nEnter any Characters to check the pallindrome or not:")

if str(num)==str(num)[::-1]:
    print("({})is a palindrome".format(num))
else:
    print("({}) is not a palindrome".format(num))
"""
#method 2(To check palindrome for +ve numbers only)
def palindrome(n):
    num=int(n)
    res=0
    while (num>0):
        rem=num%10
        res=res*10+rem
        num=num//10
    if int(n)==res:
         print("({})is a palindrome".format(res))
    else:
        print("({}) is not a palindrome".format(res))        

while True:
    value=input("Enter the Numbers to check Pallindrome: ")
    if value.isdigit():
        palindrome(value)
        break
    else:
        print("Enter positive number only!")
        
