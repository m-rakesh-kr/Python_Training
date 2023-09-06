def print_pattern(row_size):
    # here we are taking 3 for loop 1st one will change the row and 2nd one will print the space.
    # and 3rd one print the star  
    for row in range(row_size):
        for space in range(row_size-row-1):
            print(" ",end=" ")
        for star in range(2*row+1):
            print("*",end=" ") 
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
            

