from collections import deque
emp_details=[]

emp_count= int (input('emplyee count:'))
for i in range(emp_count):
    id = int(input("please enter id:"))
    name = input("Please enter name: ")
    age = int(input("Please enter age: "))
    address = input("Please enter address: ")
    # for e in emp_details:
    # print(emp_details)
    emp={'id':id,'name': name , 'age':age,'address':address}
    # emp_details={'id':id,'name': name , 'age':age,'address':address}
    emp_details.append(emp)
    # print(emp_details)
result=deque(emp_details)
# result.popleft()

while result:
    # result.popleft()
    print(result.popleft())
#print(result)
    # emp_details=({ 'id':'', 'name':'', 'age':'', 'address':''})
# print(emp_details)
# emp_details.pop()
# print(result)
# emp_details.append('gender:female')
# emp_details['gender'] = 'female'
# for items in emp_details:
   #new_items={'gender':'value'}
   # result.append(new_items)

  # print(emp_details)

# emp_count=[10]
# def emp():
#     id = int(input("please enter id:"))
#     name = input("Please enter name: ")
#     for i in emp_count:
#         print(emp.emp[i])



