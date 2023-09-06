import random
#defining a function for generating random number of 4 digit.
def gen_random_num():
    #temp_set=set()
    ran_num=random.randint(1000,9999)
    return ran_num
    """
    for i in str(ran_num):
        temp_set.add(i)
    if len(temp_set)==4:
        return ran_num
    else:
        temp_set.clear()
        return gen_random_num()
    """
#defining a function for taking input from user.
def taking_user_num():
    while True:
        #print(num1)
        user_num=input("\nGuess the 4-digit number?\n")
        if len(user_num)==4 and user_num.isdigit():
            return int(user_num)
        else:
            print("You have Guessed wrong number!")
#defining a function game_on, which will compare these two numbers and increment bulls and cows a/c to logic...
def game_on(num1,num2):
    cows=0
    bulls=0
    num1=str(num1)# random number
    num2=str(num2)# user number
    
    num1_list=[n1 for n1 in num1]
    num2_list=[n2 for n2 in num2]
    for i in range(0,4):
        if num1[i]==num2[i]:
            cows+=1
            num1_list.remove(num2[i])
            num2_list.remove(num2[i])
    for n in num1_list:
        if(n in num2_list):
            bulls+=1
            num2_list.remove(n)
    return cows,bulls

#game will start from here...
print("{0:-^70s}".format(" WELCOME TO NUMBER'S PREDICTION GAME! "))
print("\nBefore playing this game please read some Instruction as below:-")
print("\n1.Here,Computer generating a random number of 4-digit.\n2.Game is that,now you have to select that generated random number.\n\nif you do so then you will win!\t\tBest of Luck!\n")
#calling num gen fun and asigning returned value in num1
num1=gen_random_num()
#taken variable for counting total attempt during playing game bydefault assigning initial score=0
score=0
#assigning Bydefault user choice true for iterating this while loop 1st time of excution this prgm.
user_choice=True    
while True:
    num2=taking_user_num()
    score=score+1
    cows,bulls=game_on(num1,num2)
    #if cows==4 then game over.
    if cows==4:
        print("You Won the match, You have completed Game in {} round. Thank You! ".format(score))
        print("\nDo You want to play again..?")
        print("If yes Enter 'Y'")
        choice=input("\nEnter Your choice: ")
        if choice=='Y' or choice=='y':
            user_choice=True
        else:
            user_choice=False
            break
    else:
        print("{} Cows, {} Bulls".format(cows,bulls))
        cows=0
        bulls=0           
