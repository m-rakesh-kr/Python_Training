def SelectionSort(mylist):
    #here finding the lenth of list using for loop.
    listLentth=0
    for l in mylist:
        listLentth+=1
    #here we are iterating for loop till total length of the list 
    for i in range(listLentth):
        min_index=i
        for j in range(i+1,listLentth):
            if mylist[j]<mylist[min_index]:
                min_index=j
        if mylist[i]!=mylist[min_index]:
            #here swapping index values
            mylist[i],mylist[min_index]=mylist[min_index],mylist[i]

#Creating an empty list.      
mylist=[]
while True:
    size=int(input("Enter the size of list: "))
    if size>0:
        for i in range(size):
            element=int(input("Enter {} element of the list ".format(i+1)))
            #appending element in the list one by one.
            mylist+=[element]
        print("\nList before Sorting",mylist)
        #calling selection_sort function.    
        SelectionSort(mylist)
        #displaying list after sorting
        print("\nList after Sorting",mylist)
        break
    elif size<0:
        print("Negative integer is not allow as a size of list")
    else:
        print("Zero is not allowed as a size of list please enter +ve integer")
