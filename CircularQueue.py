#defining a custom function for checking Queue is empty or not
def IsEmpty():
    if rear==front==-1:
        return True
    else:
        return False
#defining a custom function for checking queue is full or not
def IsFull():
    if (front == rear+1 or front==0 and rear==size-1):
        return True
    else:
        return False

#defining function for enqueue element
def enqueue(circularQueue):
    global front
    global rear
    if IsFull():
        print("Circular Queue is Full (Overflow!)")
    else:
        if front==-1:
            front=0
        rear=(rear+1)%size
        item = int(input("Enter the element to be Inserted in the Circular Queue: "))
        circularQueue[rear]=[item]
        print(circularQueue)   
#defining function for dequeue element
def dequeue(circularQueue):
    global front
    global rear
    if IsEmpty():
        print("\nCircular Queue is Empty (Underflow!)")
    elif front==rear:
        print("\nThe element present at the front of the circular queue {} is deleted".format(circularQueue[front]))
        circularQueue[front]=None
        front=-1
        rear=-1
        print(circularQueue)
    else:
        print("\nThe element present at the front of the circular queue {} is deleted".format(circularQueue[front]))
        circularQueue[front]=None
        front+=1
        print(circularQueue)

#defining function for show front element
def frontElement():
    if IsEmpty():
        print("\nCircular Queue is Empty (Underflow!)")
    else:
        print("\nThe element present at the front of the circular queue is {}".format(circularQueue[front]))

#defining function for show front element
def rearElement():
    if IsEmpty():
        print("\nCircular Queue is Empty (Underflow!)")
    else:
        print("\nThe element present at the rear of the circular queue is {}".format(circularQueue[rear]))

# Here creating optons for users
while True:
    value=int(input("\nEnter the Size of Circular Queue: "))
    if value>0:
        size=value
        #Creating a empty CircularQueue
        circularQueue =[None]*size
        front=-1
        rear=-1
       
        print("\nCircular Queue operations:-")
        while True:
            print("\nMENU")
            print("1.Front:Get the front item from the Circular queue.")
            print("2.Rear:Get the rear item from the Circular queue")
            print("3.enqueue")
            print("4.dequeue")
            print("5.exit")
            choice = int(input("Enter the Choice: "))
            
            if choice == 1:
                frontElement()
            elif choice == 2:
                rearElement()
            elif choice == 3:
                enqueue(circularQueue)
            elif choice == 4:
                dequeue(circularQueue)
            elif choice == 5:
                break
            else:
                print("Sorry! You have selected incorrect choice.")
    elif value==0:
        print("Size of the Circular Queue should not be Zero(Not allowerd!)")
    else:
        print("\nPlz enter +ve number only as a size of the Circular Queue!")
