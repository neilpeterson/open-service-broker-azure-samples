import MySQLdb as db
import os
import time

# MySQL configurations
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_DATABASE = os.environ['MYSQL_DATABASE']

print("MYSQL_USER: " + MYSQL_USER)
print("MYSQL_PASSWORD: " + MYSQL_PASSWORD)
print("MYSQL_HOST: " + MYSQL_HOST)
print("MYSQL_DATABASE: " + MYSQL_DATABASE)

con = db.connect(user=MYSQL_USER,passwd=MYSQL_PASSWORD,host=MYSQL_HOST,db=MYSQL_DATABASE)
cur = con.cursor()

while True:
    cur.execute('''CREATE TABLE IF NOT EXISTS hello_osba (hello_osba INT(2))''')
    time.sleep(15)