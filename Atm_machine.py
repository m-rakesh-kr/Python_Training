import random
#here  created 2 dic.
#In card_details key->card_number like(112233445566) refer to value->All the details of card holders like(bal,limit,pin,contact..) so on...
card_details={
    112233445566:{'pin':1234,'user_bal':10000,'limit':1,'ac_holder_name':'Rakesh Kumar','bank_name':'SBI','mobile':'9097142242','ac_num':123456789010},
    665544332211:{'pin':4321,'user_bal':10000,'limit':1,'ac_holder_name':'Ramesh Kumar','bank_name':'BOB','mobile':'9097123456','ac_num':310987654321},
    123456654321:{'pin':1661,'user_bal':0,'limit':1,'ac_holder_name':'Paresh Kumar','bank_name':'PNB','mobile':'9097654321','ac_num':123456654321}
    }

#In atm_details key->Bank of ATM ('SBI',BOB ) refer to ATM details like (bal,loc) and atm balance is initialized bydefault 20k and so on...
atm_details={
    'SBI':{
        1:{'atm_bal':20000,'loc':'Ahmedabad'},
        2:{'atm_bal':20000,'loc':'Bihar'},
        3:{'atm_bal':200,'loc':'Delhi'}
    },
    'BOB':{
        1:{'atm_bal':20000,'loc':'Vastrapur'},
        2:{'atm_bal':200,'loc':'Iskon'}
    },
    'PNB':{
        1:{'atm_bal':20000,'loc':'Rajkot'},
        2:{'atm_bal':20000,'loc':'Iskon'}
    }
    
    }
#In admin_details it contain all field related to admin.
admin_details = {
    123456 : {'admin_nm' : 'Rakesh','pin' : 1234 ,'mobile' : 9097142242},
    654321 : {'admin_nm' : 'Gautam','pin' : 4321 ,'mobile' : 7004921821}
}

#starting making modules(functions) from here............
def bank_list():
    bl=list(atm_details.keys())
    print("Bank of ATM list\n")
    #for i in range(len(bl)):
        #print(str(i+1)+"."+ bl[i])
    print("\n".join(bl))
    while True:    
        bank_of_atm=input("\nSelect Your Bank of ATM(eg 1->SBI): ")
        if bank_of_atm in atm_details:
            return (bank_of_atm)    
        else:
            print("Sorry,You have selected Invalid bank name!")
def admin_validation():
    while True:
        admin_id=input("\nEnter your id: ")
        if admin_id.isdigit():
            admin_id=int(admin_id)
            admin_pin=input("\nEnter your password: ")
            if admin_pin.isdigit():
                admin_pin=int(admin_pin)
                if admin_id in admin_details and admin_pin == admin_details[admin_id]['pin']:
                    admin_section() 
                else:
                    print("\nYour logins credentials is wrong Please try again!")
                    return admin_validation()
            else:
                print("User id must be digti only!")
        else:
            print("User id must be digti only!")
        
def admin_section():
    while True:
        print("\n{0:*^50s}".format(" ADMIN SECTION OPERATIONS:- "))
        print("\n1.Operation on User\t2.Operation on ATM\t3.Operation on Bank\t4.Return to Main Menu")
        opt=int(input("\nEnter your option: "))
        if opt==1:
            user_operation()
        if opt==2:
            while True:
                print("\nYou have a these operation to do on ATM\n\n1.Add Money to ATM Machine\t2.Operation On ATM")
                ch=int(input("\nEnter your option: "))
                if ch==1:
                    add_money_atm()
                if ch==2:
                    atm_operation()
                else:
                    print("\nYou have Entered Invalid option Plz Try again!")
        if opt==3:
            bank_operation()
        if opt==4:
            main_menu(loc_of_atm)
        else:
            print("You have Entered Invalid option Plz Try again!")

def user_operation():
    while True:
        print("\n1.Insert User\t2.Update User\t3.Delete User\t4.Return to Admin Section")
        opt=int(input("\nEnter your option: "))
        if opt==1:
            insert_user()
            user_operation()
        if opt==2:
            update_user()
            user_operation()
        if opt==3:
            delete_user()
            user_operation()
        if opt==4:
            admin_section()
        else:
            print("\nYou have entered invalid option Plz Try again!")
def gen_unique_card():
    gen_card = random.randint(100000000000000,9999999999999999)
    for i in card_details.keys():
        if gen_card not in card_details.keys():
            return gen_card
        else:
            return gen_unique_card()
    
def insert_user():
    global card_details
    while True:
        user_name = input("\nEnter User Name : ")
        if user_name.isalpha():
            print("\nChoose bank name from following list: ")
            bank_name=bank_list()
            user_pin = random.randint(1000,9999)
            while True:
                mobile_num =input("\nEnter 10-digit mobile number : ")
                if mobile_num.isdigit() and len(mobile_num)==10:
                    while True:
                            card_num = gen_unique_card()
                            ac_num=random.randint(10000000000,999999999999)
                            card_details[card_num]={'pin':user_pin,'user_bal':2000,'limit':1,'ac_holder_name':user_name,'bank_name':bank_name,'mobile':mobile_num,'ac_num':ac_num}
                            print(f"\nUser Created Succesfully with card number: {card_num}\n")
                            print(card_details[card_num])
                            user_operation()             
                else:
                    print("\nInvalid mobile number format! try again!")
        else:
            print("\nInvalid User name format! try again!")

def update_user():
    global card_details
    while True:
        card=input("\nEnter Card Number: ")
        if card.isdigit(): 
            if card in card_details:
                print("\nList of updatable fields of user: \n1.User Name\n2.Mobile ")
                ch=int(input("\nEnter field of user that you want to update: "))
                if ch==1:
                    while True:
                        new_user_name=input("\nEnter username: ")
                        if new_user_name.isalpha():
                            card_details[card]['ac_holder_name']=new_user_name
                            print("\nUser Updated Succesfully! ")
                            print(card_details[card])
                            return user_operation()
                        else:
                            print("\nInvalid user name format! try again!")
                if ch==2:
                    while True:
                        new_mobile=input("\nEnter new mobile number: ")
                        if new_mobile.isdigit() and len(new_mobile)==10:
                            card_details[card]['mobile']=new_mobile
                            print("\nMobile number updated Succesfully! ")
                            print(card_details[card])
                            return user_operation()
                        else:
                            print("\nInvalid User name format! try again!")
                else:
                    print("\nYou have Entered Invalid option Plz Try again!")
            else:
                print("Sorry! The card number that you have entered is not found in database!")
        else:
            print("Sorry! card number must be digit only!")
def delete_user():
    global card_details
    while True:
        card_num=input("\nEnter card_no of user that you want to delete: ")
        if card_num.isdigit():
            card=int(card_num)
            if card in card_details:
                if card_details[card]['user_bal']==0:
                    del card_details[card]
                    print(f"\nCard number {card} deleted Succesfully! ")
                    return user_operation()
                else:
                    print("\nSorry! You can't delete user until user withraw or settled whole ammount ")
                    return user_operation()      
            else:
                print("Sorry! The card number that you have entered is not found in database!")
        else:
            print("Sorry! card number must be digit only!")

def add_money_atm():
    global atm_details
    while True:
        atm_name=bank_list()
        atm_loc=atm_location(atm_name)
        add_amt=input("Enter ammount to add in ATM: ")
        if add_amt.isdigit():
            add_amt=int(add_amt)
            if add_amt>0 and add_amt%100==0:
                for i in range(1,len(atm_details[atm_name])+1):
                    if atm_details[atm_name][i]['loc']==atm_loc:
                        atm_details[atm_name][i]['atm_bal']+=add_amt
                        print(f"\nAmmount added to {atm_name} ATM of {atm_loc} Successfully!\n")
                        print(atm_details[atm_name][i])
                admin_section()
            else:
                print("Invalid ammount")
        else:
            print("Ammount must be digit only!")
def atm_operation():
    while True:
        print("\n1.Insert(add) ATM \t2.Update ATM\t3.Delete ATM\t4.Return to Admin Section")
        opt=input("\nEnter your option: ")
        if opt.isdigit():
            opt=int(opt)
            if opt==1:
                insert_atm()
                atm_operation()
            if opt==2:
                update_atm()
                atm_operation()
            if opt==3:
                delete_atm()
                atm_operation()
            if opt==4:
                admin_section()
            else:
                print("\nYou have entered invalid option Plz Try again!")
        else:
            print("Option must be digit only!")
def insert_atm():
    global atm_details
    print("\nChoose bank of ATM from following list: ")
    bank_of_atm=bank_list()
    while True:
        atm_bal=input("Enter ATM Balance that you want to Insert first time(min. RS 20000): ")
        if atm_bal.isdigit():
            atm_bal=int(atm_bal)
            if atm_bal>=20000 and atm_bal%100==0:
                while True:
                    atm_loc=input("Enter the locations of ATM: ")
                    if atm_loc.isalpha():
                        total=len(atm_details[bank_of_atm])
                        atm_details[bank_of_atm][total+1]={'atm_bal':atm_bal,'loc':atm_loc}
                        print(f"\nA new ATM at location {atm_loc} Created/Inserted Succesfully! ")
                        print(atm_details[bank_of_atm])
                        return atm_operation()
                    else:
                        print("location of Atm must be Alphabet only!")
            else:
                print("Invalid ammount or ammount format plz try again")
        else:
            print("Balance must be digit only!")
                
def update_atm():
    global atm_details
    while True:
        print("\nChoose bank of ATM from following list: ")
        bank_of_atm=bank_list()
        if bank_of_atm in atm_details:
            print("\nList of updatable fields of ATM details: \n1.ATM Balance\n2.ATM location")
            ch=input("\nEnter field of ATM details that you want to update: ")
            if ch.isdigit():
                if ch=='1':
                    while True:
                        print(f"\nBefore updating fields of {bank_of_atm} Select location of {bank_of_atm} atm:-")
                        atm_loc=atm_location(bank_of_atm)
                        new_add_bal=input("\nEnter ammount to add/update(multiple of 100): ")
                        if new_add_bal.isdigit():
                            new_add_bal=int(new_add_bal)
                            if new_add_bal>0 and new_add_bal%100==0:
                                total_atm=len(atm_details[bank_of_atm])
                                for i in range(1,total_atm+1):
                                    if atm_details[bank_of_atm][i]['loc']==atm_loc:
                                        atm_details[bank_of_atm][i]['atm_bal']=new_add_bal
                                print("\nATM balance Updated Succesfully! ")
                                print(atm_details[bank_of_atm])
                                return atm_operation()
                            else:
                                print("You have entered invalid ammount format!")
                        else:
                            print("Atm ammount must be alphabet only!")
                
                if ch=='2':
                    print(f"\nBefore updating fields of {bank_of_atm} Select location of {bank_of_atm} atm:-")
                    atm_loc=atm_location(bank_of_atm)
                    new_atm_loc=input("\nEnter new ATM location: ")
                    if atm_loc.isalpha():
                        total_atm=len(atm_details[bank_of_atm])
                        for i in range(1,total_atm+1):
                            if atm_details[bank_of_atm][i]['loc']==atm_loc:
                                atm_details[bank_of_atm][i]['loc']=new_atm_loc
                        print("\nNew location of ATM updated Succesfully! ")
                        print(atm_details[bank_of_atm])
                        return atm_operation()
                    else:
                        print("Atm location must be alphabet only!")
                else:
                    print("\nYou have Entered Invalid option Plz Try again!")
            else:
                print("Choice must be digit only!")
                      
def delete_atm():
    global atm_details
    while True:
        print("\nChoose bank of ATM to delete from following list: ")
        bank_of_atm=bank_list()
        if bank_of_atm in atm_details:
            print(f"\nBefore deleting bank of atm Select location of that {bank_of_atm} atm:-")
            atm_loc=atm_location(bank_of_atm)
            total_atm=len(atm_details[bank_of_atm])
            for i in range(1,total_atm+1):
                if atm_details[bank_of_atm][i]['loc']==atm_loc:
                    if atm_details[bank_of_atm][i]['atm_bal']==0:
                        del atm_details[bank_of_atm][i]
                        print(atm_details[bank_of_atm])
                    else:
                        print("\nSorry! You can't delete this ATM until all the ammount of atm withraw or settled to respective bank ")
                        atm_operation()
            print(f"\nATM deleted Succesfully!")
            print(f"Remaining Bank of atm of {bank_of_atm} bank are: {atm_details[bank_of_atm]}")
            return atm_operation()
        
        else:
            print("\nThere is no any user of this entered card number! please try again!")
            
def bank_operation():
    while True:
        print("\n1.Insert(add) Bank \t2.Update Bank\t3.Delete Bank\t4.Return to Admin Section")
        opt=input("\nEnter your option: ")
        if opt.isdigit():
            if opt=='1':
                insert_bank()
                bank_operation()
            if opt=='2':
                update_bank()
                bank_operation()
            if opt=='3':
                delete_bank()
                bank_operation()
            if opt=='4':
                admin_section()
            else:
                print("\nYou have entered invalid option Plz Try again!")
        else:
            print("Option must be digit only!")

def insert_bank():
    global atm_details
    new_bank_name=input("Enter new Bank name: ")
    if new_bank_name.isalpha():
        if new_bank_name not in atm_details:
            atm_details[new_bank_name]={}
            print("New Bank Inserted Succesfully, Now Total bank are as below:-\n" + "\n".join(list(atm_details.keys())))
            #print(atm_details[new_bank_name])
        else:
            print("This bank is already available in database!")
    else:
        print("bank name must be alphabet only!")
def update_bank():
    global atm_details
    print("Select old Bank name from below list: ")
    old_bank_name=bank_list()
    if old_bank_name in atm_details:
        new_bank_name=input("Enter new Bank name: ")
        if new_bank_name.isalpha():
            if new_bank_name not in atm_details:
                temp=atm_details[old_bank_name]
                del atm_details[old_bank_name]
                atm_details[new_bank_name]=temp
                print("New Bank updated Successfully, Now Total bank are as below:-\n" + "\n".join(list(atm_details.keys())))
                #print(atm_details[new_bank_name])
            else:
                print("This bank is already available in database!")
        else:
            print("bank name must be alphabet only!")
    else:
        print("This bank is not available in database!")  
            
def delete_bank():
    global atm_details
    print("Before deleting Select old Bank name from below list: ")
    bank_of_atm=bank_list()
    if bank_of_atm in atm_details:
        del atm_details[bank_of_atm]
        print("Bank deleted Succesfully, Now Total bank are as below:-\n" + "\n".join(list(atm_details.keys())))
        
    else:
        print("This bank is not available in database!")
        
def deposit(card_no):
    while True:
        amt=float(input("\nEnter amount (multiple of 100) to deposit: "))
        if amt%100==0:
            if 0<amt<=25000:
                card_details[card_no]['user_bal']+=amt
                print("\nYour ammount {} successfully deposited!\n\nYour current balance is {}\n".format("Rs %.2f" %amt,"Rs %.2f" %check_balance(card_no)))
                break
            else:
                print("\nSorry! Your have entered out of range ammount! (i.e Bank fixed for you)")
        else:
            print("\nSorry! Only multiple of 100 is allowed to deposit!\n")
def withdraw(card_no,withdrawal_atm):
    while True:
        withdrawal_amt=input("\nEnter ammount (multiple of 100) to withdraw? ")
        if withdrawal_amt.isdigit():
            withdrawal_amt=float(withdrawal_amt)
            if withdrawal_amt%100==0:
                if(withdrawal_amt<=card_details[card_no]['user_bal']):
                    if withdrawal_amt<=15000:
                        #atm_bal=withdrawal_amt
                        #if withdrawal_amt<=(atm_details[withdrawal_atm]['atm_bal']):
                                    
                        if withdrawal_atm!=card_details[card_no]['bank_name']:
                            validate_atm_bal(withdrawal_atm,withdrawal_amt)
                            if (withdrawal_amt+0.05*withdrawal_amt)<card_details[card_no]['user_bal']:
                                card_details[card_no]['user_bal']-=(withdrawal_amt+0.05*withdrawal_amt)
                                print("\nWithdrwal of ammount {} Successfully!".format("Rs %.2f"%withdrawal_amt))
                                print("\nYou have been charged 5% i.e {} for withdrawing money from others ATM ".format("Rs %.2f" %(0.05*withdrawal_amt)))
                                print("\nYour remaining balance is {}".format("Rs %.2f" %check_balance(card_no)))
                                return card_details,atm_details,user_menu()
                            else:
                                print("\nInsufficient balance in your account for withdrwal!\n")
                                user_menu()
                        else:
                            validate_atm_bal(withdrawal_atm,withdrawal_amt)
                            card_details[card_no]['user_bal']-=withdrawal_amt
                            print("\nWithdrwal of ammount {} Successfully!".format("Rs %.2f"%withdrawal_amt))
                            print("\nYour remaining balance is {}".format("Rs %.2f" %check_balance(card_no)))
                            return card_details,atm_details,user_menu()
                        
                    else:
                        print("\nSorry! Your have entered out of range ammount! (i.e Bank fixed for you)")
                else:
                    print("\nSorry! Insufficient balance in your account for withdrwal!")
                    user_menu()
            else:
                print("\nSorry! Only multiple of 100 is allowed to deposit!")
        else:
            print("Ammount must be only digit!")
            
def validate_atm_bal(bank_of_atm,withdrawal_amt):
    l=len(atm_details[bank_of_atm])
    for i in range(1,l+1):
        if atm_details[bank_of_atm][i]['loc']==loc_of_atm:
            print(atm_details[bank_of_atm][i]['loc'])
            if withdrawal_amt<=atm_details[bank_of_atm][i]['atm_bal']:
                atm_details[bank_of_atm][i]['atm_bal']-=withdrawal_amt
                return
            else:
                print("\nSorry! Insufficient balance in this ATM for withdrwal!")
                return user_menu()

def check_balance(card_no):
    return card_details[card_no]['user_bal']

def account_details(card_no):
    
    print("\n{0:*^50s}\n".format(" Account Holder's details "))
    print(f"Account Holder's Name: {card_details[card_no]['ac_holder_name']}\n\nBank Name: {card_details[card_no]['bank_name']}\t\tCard Number: {card_no}")
    print(f"\nMobile No: {card_details[card_no]['mobile']}\t Account Number: {card_details[card_no]['ac_num']}")
    print("\nYour current balance is {}".format("Rs %.2f" %check_balance(card_no)))
    print("\n {0:*^50s}".format(""))

def card_validate():
    while True:
        card_no=input("\nEnter Your Card Number? ")
        if card_no.isdigit():
            card_no=int(card_no)
            if card_no in card_details:
                user_pin=input("Enter Pin: ")
                if user_pin.isdigit():
                    user_pin=int(user_pin)
                    if card_details[card_no]['pin']==user_pin:
                        while True:
                            user_bank=bank_list()
                            if card_details[card_no]['bank_name']==user_bank:
                                return card_no
                            else:
                                print("Sorry! Your card number is not matching with this Bank. Please Select again.")
                    else:
                        print("\nSorry! Wrong Pin!, Your Pin is not matching with card numbers.")
                else:
                    print("Card Pin must be only digit!")
            else:
                print("\nSorry! Your Card Number is not found in database!")
        else:
            print("Card Number must be only digit!")
    
def main_menu(loc_of_atm):
    print("\n\n {0:*^50s}\n".format(f" Welcome to {bank_of_atm} ATM of {loc_of_atm} "))
    while True:    
        print("1.Admin\t\t2.User")
        choice=input("\nEnter the Option: ")
        if choice.isdigit():
            if choice=='1':
                admin_validation()
            if choice=='2':
                user_menu()
            else:
                print("\nSorry! Incorrect command. Please try again.\n")
        else:
            print("Option must be only digit!\n")
                
def user_menu():
    while True:
        print("\n[b] Balance check\t[d] Money Deposit\n\n[w] Money withdrawal\t[ad] Account details\n\n[r] Return to Main Menu\t[q] Exit \n")
        cmd=str(input("\nWhat would you like to do? "))
        if (cmd=='q'):
            print(f"\nThank you for visit {bank_of_atm} ATM of {loc_of_atm} (Goodbye!) \n")
            break
        elif(cmd=='r'):
            return main_menu(loc_of_atm)
        elif (cmd=='b'):
            card_no=card_validate()
            print("\nYour current balance is {}\n".format("Rs %.2f" %check_balance(card_no)))

        elif (cmd=='d'):
            card_no=card_validate()
            deposit(card_no)
                                        
        elif (cmd=='w'):
            while True:
                card_no=input("\nEnter Your Card Number? ")
                if card_no.isdigit():
                    card_no=int(card_no)
                    if card_no in card_details:
                        user_pin=input("Enter Pin: ")
                        if user_pin.isdigit():
                            user_pin=int(user_pin)
                            if card_details[card_no]['pin']==user_pin:
                                while True:
                                    withdrawal_atm=bank_list()
                                    if card_details[card_no]['limit']==1:
                                        withdraw(card_no,withdrawal_atm)
                                        card_details[card_no]['limit']=0
                                    else:
                                        print("\nSorry! Your one day Transaction limit is exhausted!")           
                            else:
                                print("\nSorry! Wrong Pin!, Your Pin is not matching with card numbers.")
                        else:
                            print("Card Pin must be only digit!")
                    else:
                        print("\nSorry! Your Card Number is not found in database!")
                else:
                    print("Card Number must be only digit!")
                    
        elif (cmd=='ad'):
            card_no=card_validate()
            account_details(card_no)         
                             
        else:
            print("\nSorry! Incorrect command. Please try again.\n")
def atm_location(bank_of_atm):
    while True:
        atms=[]
        for i in range(1,len(atm_details[bank_of_atm])+1):
            atms+=[atm_details[bank_of_atm][i]['loc']]
            
        print(f"\n{bank_of_atm} is located in these following location:\n\n" +"\n".join(atms))
        loc_of_atm=input("\nEnter Location Of ATM: ")
        if loc_of_atm.isalpha():
            if loc_of_atm in atms:
                return loc_of_atm
            else:
                print("Sorry Your selected location is not matching with registered location. Try again!")
        else:
            print("Atm location must be alphabet only!")
    
#Program will started here ....
bank_of_atm=bank_list()
loc_of_atm=atm_location(bank_of_atm)
main_menu(loc_of_atm)
