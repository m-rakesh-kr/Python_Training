def print_pattern(row_size):
    num=0
    count1=0
    count2=0
    # here we are taking 2 for loop 1st one will change the row and 2nd one will print the space.  
    for r in range(1,row_size+1):
        for s in range(1,(row_size-r)+1):
            print("  ", end="")
            count1=count1+1
        #here while loop prints the no. item in each row
        while num!=((2*r)-1):
            if count1<=row_size-1:
                print(r+num, end=" ")
                count1=count1+1
            else:
                count2=count2+1
                print(r+num-(2*count2), end=" ")
            num=num+1
        count2=count1=num=0
        print()
while True:
    row_size=input("\nEnter the Row Size: ")
    if row_size.isdigit():
        row_size=int(row_size)
        if row_size>0:
            print_pattern(row_size)
            break
        else:
            print("Row size must be greater than Zero!")
    else:
        print("Row size must be digit only!")
            

