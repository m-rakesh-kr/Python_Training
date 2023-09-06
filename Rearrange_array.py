def rearrange(mylist):
    arrayLen =0
    for i in mylist:
        arrayLen+=1
   
    for i in range(arrayLen):
        mylist[mylist[i] % arrayLen] += i * arrayLen
   
    # here traversing the modified list and assigning value (mylist[i] = mylist[i] // arrayLen)
    for i in range(arrayLen):
        mylist[i] = mylist[i] // arrayLen 

#mylist = [1, 3, 4, 2, 0]
        
while True:
    size=input("Enter the Size of list(+ve Integer): ")
    if size.isdigit() and size!='0':
        size=int(size)
        mylist=[]
        print("Enter the elements of list: ")
        i=1
        while i<size+1:
            value=input(f"Enter {i} value: ")
            if value.isdigit():
                value=int(value)
                if value<size:
                    if value not in mylist:
                        mylist+=[value]
                        i=i+1
                    else:
                        print("Repeat not allowed!")
                else:
                    print(f"Value must be less than the size of an array! i.e {size}")
            else:
                print("Value must be digit only!")
        print("List before rearrange",mylist)
        rearrange(mylist)
        print("List after rearrange ",mylist)
        break
        
    else:
        print("Size of list must be digit excep 0 only!")
        
