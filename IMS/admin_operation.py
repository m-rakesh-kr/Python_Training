from db import *
from input_output import *
from query_file import *
from validation import select_id,enter_valid_marks,check_taken_interview,round_no,get_que_category

#-------------Admin_Operations class.......................
class Admin_operation:
    
    def view_applied_applicant(self):
        f_data=db_operation().select_qry(q_applied_applicant)
        if f_data!=[]:
            return f_data
        else:
            return False

    #Operation on Questions............................... 
    def view_question(self):
        f_data=db_operation().select_qry(q_view_que)
        if f_data!=[]:
            return f_data
        else:
            return False

    def add_question(self):
        que=input_que()
        cate=get_que_category()
        t_que=tuple([que,cate])
        if db_operation().execute_all_qry(q_insert_que,t_que)==None:
            succes_msg()
            return True
        else:
            error_msg()
            return False

    def update_question(self):
        f_data=self.view_question()
        if f_data!=False:
            disp_questions(f_data)
            s_id=select_id(f_data)
            que=input_que()
            s_tup=[que,s_id]
            ack=db_operation().execute_all_qry(q_updt_que,s_tup)
            #print(ack)
            if ack==None:
                succes_msg()
                return True
            else:
                error_msg()
                return True
        else:
            return False
        
    def delete_question(self):
        f_data=self.view_question()
        if f_data!=False:
            disp_questions(f_data)
            s_id=select_id(f_data)
            ack=db_operation().execute_all_qry(q_del_que,[s_id])
            #print(ack)
            if ack==None:
                succes_msg()
                return True
            else:
                error_msg()
                return True
        else:
            return False

    #Operation on Job...............................
    def view_job_list(self):
        f_data=db_operation().select_qry(q_view_vacancy)
        if f_data!=[]:
            disp_vacancy(f_data)
            return f_data
        else:
            empty_tab()
            return False

    def add_job(self):
        t_job=input_job()
        if db_operation().execute_all_qry(q_insert_job,t_job)==None:
            succes_msg()
            return True
        else:
            error_msg()
            return False

    def update_job(self,field,s_id,u_field):
            #s_tup=[s_id,u_field]
            ack=db_operation().execute_all_qry(q_update_job.format(field),[u_field,s_id])
            #print(ack)
            if ack==None:
                succes_msg()
                return True
            else:
                error_msg()
                return False

    def delete_job(self):
        f_data=self.view_job_list()
        if f_data!=False:
            s_id=select_id(f_data)
            ack=db_operation().execute_all_qry(q_del_job,[s_id])
            #print(ack)
            if ack==None:
                succes_msg()
                return True
            else:
                error_msg()
                return False
        else:
            return False
        
    def interview_que(self,job_tech):
        f_data=db_operation().select_qry2(q_interview_que,[job_tech])
        if f_data!=[]:
            return f_data
        else:
            question_empty_status()
            return False
        
    def ask_que(self,job_id):
        jt=db_operation().select_qry2(q_job_techno,[job_id])
        job_tech=jt[0][0]
        #print(job_tech)
        f_que=self.interview_que(job_tech)
        #print(f_que)
        if f_que!=False:
            marks=[]
            tup_row=[]
            qn=1
            for r in f_que:
                tup_row.append(r)
                disp_ask_que(tup_row,qn)
                tup_row.clear()
                valid_m=enter_valid_marks()
                marks.append(valid_m)
                qn=qn+1
            return marks
            #end_interview_msg()
        else:
            return False           
              
    def take_interview(self):
        interview_msg()
        f_data=self.view_applied_applicant()
        #print(f_data)
        if f_data!=False:
            disp_applied_applicant(f_data)
            s_id=select_id(f_data)
            if check_taken_interview(s_id)==True:
                get_id=db_operation().select_qry2(q_get_job_id,[s_id])
                job_id=get_id[0][0]
                #print(get_id)
                #print(job_id)
                marks=self.ask_que(job_id)
                if marks!=False:
                    t_marks=sum(marks)
                    t_que=tuple([t_marks,s_id])
                    if db_operation().execute_all_qry(q_ins_interview_rcd,t_que)==None:
                        end_interview_msg()
                        return True
                    else:
                        error_msg()
                        return False
                else:
                    return False
            else:
                taken_interview()
                return False
        else:
            disp_applicant_status()
            return False

    def create_report(self):
        f_data=db_operation().select_qry(q_interviewed_applicant)
        if f_data!=[]:
            interviewed_applicant()
            disp_interviewed_applicant(f_data)
            s_id=select_id(f_data)
            s_id=int(s_id)
            a_id=(s_id,)
            f_report=db_operation().select_qry2(q_create_report,a_id)
            if f_report!=[]:
                report_msg()
                disp_report(f_report)
                return True
            else:
                empty_tab()
                return False
        else:
            empty_tab()
            return False
        
    def next_round_list(self):
        f_data=db_operation().select_qry(q_interviewed_applicant)
        if f_data!=[]:
            interviewed_applicant()
            disp_interviewed_applicant(f_data)
            s_id=select_id(f_data)
            #check_round_status()
            s_r=round_no()
            s_id=int(s_id)
            tup_r=(s_r,s_id)
            ack=db_operation().execute_all_qry(q_applicant_next_round,tup_r)
            if ack==None:
                succes_msg()
                next_round_msg(s_r)
                return True
            else:
                error_msg()
                return False
        else:
            empty_tab()
            return False
