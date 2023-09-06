def print_pattern(row_size):
    #here we r taking a list1 which will contain all the element of list2
    list1=[]  
    for i in range(row_size):
        list2=[]
        for j in range(i+1):
            if j==0 or j==i:
                list2.append(1)
            else:
                list2.append(list1[i-1][j-1] + list1[i-1][j])
        list1.append(list2)
        
    for i in range(row_size):
        for j in range(row_size-i-1):
            print(" ",end="")
        for j in range(i+1):
            print(list1[i][j], end=" ")
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
            

