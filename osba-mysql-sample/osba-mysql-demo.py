import MySQLdb as db
import os

# MySQL configurations
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_HOST = os.environ['MYSQL_HOST']

print(MYSQL_USER)
print(MYSQL_PASSWORD)
print(MYSQL_HOST)

con = db.connect(user=MYSQL_USER,passwd=MYSQL_PASSWORD,host=MYSQL_HOST)

cur = con.cursor()
cur.execute('CREATE DATABASE hello_osba;')