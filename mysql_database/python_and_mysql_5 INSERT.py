from mysql import connector

myconn = connector.connect(host='localhost', user='root', password='15041999', database='record_company')

mycursor = myconn.cursor()

try:
    mycursor.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name VARCHAR(50) NOT NULL, age INTEGER NOT NULL)')
except:
    print("Table already exists OR could not be created")

mycursor.execute('SHOW TABLES')
for tb in mycursor:
    print(tb)
print("------------------------------------------------------------------------")

query = 'INSERT INTO students(id, name, age) VALUES(%s, %s, %s)'
mycursor.execute(query, (1, 'Shailesh', 22))

details = [(2, 'Shubham', 15), (3, 'Chetan', 23), (4, 'Mangesh', 22)]
mycursor.executemany(query, details)
myconn.commit()

mycursor.execute('SELECT * FROM students')
records = mycursor.fetchall()
for record in records:
    print(record)
print("------------------------------------------------------------------------")

query = 'INSERT INTO students(id, name, age) VALUES({}, "{}", {})'
mycursor.execute(query.format(5, 'Suraj', 21))
myconn.commit()

mycursor.execute('SELECT * FROM students')
records = mycursor.fetchall()
for record in records:
    print(f'{record[0]} {record[1]} {record[2]}')
print("------------------------------------------------------------------------")

try:
    mycursor.execute("INSERT INTO students(id, name, age) VALUES (1, 'Shailesh', 22)")
    myconn.commit()
    print('Successfully inserted')
except:
    myconn.rollback()
    print('couldn\'t insert')
print("------------------------------------------------------------------------")

mycursor.execute('DROP TABLE IF EXISTS students')
myconn.close()
