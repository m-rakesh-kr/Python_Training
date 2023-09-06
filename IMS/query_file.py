#...................................Queries variablse..............................

q_apply_job="INSERT INTO applicant_details(full_name,mobile,qualifications,gender,age,address,job_id,applicant_exper) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

q_user_sign_up="INSERT INTO user_details(full_name,mobile,password,status) VALUES(%s,%s,%s,%s)"

q_insert_que="INSERT INTO questions(question,category) VALUES(%s,%s)"

q_view_que="SELECT * FROM questions"

q_updt_que="UPDATE questions SET question=(%s) WHERE id=(%s)"

q_del_que="DELETE FROM questions WHERE id=(%s)"

q_check_applied="SELECT mobile,job_id FROM applicant_details WHERE mobile=(%s) and job_id=(%s)"

q_insert_job="INSERT INTO job_details(job_name,job_type,job_desc,experience,job_techno) VALUES(%s,%s,%s,%s,%s)"

q_view_vacancy="SELECT * FROM job_details"

q_del_job="DELETE FROM job_details WHERE id=(%s)"

q_update_job="UPDATE job_details SET {}=(%s) WHERE id=(%s)"

q_check_username="SELECT mobile,full_name FROM user_details WHERE mobile=(%s) and status=(%s)"

q_check_pswd="SELECT password FROM user_details WHERE mobile=(%s) and status=(%s)"

q_applied_applicant="SELECT ad.id,ad.full_name,ad.mobile,ad.qualifications,ad.gender,ad.applicant_exper,jd.job_name,jd.job_techno,jd.job_type,ad.applied_at FROM applicant_details ad INNER JOIN job_details jd ON ad.job_id=jd.id"

q_insert_user="INSERT INTO user_details(full_name,mobile,password,status) VALUES(%s,%s,%s,%s)"

q_interview_que="SELECT question FROM questions WHERE category=(%s)"

q_ins_interview_rcd="INSERT INTO interview_records(total_marks,a_id) VALUES(%s,%s)"

q_check_taken_interview="SELECT a_id FROM interview_records WHERE a_id=(%s)"

#q_interviewed_applicant="SELECT interview_records.id,applicant_details.full_name,applicant_details.qualifications,applicant_details.job_id FROM interview_records INNER JOIN applicant_details On  interview_records.a_id=applicant_details.id"

q_interviewed_applicant="SELECT ir.id,ad.full_name,ad.qualifications,jd.job_name,ad.applied_at,ir.ap_round FROM interview_records ir INNER JOIN applicant_details ad ON ir.a_id=ad.id INNER JOIN job_details jd ON ad.job_id=jd.id"

q_applicant_next_round="UPDATE interview_records SET ap_round=(%s) WHERE id=(%s)"

q_create_report="SELECT ir.id,ir.total_marks, ir.ap_round, ad.full_name,ad.qualifications,ad.mobile FROM interview_records ir INNER JOIN applicant_details ad ON ir.a_id=ad.id WHERE ir.id=(%s)"

q_check_mob="SELECT mobile FROM applicant_details WHERE mobile='{}'"

q_get_job_id="SELECT job_id FROM applicant_details WHERE id=(%s)"

q_job_techno="SELECT job_techno FROM job_details WHERE id=(%s)"



