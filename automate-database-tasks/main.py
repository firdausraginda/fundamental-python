import psycopg2

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

# create table
cursor.execute('''create table mystaff.employees
        (id int primary key not null,
        first_name varchar(25) not null,
        last_name varchar(25) not null,
        department varchar(25) not null,
        phone varchar(25),
        address varchar(50),
        salary int);
        ''')

# insert some records to table
cursor.execute('''insert into mystaff.employees (id, first_name, last_name, department, phone, address, salary)
        values (1, 'John', 'Smith', 'Sales', '012345678', '1st street, Miami', 50000),
        (2, 'Jack', 'Doe', 'IT', '08213481', '2nd street, NY', 55000),
        (3, 'Emily', 'Davids', 'Sales', '912632341', '3rd street, LA', 59000),
        (4, 'Karen', 'Wilson', 'Logistics', '129087892', '4th street, Las Vegas', 41000),
        (5, 'Emma', 'Richard', 'Marketing', '892364914', '5th street, Denver', 40000);
        ''')

# update a row value
cursor.execute('''update mystaff.employees set department = 'Logistics' where last_name = 'Doe';''')

# delete a row
cursor.execute('''delete from mystaff.employees where salary > 50000;''')

# querying the database with fetchall
cursor.execute('''select * from mystaff.employees where salary between 40000 and 50000;''')
records = cursor.fetchall()
for record in records:
    print(record)

# querying the database with fetchmany
cursor.execute('''select * from mystaff.employees where salary between 40000 and 50000;''')
records = cursor.fetchmany(size=2)
for record in records:
    print(record)

# inserting 1 row to later conduct rollback
cursor.execute('''insert into mystaff.employees (id, first_name, last_name, department, phone, address, salary)
            values (6, 'Jane', 'Sanders', 'HR', '98237643892', '6th street, Miami', 61000);
            ''')

# Rolling back (undoing) the changes/transactions performed since the last commit()
connection.rollback()

# Commiting (saving) the changes/transactions performed since the last commit()
connection.commit()

connection.close()