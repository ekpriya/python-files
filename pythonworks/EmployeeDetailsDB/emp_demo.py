import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root@123",
  database="EmployeeDetailsDB"
)

print(mydb)


# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root@123"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE mydatabase")













# import mysql.connector
# from mysql.connector import Error
#
# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='Electronics',
#                                          user='pynative',
#                                          password='pynative@#29')
#     sql_select_Query = "select * from Laptop"
#     cursor = connection.cursor()
#     cursor.execute(sql_select_Query)
#     records = cursor.fetchall()
#     print("Total number of rows in Laptop is: ", cursor.rowcount)
#     print("\nPrinting each laptop record")
#     for row in records:
#         print("Id = ", row[0], )
#         print("Name = ", row[1])
#         print("Price  = ", row[2])
#         print("Purchase date  = ", row[3], "\n")
# except Error as e:
#     print("Error reading data from MySQL table", e)
# finally:
#     if (connection.is_connected()):
#         connection.close()
#         cursor.close()
#         print("MySQL connection is closed")