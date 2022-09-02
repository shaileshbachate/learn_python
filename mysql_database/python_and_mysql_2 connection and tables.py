import mysql.connector

myconn = mysql.connector.connect(host='localhost',user='root',password='15041999', database='emp')

mycursor = myconn.cursor()

mycursor.execute('SHOW TABLES')

for tb in mycursor:
    print(tb)

myconn.close()
