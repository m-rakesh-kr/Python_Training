#Finding determinant of N*N matrice using formula of determinant
def det(m,rc):
    M=[[0 for i in range(0,rc)] for j in range(0,rc)]
    p=1
    deter = 0
    if(rc == 2):
        deter = m[0][0]*m[1][1]-m[0][1]*m[1][0]
        return deter
    else:
        for i in range(0,rc):
            c1 = 0
            c2 = 0
            for j in range(0,rc):
                for k in range(0,rc):
                    if(j != 0 and k != i):
                        M[c1][c2] = m[j][k]
                        c2+=1
                        if(c2>rc-2):
                            c1+=1
                            c2=0
            deter = deter + p*(m[0][i]*det(M,rc-1));
            p=-1*p;
        return deter;

while True:
    rc=int(input("Enter the order of squared matrix: "))
    if rc<0:
         print("Please enter +ve order to find the determinant of the matrix!")
         
    elif rc==0:
        print("ZERO is not allowed! Please enter +ve order to find the determinant of the matrix!")

    else:
        m=[] 
        if rc==1:
            value=int(input("\nEnter Value for ({}x{}) matrix: ".format(rc,rc)))
            print("Determinant of matrix is: ",value)
            break
        else:
            for i in range(0,rc):
                temp=[]
                for j in range(0,rc):
                    value=int(input("\nEnter Value for ({}x{}) matrix : ".format(rc,rc)))
                    temp+=[value]
                m+=[temp]
            #printing matrix1
            print("Matrix= ")
            for i in range(rc):
                for j in range(rc):
                    print(m[i][j],end=" ")
                print()
            #calling determinant function
            determinant=det(m,rc)
            print("Determinant of matrix is: ",determinant)
            break
            
