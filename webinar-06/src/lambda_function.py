import pymysql 
import json 
import sys


def parser_mysql_return(mysql_data):
     students_list = []
     for student in mysql_data:
          dict_return = {' name': student[0], 'email': student[1] }
          students_list.append(dict_return)
     return students_list
    
     
def lambda_handler(event, context):
     
     rds_host='<DATABASE HOST ENDPOINT>'
     name='<DATABASE USER>'
     password='<DATABASE PASSWORD>'
     db_name='<DATABASE NAME>'

     try:
         conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
     except Exception as e:
         print(str(e))
         print("ERROR: Unexpected error: Could not connect to MySql instance.")
         sys.exit()
     print("SUCCESS: Connection to RDS mysql instance succeeded")
     
     cursor = conn.cursor()
     cursor.execute("SELECT firstname, email FROM mdl_user LIMIT 10;")
     students = cursor.fetchall()
     students_list = parser_mysql_return(students)

     return students_list