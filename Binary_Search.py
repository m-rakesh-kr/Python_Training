#defining a function for insert an element in the list
def Insert(mylist,size):
    #find length of the list
    list_len=0
    for i in mylist:
        list_len+=1
    if list_len<size:
        element = int(input("\nEnter the element to be Inserted in the list: "))
        mylist+=[element]
        return mylist
    else:
        print("List is Full..!")
#here making a method of selection sort for sorting list
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
    return mylist

def Binary_search(mylist):       
    if mylist!=[]:
        key=int (input("Enter the key to find in the list: "))
        sorted_list=SelectionSort(mylist)
        low=0
        #here finding the lenth of list using for loop.
        listLength=0
        for l in sorted_list:
            listLength+=1
        high=listLength-1
        find=0
        while low<=high and not find:
            mid=(low+high)//2
            if key==sorted_list[mid]:
                find=1
            elif key>sorted_list[mid]:
                low=mid+1
            else:
                high=mid-1
        if find==1:
            print("key {} is founded in the list".format(key))
        else:
            print("key {} is not founded in the list".format(key))
    else:
        print("List is empty!")
#here we are creating a dynamic list and taking elements of the list from user.     
mylist=[]

while True:
    size=int(input("Enter the Size of list: "))
    if size>0:
        while True:
            print("1.Insert")
            print("2.Search")
            choice=int(input("Enter the choice: "))
            if choice==1:
                #calling Insert function
                Insert(mylist,size)
            elif choice==2:
                
                #calling Binary search function
                Binary_search(mylist)
            else:
                print("Sorry! You have selected incorrect choice.")
                
    elif size==0:
        print("Zero is not allowed..! as a size of list")
                
    else:
        print("\nPlz enter +ve number only as a size of the list!")

