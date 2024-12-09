import sqlite3

def create_employee_table():
    connection=sqlite3.connect('data.db') # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    cursor.execute('create table if not exists employee (empid integer primary key,empname text,empsal real)') # excecute sql query
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection

create_employee_table()

def add_employee(id,name,sal):
    connection=sqlite3.connect('data.db') # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    cursor.execute('insert into employee values(?,?,?)',(id,name,sal)) # excecute sql query
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection

# add_employee(1000,"shilpa",99.78)
# add_employee(2000,"shridhar",88.82)
# add_employee(3000,"shuvra",89.28)
# add_employee(4000,"vinay",87.78)

def select_employee_table():
    connection=sqlite3.connect('data.db') # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    all_rows=cursor.execute('select * from employee') # excecute sql query
    print(all_rows)
    #print(list(all_rows))
    print("Here all_rows is generator returning tuple with three values!")
    for each_record in all_rows:
        print(each_record[0],each_record[1],each_record[2])
    print("using multiple varibale assignments to unpack tuple...")
    all_rows = cursor.execute('select * from employee')
    for id,name,sal in all_rows:
        print(id,name,sal)
    all_rows = cursor.execute('select * from employee')
    all_rows=all_rows.fetchall()
    store_list=list(all_rows)
    print("total number of records",len(store_list))
    all_rows = cursor.execute('select * from employee')
    first_record=all_rows.fetchone()
    print("First record is",first_record)
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection

#select_employee_table()


def update_employee(id,sal):
    connection=sqlite3.connect('data.db') # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    cursor.execute('update employee set empsal=? where empid=?',(sal,id)) # excecute sql query
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection


update_employee(1000,99999.9999)

select_employee_table()

def delete_employee(id):
    connection=sqlite3.connect('data.db') # create the connection to datbase
    cursor=connection.cursor() # create the cursor
    cursor.execute('delete from employee where empid=?',(id,)) # excecute sql query
    connection.commit() # commit or save the sqlquery
    connection.close() # close the connection

delete_employee(2000)