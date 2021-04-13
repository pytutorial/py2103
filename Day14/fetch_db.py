import MySQLdb
db_host = '34.122.175.106'#34.122.175.106/phpmyadmin
db_user = 'test'
db_pass = 'abc@123'
db_name = 'py2103'

conn = MySQLdb.connect(
    db_host, db_user, db_pass, db_name
    ,charset='utf8'
)
code = input('Nhập mã sách:')  # " OR 1=1 OR 1="
cursor = conn.cursor()
cursor.execute('SELECT * FROM book WHERE code=%s',[code])
row = cursor.fetchone()
print(row)
#dataset = cursor.fetchall()
#for row in dataset: print(row)