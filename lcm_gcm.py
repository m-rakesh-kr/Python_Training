def lcm(num1,num2):
    #finding lcm............
    if num1 > num2:  
        temp = num1  
    else:  
        temp = num2  
    while(True):  
        if((temp % num1 == 0) and (temp % num2 == 0)):  
            lcm = temp  
            break  
        temp += 1
    return lcm

def gcm(num1,num2):
    temp=0
    #finding gcm............
    #it swapped number of num1 and num2 till condition is False.
    while num2!=0:
        temp = num2
        num2 = num1%num2
        num1 = temp
    gcm = num1
    return gcm
    
print("\nEnter two numbers to find the Lcm and Gcm of that numbers:-")
while True:
    #taking two from user to find the lcm and gcm 
    num1 = input("First Number: ")
    num2 = input("Second Number: ")
    if num1.isdigit() and num2.isdigit():
        num1=int(num1)
        num2=int(num2)
        if num1!=0 and num2!=0:
            lcm=lcm(num1,num2)
            gcm=gcm(num1,num2)
            
            print("\nLCM of ({},{})= {}".format(num1,num2,lcm))
            print("\nGCM of ({},{})= {}".format(num1,num2,gcm))
            break
        else:
            print("Numbers must be greater than Zero(bcoz Zero is a multiple of every number)")
    else:
        print("Number must be digit only!")

