import MySQLdb
import mysql.connector
# db_host ='34.122.175.106'
# db_port = 3306
# db_user = 'admin'
# db_pass = 'abc@123'
# db_name = 'py2103'
db = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    passwd = "root",
)
mycusrsor =  db.cursor()



# conn = MySQLdb.connect(
#     db_host,db_user,db_pass,db_name
# )

print('Connected')