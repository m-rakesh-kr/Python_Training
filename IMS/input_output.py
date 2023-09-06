from tabulate import tabulate
from validation import validate_job,get_job_techno

def error_msg():
    print("Something Went Wrong. plz Try again!\n")

def empty_tab():
    print("Empty! There is no any data available in Table!")
    return True

def succes_msg():
    print("Transaction Successfully Executed!\n")
    return True

def regis_success_msg():
    print("You have Registered Succesfully! \n")
    return True

def disp_vacancy(f_data):
    print(tabulate(f_data, headers=["Id", "Job Name", "Job Type", "Job Description", "Job Created at", "Experience Required in yrs", "Job Technology"]))
    return True

def disp_applied_applicant(f_data):
    print(tabulate(f_data, headers=["Id", "Full Name", "Mobile No", "Qualifications", "Gender", "Applicant Experience", "Job Name", "Job Technology", "Job Type", "Applied at"]))
    return True

def input_que():
    que=input("Enter Question: ")
    return que

def input_job():
    job_nm=input("Enter Job Name: ")
    job_nm=validate_job(job_nm)
    job_techno=get_job_techno()
    job_type=input("Enter Job Type: ")
    job_type=validate_job(job_type)
    job_desc=input("Enter Job Description: ")
    job_exp=input("Enter Required Job experience in yrs(Interval 0-1,1-2): ")
    t_job=tuple([job_nm,job_type,job_desc,job_exp,job_techno])
    return t_job

def disp_questions(f_data):
    print(tabulate(f_data, headers=["Id", "Question", "Marks of each Question", "Category"]))
    return True

def wrong_id_msg():
    print("You have selected wrong Id(There is no any data(row) availabel in DB from this Id! Try again!\n)")
    return True

def disp_ask_que(r,que):
    print(tabulate(r, headers=[f"Q.no {que} Question asked by the interviewer to the applicant"]))
    return True

    
def disp_job_status():
    print("Sorry,There is no any job created/release!")
    return True

def disp_applicant_status():
    print("There is no any applicant applied for a job till now!")
    return True

def interview_msg():
    print("\n***************Select Applicant for Interview***************\n")
    return True


def end_interview_msg():
    print("\nThank You! for giving the time to interview...My team will be contact you shortly!")
    return True

def taken_interview():
    print("The Interview of the applicant has been done already!")
    return True

def disp_interviewed_applicant(f_data):
    print(tabulate(f_data, headers=["Id", "Name", "Qualification", "Job_Name", "Applied On (Date-Time)", "Round"]))
    return True

def report_msg():
    print("\nReaport Created Succesfully!\n")
    return True

def disp_report(f_report):
    print(tabulate(f_report, headers=["Id", "Total Marks", "Round", "Full Name", "Qualifications", "Mobile Number"]))
    return True
    
def interviewed_applicant():
    print("\n********** List of Interviewed Applicants **********\n")
    return True

def next_round_msg(r):
    print(f"Applicant Successfully Switched for {r} round\n")
    return True

def already_applied(name):
    print(f"Sorry {name} You already applied for this Job!..." )
    return True


def question_empty_status():
    print("Sorry, There is no any questions inserted by Admin for Interview of these tecgnology.")
    return True
