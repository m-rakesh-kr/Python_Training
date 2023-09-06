from db import *
from input_output import *
from validation import *
from query_file import q_insert_user

#-------------user_details class.............................    
class User_authen:
    def user_sign_up(self):
        status=user_status()
        mob=get_mobile()
        ack=check_exist_mobile(mob)
        if ack==True:
            name=get_fullname()
            pswd=get_password()
            conf_pswd=get_conf_pswd()
            ack=check_pswd(pswd,conf_pswd)
            sel_tup=(name,mob,pswd,status)
            query=(q_insert_user)            
            if db_operation().execute_all_qry(query,sel_tup)==None:
                regis_success_msg()
            else:
                error_msg()
                self.user_sign_up()
        else:
            return self.user_sign_up() 
                  
    def user_login(self):
        status=user_status()
        mobile_no=get_login_username()
        username,mobile_no,status=check_login_username(mobile_no,status)
        if status!='db_error':
            pswd=get_login_pswd()
            status=check_login_pswd(mobile_no,status,pswd)
            return status,username,mobile_no
        else:
            return 'db_error','db_error','db_error'
