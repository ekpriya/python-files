class GetDetailsF:
    def get_details(self):
        emp_details = []

        while True:
            try:
                emp_count = int(input('Employee Count:'))
                assert (emp_count>0)
                break
            except AssertionError :
                print ('number must be greater than zero')
            except ValueError:
                print("enter a integer")
            except KeyboardInterrupt:
                print(" No Data Entered")


        for i in range(emp_count):
            id = int(input("please Enter id:"))
            name = input("Please Enter name: ")
            age = int(input("Please Enter age: "))
            address = input("Please Enter address: ")
            emp = {'id': id, 'name': name, 'age': age, 'address': address}
            emp_details.append(emp)
        return emp_details
