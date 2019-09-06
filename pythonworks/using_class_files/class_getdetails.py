class GetDetails:
    def get_details(self):
        emp_details = []
        emp_count = int(input('employee count:'))
        for i in range(emp_count):
            id = int(input("please enter id:"))
            name = input("Please enter name: ")
            age = int(input("Please enter age: "))
            address = input("Please enter address: ")
            emp = {'id': id, 'name': name, 'age': age, 'address': address}
            emp_details.append(emp)
        return emp_details

