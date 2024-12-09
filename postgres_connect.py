import psycopg2

def create_employee_table():
    connection=psycopg2.connect(user="manoj",password="redhat",port=5432,host="localhost",database="tomtom_db") # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    cursor.execute('create table if not exists employee (empid integer primary key,empname text,empsal real)') # excecute sql query
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection

create_employee_table()

def add_employee(id,name,sal):
    connection = psycopg2.connect(user="manoj", password="redhat", port=5432, host="localhost",
                                  database="tomtom_db")  # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    cursor.execute('insert into employee values(%s,%s,%s)',(id,name,sal)) # excecute sql query
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection

# add_employee(1000,"shilpa",99.78)
# add_employee(2000,"shridhar",88.82)
# add_employee(3000,"shuvra",89.28)
# add_employee(4000,"vinay",87.78)

def select_employee_table():
    connection = psycopg2.connect(user="manoj", password="redhat", port=5432, host="localhost",
                                  database="tomtom_db")  # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    cursor.execute('select * from employee') # excecute sql query
    all_rows=cursor.fetchall()
    #print(all_rows)
    #print(list(all_rows))
    print("Here all_rows is generator returning tuple with three values!")
    for each_record in all_rows:
        print(each_record[0],each_record[1],each_record[2])
    print("using multiple varibale assignments to unpack tuple...")
    all_rows = cursor.execute('select * from employee')
    all_rows = cursor.fetchall()
    for id,name,sal in all_rows:
        print(id,name,sal)
    all_rows = cursor.execute('select * from employee')
    all_rows = cursor.fetchall()
    store_list=list(all_rows)
    print("total number of records",len(store_list))
    all_rows = cursor.execute('select * from employee')
    first_record = cursor.fetchall()
    print("First record is",first_record)
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection

#select_employee_table()


def update_employee(id,sal):
    connection = psycopg2.connect(user="manoj", password="redhat", port=5432, host="localhost",
                                  database="tomtom_db")  # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    cursor.execute('update employee set empsal=%s where empid=%s',(sal,id)) # excecute sql query
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection


update_employee(1000,99999.9999)

select_employee_table()

def delete_employee(id):
    connection = psycopg2.connect(user="manoj", password="redhat", port=5432, host="localhost",
                                  database="tomtom_db")  # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    cursor.execute('delete from employee where empid=%s',(id,)) # excecute sql query
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection

delete_employee(2000)