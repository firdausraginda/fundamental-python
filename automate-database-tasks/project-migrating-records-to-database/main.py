import psycopg2

f = open(r'./employees.txt')

records = []

# read txt file per line and append to records
for i in f.readlines():
    records.append(i.rstrip('\n').split('/'))

# create connection
try:
    connection = psycopg2.connect(
        database="staff", user="agi", password="coba", host="127.0.0.1", port="5432")
except psycopg2.Error as err:
    print("An error was occured!")
else:
    print("Connection to database was successful!")

# cursor is a dedicated structure that allows to traverse the records of our database
cursor = connection.cursor()  # initialize the cursor

# iterating over the records list and for each inner list, insert it into database
try:
    for i in records:
        cursor.execute('''insert into mystaff.employees (id, first_name, last_name, department, phone, address, salary) 
                        values (%s,%s,%s,%s,%s,%s,%s);''',
                       (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
except psycopg2.Error as err:
    print("An error was occured when inserting the records!")
else:
    print("Records inserted successfully!")

# Commiting (saving) the changes/transactions performed since the last commit()
connection.commit()

connection.close()
