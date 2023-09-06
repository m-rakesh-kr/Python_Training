#defining a function for checking stack is empty or not.
def IsEmpty():
    if top==-1:
        return True
    else:
        return False
#defining a function for cheking stack is full or not.
def IsFull():
    if top==size-1:
        return True
    else:
        return False
# defining function for push element
def pushInStack():
    global top,stack
    if IsFull():
        print("Stack is Full (Overflow!)")
    else:
        top+=1
        stack+=" "
        element =input("Enter the element to be Inserted in the stack: ")
        stack[top]=element
        print(stack)
            
# defining function for Pop element
def popInStack(): 
    global top,stack
    if IsEmpty():
        print("\nStack is empty (Underflow!)")
        top=-1
    else:
        print("\nThe Topmost Element of Stack is deleted i.e {}".format(stack[top]))
        stack=stack[:top]
        top=top-1
        print(stack)
        
# defining function for Peep element
def peepInstack():
    pos=int(input("Enter Position For Search:->"))
    if(top-pos<=-1) or pos<0:
        print("\nPosition does not exist! in the stack ..plz select another position")
        return
    else:
        print("\nElement is: {}".format(stack[top-pos]))
      
# defining function for Peep element
def peekInstack():
    if IsEmpty():
        print("\nStack is empty (Underflow!)")
    else:
        print("\nThe element present at the top of the stack is {}".format(stack[top]))


#Creating a empty stack
stack = []
top=-1
#taking size of the stack from user        
while True:
    value=int(input("\nEnter the Size of the Stack: "))
    if value>0:
        size=value
        print("\nStack operations:-")
        # Here creating optons for users
        while True:
            print("\nMENU")
            print("1.PUSH")
            print("2.PEEP")
            print("3.POP")
            print("4.PEEK")
            print("5.Exit")
            choice = int(input("Enter the Choice(1-4): "))

            if choice == 1:
                pushInStack()

            elif choice == 2:
                peepInstack()
                
            elif choice == 3:
                popInStack()
            
            elif choice == 4:
                peekInstack()
            
            elif choice == 5:
                break

            else:
                print("Sorry! You have selected incorrect choice.")
    elif value==0:
    	print("Size of Stack Should not be Zero(Not allowed!)")
    else:
        print("\nPlz enter +ve number only as a size of the stack!")

