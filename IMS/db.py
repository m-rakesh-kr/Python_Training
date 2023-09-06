import  psycopg2
class db_operation:
    def __init__(self):
        try:
            self.conn=psycopg2.connect(
                        host='localhost',
                        dbname='ims',
                        user='rakesh',
                        password='password',
                        port='5432')
            self.cur=self.conn.cursor()
        except Exception as e:
            print("Something Went Wrong!",e)

    def db_close(self):
            self.conn.commit()
            self.cur.close()
            self.conn.close()

    def execute_all_qry(self,q,s):
        try:
            ack=self.cur.execute(q,s)
            self.db_close()
            return ack
        except Exception as e:
            print(e)

    def select_qry(self,q):
        try:
            self.cur.execute(q)
            f_data=self.cur.fetchall()
            self.db_close()
            return f_data
        except Exception as e:
            print(e)

    def select_qry2(self,q,s):
        try:
            self.cur.execute(q,s)
            f_data=self.cur.fetchall()
            self.db_close()
            return f_data
        except Exception as e:
           print(e)
        