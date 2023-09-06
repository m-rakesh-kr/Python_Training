# here we are making a function for insertion sort
def InsertionSort(myList):
    #here finding the lenth of list using for loop.
    listLentth=0
    for l in myList:
        listLentth+=1
    #here we are iterating for loop from 1 to totallength of the list 
    for i in range(1,listLentth):
        currentElement=myList[i]
        position=i
        while currentElement<myList[position-1] and position>0:
            myList[position]=myList[position-1]
            position=position-1
        myList[position]=currentElement

#Creating an empty list.      
mylist=[]
while True:
    size=0
    size=int(input("Enter the size of list: "))
    if size>0:
        for i in range(size):
            element=int(input("Enter {} element of the list ".format(i+1)))
            #appending element in the list one by one.
            mylist+=[element]
        print("\nList before Sorting",mylist)
        #calling selection_sort function.    
        InsertionSort(mylist)
        #displaying list after sorting
        print("\nList after Sorting",mylist)
        break
    elif size<0:
        print("Negative integer is not allow as a size of list")
    else:
        print("Zero is not allowed as a size of list please enter +ve integer")
