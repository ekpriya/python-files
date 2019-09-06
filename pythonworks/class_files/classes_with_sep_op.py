from collections import deque


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


class GetStack:
    def get_stack(self, emp_details):
        # get_details_ob = GetDetails()
        print('stack operation')
        while emp_details:
            print(emp_details.pop())


class GetQueue:
    def get_queue(self, emp_details):
        # get_detail_obj = GetDetails()
        # emp_details = get_detail_obj.get_details()
        new_list = emp_details[:]
        result = deque(new_list)
        print('queue operation')
        while result:
            print(result.popleft())


if __name__ == '__main__':

    emp_ob = GetDetails()
   # emp_ob.get_details()
    result =  emp_ob.get_details()
    new_list = result[:]
    emp_ob1 = GetStack()
    emp_ob1.get_stack(emp_details=result)

    emp_ob2 = GetQueue()
    emp_ob2.get_queue(emp_details=new_list)





