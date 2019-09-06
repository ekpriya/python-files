
# def emp_count_function():
#     print('')
#
#
# emp_details = []
# emp_count = int(input('employee count:'))
# for i in range(emp_count):
#             id = int(input("please enter id:"))
#             name = input("Please enter name: ")
#             age = int(input("Please enter age: "))
#             address = input("Please enter address: ")
#             emp={'id':id,'name': name , 'age':age,'address':address}
#             emp_details.append(emp)
# # print(emp_details)
# result=emp_details
# print(result)

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
    print(emp_details)
    # result = emp_details
    return emp_details