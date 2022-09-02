from mysql import connector

mydb = connector.connect(host='localhost', user='root', password='15041999', database='record_company')

mycursor = mydb.cursor()

try:
    mycursor.execute('CREATE TABLE mytb (id INTEGER PRIMARY KEY, name VARCHAR(50) NOT NULL, age INTEGER NOT NULL)')
except:
    print("Table already exists OR could not be created")

mycursor.execute('SHOW TABLES')
for tb in mycursor:
    print(tb)
print("------------------------------------------------------------------------")


# INSERT #
query = "INSERT INTO mytb VALUES(99, 'shailesh', 22)"
mycursor.execute(query)
mydb.commit()

mycursor.execute('SELECT * FROM mytb')
records = mycursor.fetchall()
for record in records:
    print(record)
print("------------------------------------------------------------------------")


# UPDATE #
query = "UPDATE mytb SET age = 35 WHERE id = 99"
mycursor.execute(query)
mydb.commit()

mycursor.execute('SELECT * FROM mytb')
records = mycursor.fetchall()
for record in records:
    print(record)
print("------------------------------------------------------------------------")


# DELETE #
query = "DELETE FROM mytb WHERE name = 'shailesh'"
mycursor.execute(query)
mydb.commit()

mycursor.execute('SELECT * FROM mytb')
records = mycursor.fetchall()
for record in records:
    print(record)

# mycursor.execute('DELETE FROM mytb')  # deletes all records
# mydb.commit()
print("------------------------------------------------------------------------")

# INSERT #

id = 0
mycursor.execute('SELECT MAX(id) FROM mytb')
max_id = mycursor.fetchone()[0]  # a tuple is fetched, but we need only first item
if max_id: 
    id = max_id
id += 1

query = f"INSERT INTO mytb VALUES({id}, '{input('Name: ')}', {int(input('Age: '))})"
mycursor.execute(query)
mydb.commit()

mycursor.execute('SELECT * FROM mytb')
records = mycursor.fetchall()
for record in records:
    print(record)
print("------------------------------------------------------------------------")

# DROP TABLE
mycursor.execute('DROP TABLE IF EXISTS mytb')

mydb.close()
