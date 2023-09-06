def print_pattern(row_size):
    #creating 2D array with initializing all the index as zero.
    #this 2d array will store all format i.e sequences of pattern.
    myList=[[0 for x in range(row_size)] for y in range(row_size)]
    num=1
    low=0
    high=row_size-1
    total=(row_size+1)//2
#here we are taking four for loop..for upper,right,down and left.
    for i in range(total):
        #this for will be print upper part of square(spiral).
        for j in range(low,high+1):
            myList[i][j]=num
            num=num+1
        #this for will be print right side part of square(spiral).
        for j in range(low+1,high+1):
            myList[j][high]=num
            num=num+1
        #this for will be print downward part of square(spiral).
        for j in range(high-1,low-1,-1):
            myList[high][j]=num
            num=num+1
        #this for will be print left side part of square(spiral).
        for j in range(high-1,low,-1):
            myList[j][low]=num
            num=num+1
        low=low+1
        high=high-1
    
    for i in range(row_size):
        for j in range(row_size):
            print(myList[i][j], end="  ")
        print()
#here taking row_size from the user with validation and calling function with row_size as argu.....       
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
            

  

