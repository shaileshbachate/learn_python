# import mysql.connector

# # OR #

from mysql import connector

myconn = connector.connect(host='localhost',user='root',passwd='15041999')

mycursor = myconn.cursor()

mycursor.execute('SHOW DATABASES')

for db in mycursor:
    print(db)

myconn.close()
