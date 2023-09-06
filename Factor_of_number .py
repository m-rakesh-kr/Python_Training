def factor(num):
    """
    #method-->2 using for loop
    fact=[]
    if num>0:
        for f in range(1, num + 1):
            if num % f == 0:
                fact+=[f]
    else:
        fact=[0]
    print(f"The factors of {num} are: {fact} ")

    """
    #Method-->1 using list comprehension...
    if num>0:   #finding factors for +ve numbers.
        fact=[f for f in range(1,num+1) if num%f==0]

    #elif num<0: #finding factors for -ve numbers.
        #fact=[f for f in range(num,0) if num%f==0]
    else:
        fact=[0]

    print(f"The factors of {num} are: {fact} ")

#taking num from users.
while True:
    num =input("\nEnter the num to find the factor: ")
    if num.isdigit():
        num=int(num)
        factor(num)
        break
    else:
        print("Number must be Numeric only!")
        
        
        
