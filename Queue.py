# defining function for enqueue element
def IsEmpty():
    if rear==front==-1:
        return True
    else:
        return False   
#defining a custom function for checking queue is full or not
def IsFull():
    if counter==size:
        return True
    else:
        return False
# defining function for enqueue element
def enqueue():
    global rear,myQueue,counter
    if IsFull():
        print("Queue is Full..(Overflow!)")
    else:
        rear+=1
        myQueue+=" "
        item = input("Enter the element to be Inserted in the Queue: ")
        myQueue[rear]=item
        counter+=1
        print(myQueue)
# defining function for peek element
def peek(myQueue):
    if IsEmpty():  
        print("\nQueue is empty (Underflow!)")
    else:
        print("\nThe element present at the front of the queue is {}".format(myQueue[0]))

# defining function for dequeue element
def dequeue():
    global front,rear,myQueue,counter
    if IsEmpty():   
        print("\nQueue is empty (Underflow!)")
    else:
        front=0
        print("\nFront element {} of queue is deleted".format(myQueue[front]))
        myQueue=myQueue[front+1:]
        rear -= 1
        print(myQueue)
        if myQueue==[]:
            front=-1
            rear=-1
            counter=0
#Creating a empty Queue
myQueue =[]
rear=-1
front=-1
counter=0
while True:
    value=int(input("\nEnter the size of Queue: ")) 
    if value>0:
        size=value
        print("\nQueue operations:-")
        # Here creating optons for users
        while True:
            print("\nMENU")
            print("1.enqueue")
            print("2.peek")
            print("3.dequeue")
            print("4.exit")
            choice = int(input("Enter the Choice: "))

            if choice == 1:
                enqueue()

            elif choice == 2:
                peek(myQueue)

            elif choice == 3:
                dequeue()

            elif choice == 4:
                break

            else:
                print("Sorry! You have selected incorrect choice.")
    elif value==0:
    	print("Size of Queue Should not be Zero(Not allowed!)")
    else:
        print("\nPlz enter +ve number only as a size of the Queue!")
