from collections import deque


class Employee:
     def __init__(self):
        # self.get_details()
        self.get_stack()
        self.get_queue()

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

     def get_stack(self):
        emp_details = self.get_details()
        while emp_details:
            print(emp_details.pop())

     def get_queue(self):
        emp_details = self.get_details()
        new_list = emp_details[:]
        result = deque(new_list)
        while result:
            print(result.popleft())

emp_ob = Employee()
# emp_ob.get_details()
# emp_ob.get_stack
# emp_ob.get_queue