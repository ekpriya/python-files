import mysql.connector


def check_mysql():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root@123"
    )
    print(mydb)





def create_database():

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123"
  )

  mycursor = mydb.cursor()

  mycursor.execute("CREATE DATABASE kavipriya")




def show_database():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123"
    # database="SampleDB"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SHOW DATABASES")
  for x in mycursor:
      print(x)




def create_table():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123",
    database="kavipriya"
  )

  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE employee_records (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


def show_tables():
  import mysql.connector

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123",
    database="kavipriya"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SHOW TABLES")

  for x in mycursor:
    print(x)



def insert_valuesinto_tables():
  import mysql.connector

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123",
    database="kavipriya"
  )
  mycursor = mydb.cursor()

  sql = "INSERT INTO employee_records ( name, address) VALUES (%s, %s)"
  val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),

  ]

  mycursor.executemany(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "was inserted.")
#

def view_data_table():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123",
    database="kavipriya"
  )
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM employee_records")

  myresult = mycursor.fetchall()

  for x in myresult:
        print(x)


def insert_new_row():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root@123",
      database="kavipriya"
      )
    mycursor = mydb.cursor()
    mycursor.execute("ALTER TABLE employee_records ADD COLUMN age INT (10)")

#
#
#
def delete_record():
   mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="root@123",
     database="kavipriya"
   )

   mycursor = mydb.cursor()


   sql = "DELETE FROM employee_records WHERE address = 'Mountain 21'"

   mycursor.execute(sql)

   mydb.commit()

   print(mycursor.rowcount, "record(s) deleted")
#
#
#
#
#
def drop_table():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@123",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  print("table died")
  #sql = "DROP TABLE employee"
  sql = "DROP DATABASE mydatabase"
  mycursor.execute(sql)


# def create_database():
#     mydb = mysql.connector.connect(
#       host="localhost",
#       user="root",
#       passwd="root@123"
#     )
#
#     mycursor = mydb.cursor()
#
#     mycursor.execute("CREATE DATABASE SampleDB")



#check_mysql()
#create_database()
#show_database()
#create_table()
#insert_valuesinto_tables()
#show_tables()
#view_data_table()
insert_new_row()
# delete_record()
# drop_table()
