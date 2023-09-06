from validation import *
from db import *
from input_output import *
from query_file import q_view_vacancy,q_apply_job

#-------------Applicant_Operations class.......................
class Applicant_operation:
    def view_vacancy(self):
        f_data=db_operation().select_qry(q_view_vacancy)
        if f_data!=[]:
            return f_data
        else:
            return False               
    def apply_job(self,name,mobile):
        job_list=self.view_vacancy()
        if job_list!=False:
            disp_vacancy(job_list)
            job_id=select_id(job_list)
            ack=check_applied(mobile,job_id)
            if ack==True:
                quali=get_qualification()
                experi=get_job_experi()
                age=get_age()
                gender=get_gender()
                addr=get_address()         
                sel_tup=(name,mobile,quali,gender,int(age),addr,int(job_id),experi)
                #print(sel_tup)
                if db_operation().execute_all_qry(q_apply_job,sel_tup)==None:
                    succes_msg()
                    return True
                else:
                    error_msg()
                    return False
            else:
                already_applied(name)
                return False  
        else:
            disp_job_status()
            return False

    
