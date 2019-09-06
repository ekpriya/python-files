import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root@123"
    )
print(" 1: create a table to insert the data \n",
      "2: insert data \n" ,
      "3: read all the data \n",
      "4: read by id \n",
      "5: update the values \n",
      "6: delete the values \n",
      "....CHOOSE YOUR OPTION ....")
def get_count():
    emp_count = int(input('ENTER:'))
    return emp_count

def switch_case(emp_count):
    switcher ={
        1 : check_mysql(),
        2: " This is Case Two ",
        3: "333",
        4: "4444",
        5:"asdf",
        6: "666"

    }
    print( switcher.get(emp_count))


def check_mysql():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root@123"
    )
    print(mydb)


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




switch_case(emp_count=get_count())