def print_pattern(row_size):
    # here we are taking 2 for loop 1st one will change the row and 2nd one  will print the pattern/num.  
    for row in range(0,row_size+1,1):
        for col in range(1,row+1):
            print(col,end=" ")
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
            

