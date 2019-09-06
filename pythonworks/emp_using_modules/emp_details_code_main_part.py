from collections import deque


def get_details():
    emp_details = []
    emp_count = int(input('employee count:'))
    for i in range(emp_count):
                id = int(input("please enter id:"))
                name = input("Please enter name: ")
                age = int(input("Please enter age: "))
                address = input("Please enter address: ")
                emp={'id': id, 'name': name, 'age': age, 'address': address}
                emp_details.append(emp)
    # print(emp_details)
    # result = emp_details
    return emp_details


# resultvalues = emp_count_function()
# print(resultvalues)

def emp_stack_function():
    emp_details = get_details()
    while emp_details:
        print( emp_details.pop())


def emp_queue_function():
    emp_details = get_details()
    result = deque(emp_details)
    while result:
        print( result.popleft())

# get_details()
# emp_stack_function()
emp_queue_function()
