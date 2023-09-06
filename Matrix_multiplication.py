while True:
    m1_row=int(input("Enter the row of matrix1: "))
    m1_col=int(input("Enter the column of matrix1: "))
    m2_row=int(input("Enter the row of matrix2: "))
    m2_col=int(input("Enter the column of matrix2: "))

    
    if m1_row<0 or m1_col <0 or m2_row<0 or m2_col<0:
        print("Please Enter +ve row and column  of the matrix!")

    elif m1_row==0 or m1_col ==0 or m2_row==0 or m2_col==0:
        print("ZERO is not allowed! Please Enter +ve row and column  of the matrix!")

    else:
        if m1_col==m2_row:
            #For matrix1 taking input from the user.
            matrix1=[]
            for i in range(0,m1_row):
                temp=[]
                for j in range(0,m1_col):
                    value=int(input("\nEnter Value for matrix1({}x{}) [{}][{}]: ".format(m1_row,m1_col,i,j)))
                    temp+=[value]
                matrix1+=[temp]
            #printing matrix1
            print("Matrix1= ")
            for mat1 in matrix1:
                print(mat1)

            #For matrix1 taking input from the user.    
            matrix2=[]   
            for i in range(0,m2_row):
                temp=[]
                for j in range(0,m2_col):
                    value=int(input("\nEnter Value for matrix2({}x{}) [{}][{}]: ".format(m2_row,m2_col,i,j)))
                    temp+=[value]
                matrix2+=[temp]
            #printing matrix2
            print("\nMatrix2= ")
            for mat2 in matrix2:
                print(mat2)
            
            result=[]
            #assigning zero on all the index of result list to overcome array index out of bound.
            result=[[0 for i in range(0,m2_col)] for j in range(0,m1_row)]
            
            #here finding length of matrices by using custom defined fun.
            def findLength(value):
                count = 0
                for i in value:
                    count+= 1  
                return count    
            m1_len=findLength(matrix1)
            m2_len=findLength(matrix2)
            m2_0_index_len=findLength(matrix2[0])

            for m2_row in range(m1_len):
                for m2_col in range(m2_0_index_len):
                    for row in range(m2_len):
                        result[m2_row][m2_col]+=matrix1[m2_row][row]*matrix2[row][m2_col]
            #printing result of matrix1 and matrix 2.
            print("\nResult of matrix1 X matrix2= ")
            for res in result:
               print(res)
            break
        else:
            print("For multiplication,column of matrix1 and row of matrix2 must be equal")

    
