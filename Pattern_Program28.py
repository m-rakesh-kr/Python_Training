def diamond_print(row_size):
    #method-->1 for diamond printing...
    #for upper part of diamond......
    for row in range((row_size//2)+1):
        for space in range(row_size-row-1):
            print(" ",end=" ")
        for star in range(2*row+1):
            print("*",end=" ")
        #here taking print for changing row. 
        print()
    #for lower part of diamond......
    for row in range((row_size//2),0,-1):
        for space in range(0,row_size-row):
            print(" ",end=" ")
        for star in range(1,2*row):
            print("*",end=" ")
        #here taking print for changing row. 
        print()
    """
    #method-->2 for diamond printing...
    #this for loop print the upper part of the diamond
    for i in range((row_size//2+1)):
        print(" "*(row_size-i-1) + "* "*(i+1))
        
    #this for loop print the lower part of the diamond
    for j in range((row_size//2),0,-1):
        print(" "*(row_size-j) + "* "*(j))
    """
#here taking row_size from the user with validation and calling function with row_size as argu.....
while True:
    row_size=input("\nEnter the Row Size: ")
    if row_size.isdigit():
        row_size=int(row_size)
        #if row_size%2!=0:
        if row_size>0:
            diamond_print(row_size)
            break
        else:
            print("Row size must be greater than Zero!")
        #else:
            print("Please Enter odd Number to show proper diamond shape!")
    else:
        print("Row size must be digit only!")
            
