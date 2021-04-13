#pip install mysqlclient
import MySQLdb

db_host = '34.122.175.106'
db_user = 'admin'
db_pass = 'abc@123'
db_name = 'py2103'

conn = MySQLdb.connect(
    db_host, db_user, db_pass, db_name
)
print('Connected')
