import db
from users import *
from applicant import *
from input_output import *
from admin_operation import *
from validation import validate_job

#------------------------Operation on Job Driver-----------------------
def update_job_list(obj):
    f_data=obj.view_job_list()
    if f_data!=False:
        s_id=select_id(f_data)
        while True:
            print("\n***** Updatable fields of Jobs(Vacancies)*****")
            print("\n1.Job Name\t2.Job_Type\t3.Job Description\t4.Experience\t5.Job Technology\t6.Exit")
            ch=input("\nEnter Your Choice: ")
            if ch.isdigit():
                if ch=='1':
                    job_nm=input("Enter Job_name: ")
                    job_nm=validate_job(job_nm)
                    field='job_name'
                    obj.update_job(field,s_id,job_nm)
                elif ch=='2':
                    job_type=input("Enter Job type: ")
                    job_type=validate_job(job_type)
                    field='job_type'
                    obj.update_job(field,s_id,job_type)
                elif ch=='3':
                    job_desc=input("Enter Job Description: ")
                    field='job_desc'
                    obj.update_job(field,s_id,job_desc)
                elif ch=='4':
                    job_exp=input("Enter Job experience in yrs(Interval 0-1,1-2): ")
                    field='experience'
                    obj.update_job(field,s_id,job_exp)
                elif ch=='5':
                    job_tech= get_job_techno()
                    field='job_techno'
                    obj.update_job(field,s_id,job_tech)

                elif ch=='6':
                    print("Returned to Admin Section MENU!\n")
                    return False
                else:
                    print("You have Entered Invalid option try again!")
            else:
                print("Choice must be digit only!")

def job_list(obj):
    while True:
        print("\n***** Operations on Jobs(Vacancies)*****")
        print("\n1.View Job\t2.Add Job\t3.Update Job\t4.Delete Job\t5.Exit")
        ch=input("\nEnter Your Choice: ")
        if ch.isdigit():
            if ch=='1':
                obj.view_job_list()
            elif ch=='2':
                obj.add_job()
            elif ch=='3':
                update_job_list(obj)
            elif ch=='4':
                obj.delete_job()
            elif ch=='5':
                print("Returned to Admin Section MENU!\n")
                return False
            else:
                print("You have Entered Invalid option try again!")
        else:
            print("Choice must be digit only!")

#------------------------Operation on Questions Driver---------------------
            
def question_list(obj):
    while True:
        print("\n***** Operations on Question*****")
        print("\n1.View Question\t\t2.Add Qestions\t3.Update Questions\t4.Delete Question\t5.Exit")
        ch=input("\nEnter Your Choice: ")
        if ch.isdigit():
            if ch=='1':
                f_data=obj.view_question()
                if f_data!=False:
                    disp_questions(f_data)
                else:
                    empty_tab()
            elif ch=='2':
                obj.add_question()
            elif ch=='3':
                obj.update_question()
            elif ch=='4':
                obj.delete_question()
            elif ch=='5':
                print("Returned to Admin Section MENU!\n")
                return False
            else:
                print("You have Entered Invalid option try again!")
        else:
            print("Choice must be digit only!")
            
#------------------------Admin Section Driver---------------------
            
def admin_section():
    print("\n***** Welcome to Admin Section *****")
    while True:
        print("\n***** Operations MENU *****")
        print("\n1.View Applied Applicants\t2.Questions List\t3.Job(vacancies) List\n\n4.Take Interview\t\t5.Create Report\t\t6.Switch to Next Round\t7.Log Out")
        ch=input("\nEnter Your Choice: ")
        if ch.isdigit():
            obj=Admin_operation()
            if ch=='1':
                f_data=obj.view_applied_applicant()
                if f_data!=False:
                    disp_applied_applicant(f_data)
                else:
                    disp_applicant_status()
            elif ch=='2':
                question_list(obj)
            elif ch=='3':
                job_list(obj)
            elif ch=='4':
                obj.take_interview()
            elif ch=='5':
                obj.create_report()
            elif ch=='6':
                obj.next_round_list()
            elif ch=='7':
                print("Thank You bye!\n")
                return False
            else:
                print("You have Entered Invalid option try again!")
        else:
            print("Choice must be integer only!")
                          
#-----------------------Applicant Section Driver---------------------
            
def applicant_section(name,mobile):
    print("\n***** Welcome to Candidate Section *****")
    while True:
        print("\n***** Operations MENU*****")
        print("\n1.Apply for Job\t\t2.View Vacancies(Job) list\t3.Log out")
        ch=input("\nEnter Your Choice: ")
        if ch.isdigit():
            obj=Applicant_operation()
            if ch=='1':
                obj.apply_job(name,mobile)
            elif ch=='2':
                f_data=obj.view_vacancy()
                if f_data!=False:
                    disp_vacancy(f_data)
                else:
                    disp_job_status()
            elif ch=='3':
                print("Thank You bye!\n")
                return False
            else:
                print("You have Entered Invalid option try again!")
        else:
            print("Choice must be digit only!")
                    

#------------------------Main Driver---------------------------------
            
def authentication():
    print("\n***** Welcome to Interview Management System *****\n")
    while True:
        print("1.Login\t\t2.Sign up\t3.Exit")
        ch=input("\nEnter Your Choice: ")
        if ch.isdigit():
            obj=User_authen()
            if ch=='1':
                ack,name,mobile=obj.user_login()
                if ack !='db_error':
                    if ack=='1':
                        admin_section()
                    elif ack=='0':
                        applicant_section(name,mobile)
                else:
                    error_msg()     
            elif ch=='2':
                obj.user_sign_up()
            elif ch=='3':
                break
        else:
            print("Choice must be digit only!\n")

#Program will be start from here...
if __name__ == "__main__":
    authentication()
   
#else:
    #print ("Executed when imported")




