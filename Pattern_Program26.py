#here taking a var for starting number bydefault storing 1
start=1
def print_pattern(start,row_size):
# here we are taking 2 for loop 1st one will change the row and 2nd one will print the num/pattern.  
    for i in range(1,row_size+1):
        for j in range(1,i+1):
            print(start,end=" ")
            start=start+1 
        print()
while True:
    row_size=input("\nEnter the Row Size: ")
    if row_size.isdigit():
        row_size=int(row_size)
        if row_size>0:
            print_pattern(start,row_size)
            break
        else:
            print("Row size must be greater than Zero!")
    else:
        print("Row size must be digit only!")
            

  
