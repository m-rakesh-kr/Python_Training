import re
import db
from query_file import q_check_username,q_check_pswd,q_check_taken_interview,q_check_mob,q_check_applied

def get_fullname():
    name=input("Enter Your Full Name: ")
    regex_name = re.compile(r'([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)
    res = regex_name.search(name)
    if res:
        return name
    else:
        print("Name format is not valid!")  
        return get_fullname()

def get_mobile():
    mob_no=input("Enter Your Mobile no: ")    
    if len(mob_no) == 10 and mob_no.isnumeric():
        return mob_no
    else:
        print("Mobile number format is not valid! It must be 10 digit.")
        return get_mobile()

def check_exist_mobile(mob):
        query=(f"Select mobile from user_details where mobile='{mob}'")
        f_data=db.db_operation().select_qry(query)
        if f_data==[]:
            return True
        else:
            print("This mobile Number is existing already! Try another number!\n")
            return False

def user_status():
    cmd=True
    while cmd:
        print("\nUser Type:\n1.Admin \t 2.Applicant")
        opt=input("\nSelect user type: ")
        if opt.isdigit():
            if opt=='1':
                return '1'
            elif opt=='2':
                return '0'
            else:
                print("Something went Wrong! You have entered Invalid num! try again\n")
                cmd=True
        else:
            print("Selection of user type must be digit only!")

def get_password():
    pswd=input("\nEnter Your Password (It must be (8-chars) and atleast 1 [A-Z],[a-z],[0-9],[@]): ")
    if (len(pswd)<8):
        print("Password format is invalid! It must be (8-chars) and atleast 1 [A-Z],[a-z],[0-9],[@]")
        return get_password()
    elif not re.search("[a-z]", pswd):
        print("Password format is invalid! It must be (8-chars) and atleast 1 [A-Z],[a-z],[0-9],[@]")
        return get_password()
    elif not re.search("[A-Z]", pswd):
        print("Password format is invalid! It must be (8-chars) and atleast 1 [A-Z],[a-z],[0-9],[@]")
        return get_password()
    elif not re.search("[0-9]", pswd):
        print("Password format is invalid! It must be (8-chars) andatleast 1 [A-Z],[a-z],[0-9],[@]")
        return get_password()
    elif not re.search("[_@$]", pswd):
        print("Password format is invalid! It must be (8-chars) and atleast 1 [A-Z],[a-z],[0-9],[@]")
        return get_password()
    elif re.search("\s", pswd):
        print("Password format is invalid! It must be (8-chars) and atleast 1 [A-Z],[a-z],[0-9],[@]")
        return get_password()
    else:
        return pswd
    
def get_conf_pswd():
    conf_pswd=input("Enter Confirm Password: ")
    return conf_pswd
    
def check_pswd(pswd,conf_pswd):
    if pswd==conf_pswd:
        return True
    else:
        print("Password is not matching plz try again! ")
        conf_pswd=get_conf_pswd()
        return check_pswd(pswd,conf_pswd)

def get_login_username():
    username=input("Enter your login Username(mobile no): ")
    return username
    
def check_login_username(username,status):
    s_tup=[username,status]
    f_data=db.db_operation().select_qry2(q_check_username,s_tup)
    #print(f_data)
    if f_data!=[] and f_data!=None:
        if str(username)==f_data[0][0]:
            return f_data[0][1],username,status
        else:
            print("Mobile not matching with registered mobile.\n" )
            status=user_status()
            username=get_login_username()
            return check_login_username(username,status)
    else:
        if f_data==None:
            return 'db_error','db_error','db_error'
        else:
            print("Username not found with registered Mobile! Try again!\n")
            status=user_status()
            username=get_login_username()
            return check_login_username(username,status)

def get_login_pswd():
    pswd=input("Enter your login Password: ")
    return pswd
    
def check_login_pswd(username,status,pswd):
    #s_tup=(username,status)
    s_tup=[username,status]
    get_pswd=db.db_operation().select_qry2(q_check_pswd,s_tup,)
    #print(get_pswd)
    if get_pswd!=[] and get_pswd!=None:
        if str(pswd) == get_pswd[0][0]:
            return status
        else:
            print("Password not matching (Incorrect) Try again!\n")
            status=user_status()
            username=get_login_username()
            pswd=get_login_pswd()
            return check_login_pswd(username,status,pswd)
    else:
        if get_pswd==None:
            return 'db_error'
        else:
            print("Username or Password are Wrong Please check and Try again!\n")
            status=user_status()
            username=get_login_username()
            pswd=get_login_pswd()
            return check_login_pswd(username,status,pswd)
            

def check_mob_no(mob):
    mobile=db.db_operation().select_qry(q_check_mob.format(mob))
    if mobile==[]:
        return mob
    else:
        print("This Mobile no is already registered with others applicant! Use another mobile no.\n" )
        mob=get_mobile()
        return check_mob_no(mob)
        
    
def get_qualification():
    quali=input("Enter Your Qualification: ")
    regex_name = re.compile(r'([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)
    res = regex_name.search(quali)
    if res:
        return quali
    else:
        print("Qualification format is not valid!")  
        return get_qualification()

def get_age():
    age=input("Enter Your Age: ")
    if age.isdigit() and int(age)>=16 and int(age)<=40:
        return age
    else:
        print("Age must be digit only and between(16-40)")
        return get_age()

def get_gender():
    print("Gender Categories:\n1.Male\t2.Female")
    gen=input("Select Gender: ")
    if gen.isdigit():
        if gen=='1':
            return 'male'    
        elif gen=='2':
            return 'female'
        else:
            print("You have selected invalid option! try again!\n")
            return get_gender()
    else:
        print("Please Select gender as digit number!\n")
        return get_gender()

def get_address():
    addr=input("Enter Your Address: ")
    regex_name = re.compile(r'([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)
    res = regex_name.search(addr)
    if res:
        return addr
    else:
        print("Address format is not valid!")  
        return get_address()
    

def select_id(f_list):
    s_id=input("\nEnter(Select) Id: ")
    if s_id.isdigit():
        l=[]
        for i in range(len(f_list)):
            for j in range(1):
                l.append(f_list[i][0])
        if int(s_id) in l:
            return s_id
        else:
            print("You have Selected Invalid Id(i.e Not available in table). Try again!\n")
            return select_id(f_list)      
    else:
        print("Id must be digit only. Try again!\n")
        return select_id(f_list)
    
def validate_job(nm):
    regex_name = re.compile(r'([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)
    res = regex_name.search(nm)
    if res:
        return nm
    else:
        print("Input format is not valid!")
        nm=input("Enter again: ")
        return validate_job(nm)

# def validate_job_exp(job_exp):
#     if not job_exp.isalpha():
#         if isinstance(float(job_exp), float):
#             return job_exp
#         else:
#             job_exp=input("Enter Job experience in yrs(Interval 0-1,1-2): ")
#             validate_job_exp(job_exp)
#     else:
#         job_exp=input("Enter Job experience in yrs(Interval 0-1,1-2): ")
#         validate_job_exp(job_exp)

def get_job_experi():
    job_exp=input("Enter Job experience in yrs(numeric 0,1,1.5,2): ")
    if not job_exp.isalpha():
        if isinstance(float(job_exp), float) or isinstance(int(job_exp),int):
            return job_exp
        else:
            print("Experience must be in ")
            get_job_experi()
    else:
        get_job_experi()

def enter_valid_marks():
    m=input("\nEnter marks according to ans(range b/w 1-10): ")
    if m.isdigit():
        return int(m)
    else:
        print("marks must be digit only!")
        return enter_valid_marks()
                        
def check_taken_interview(s_id):
    s_tup=[s_id]
    f_data=db.db_operation().select_qry2(q_check_taken_interview,s_tup)
    if f_data==[]:
        return True
    else:
        return False
    
def round_no():
    rn=input("Enter next round number(2 or 3): ")
    if rn.isdigit() and rn=='2' or rn=='3':
        return int(rn)
    else:
        print("Round number must be digit only! and 2 or 3")
        return round_no()
    
def check_applied(mobile,job_id):
    f_data=db.db_operation().select_qry2(q_check_applied,(mobile,job_id))
    if f_data==[]:
        return True
    else:
        return False

def get_que_category():
    print("\nQuestion Categories are...\n\n1.Python\t2.Java")
    s_cat=input("\nSelect Question Category: ")
    if s_cat.isdigit():
        if s_cat=='1':
            return 'Python'
        elif s_cat=='2':
            return 'Java'
    else:
        print("Selection of Category must be digit only!")
        return get_que_category()


def get_job_techno():
    print("\nJob Technologies are...\n\n1.Python\t2.Java")
    s_cat=input("\nSelect Job technology: ")
    if s_cat.isdigit():
        if s_cat=='1':
            return 'Python'
        elif s_cat=='2':
            return 'Java'
    else:
        print("Selection of job technology must be digit only!")
        return get_que_category()


      

