from mysql import connector

mydb = connector.connect(host='localhost', user='root', password='15041999', database='record_company')

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM albums')

print(f'mycursor.rowcount : {mycursor.rowcount}')   # -1
print("------------------------------------------------------------------------")

first_record = mycursor.fetchone()
print(first_record)         # a tuple
print(f'mycursor.rowcount : {mycursor.rowcount}')   # 1
print("------------------------------------------------------------------------")

next_three_records = mycursor.fetchmany(3)
print(next_three_records)   # a list of tuples
print(f'mycursor.rowcount : {mycursor.rowcount}')   # 4
print("------------------------------------------------------------------------")

mycursor.next()             # skip the record and go to the next one

remaining_records = mycursor.fetchall()
print(remaining_records)    # a list of tuples
print(f'mycursor.rowcount : {mycursor.rowcount}')
print("------------------------------------------------------------------------")

mycursor.execute(f"SELECT * FROM albums WHERE release_year = {int(input('Year: '))}")
records = mycursor.fetchall()
print(records)    # a list of tuples
print("------------------------------------------------------------------------")

mycursor.execute("SELECT * FROM albums WHERE name = %s", ('Tiara', ))
records = mycursor.fetchone()
print(records)    # a list of tuples
print("------------------------------------------------------------------------")

# print(dir(mycursor))
mydb.close()
