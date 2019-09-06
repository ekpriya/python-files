import mysql.connector
from mysql.connector import cursor

print(" 1: Insert  employee data \n" ,
      "2: Get all the employee \n",
      "3: Get by employee id \n",
      "4: Delete by employee id \n",
      "5: Update the data by employee id \n"
      "....CHOOSE YOUR OPTION ....")




def get_option():
    while True:
        try:
            emp_option = int(input('ENTER your option :'))
            assert (emp_option>0)
            return emp_option
        except AssertionError:
            print('number must be greater than zero')
        except Exception as err:
            print(repr(err))

def conditon(emp_option):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root@123",
        database="defaultDB"
    )

    if(emp_option == 1):
        try:
            print(" U HAVE SELECTED OPTION NO: 1.......inserting values into the tables")


            while True:
                try:
                    emp_count = int(input('Employee Count:'))
                    assert (emp_count > 0)
                    break
                except AssertionError:
                    print('number must be greater than zero')

            for i in range(emp_count):
                id = int(input("enter the id :"))
                name = input("enter the name: ")
                address = input("enter your address:")
                cursor.execute("""INSERT INTO emp_records(id, name, address) VALUES(%s,%s, %s)""",(id, name, address))
            mydb.commit()
            print("values inserted")

        except Exception as err:
            print(repr(err))

    elif(emp_option == 2):
        try:
            print("option to view the data in the table")

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM emp_records")

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)
        except Exception as err:
            print(repr(err))


    elif(emp_option == 3 ):
        try:
            print("THIS option is for getting employee by ID")


            mycursor = mydb.cursor()
            id = int(input("enter id:"))
            mycursor.execute("SELECT * FROM emp_records WHERE id = %s", (id,))
            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

        except Exception as err:
            print(repr(err))



    elif (emp_option == 4):
        try:


            mycursor = mydb.cursor()
            id = int(input("enter id to be deleted "))
            mycursor.execute("DELETE FROM emp_records WHERE id = %s", (id,))
            mydb.commit()
            print("value deleted")


        except Exception:
            print("Id error")

    elif(emp_option == 5):
        print("update the data in the table by id ")
        try:


            mycursor = mydb.cursor()
            id = int(input("enter id:"))
            name = input("enter name:")
            # address = input("enter new address if need:")
            mycursor.execute("UPDATE emp_records SET name = %s  WHERE id = %s ",(name,id,))
            mydb.commit()
            mycursor.execute("SELECT * FROM emp_records")
            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)
            print(mycursor.rowcount, " after new update ...record(s) affected")
        except Exception as err:
            print(repr(err))


    elif(emp_option==6):


        mycursor = mydb.cursor()
        mycursor.execute("ALTER TABLE emp_records DROP COLUMN id ")
        mydb.commit()
    else:
        print("please ..choose from the available option  ")


conditon(emp_option=get_option())































    # elif(emp_option == 2):
    #
    #      print(" U HAVE SELECTED OPTION NO: 2.......inserting values into the table ")
    #     try:
    #         sql = "INSERT INTO emp_records (id, name, address) VALUES (%s,%s, %s)"
    #         val = [
    #             ('1','kavi', 'Lowstreet '),
    #             ('2','rubi', 'Apple '),
    #             ('3','sugu', 'Mountain '),
    #             ('4','devi', 'Valley '),
    #             ('5','sathish', 'Ocean '),
    #             ('6','jaggu','lake')
    #
    #                 ]
    #         mycursor = mydb.cursor()
    #         mycursor.executemany(sql, val)
    #
    #         mydb.commit()
    #
    #         print(mycursor.rowcount, "was inserted.")
    #     except Exception as err:
    #         print(repr(err))
    #
    # elif(emp_count == 3):
    #     try:
    #         print(" U HAVE SELECTED OPTION NO: 3.......viewing all the data of the respective table")
    #         mycursor = mydb.cursor()
    #
    #         mycursor.execute("SELECT * FROM emp_records")
    #
    #         myresult = mycursor.fetchall()
    #
    #         for x in myresult:
    #             print(x)
    #     except Exception as err:
    #         print(repr(err))
    #
    # elif(emp_count == 4 ):
    #
    #     print(" U HAVE SELECTED OPTION NO: 3.......get by respective id")
    #     sql = "SELECT * FROM emp_records WHERE id = %s"
    #     id = get_by_id()
    #
    #     mycursor = mydb.cursor()
    #     mycursor.execute(sql, id)
    #
    #     myresult = mycursor.fetchall()
    #
    #     for x in myresult:
    #         print(x)
    #
    #
    # elif(emp_count == 5):
    #     print(" U HAVE SELECTED OPTION NO: 5.......update the values in the table")
    #     mycursor = mydb.cursor()
    #     mycursor.execute("ALTER TABLE emp_records ADD COLUMN age INT (10)")
    #
    #
    # elif(emp_count == 6):
    #     print(" U HAVE SELECTED OPTION NO: 6.......delete the values in the table")





