import json
from collections import deque


class GetDetails:
    def get_details(self):
        emp_details = []
        while True:
            try:
                emp_count = int(input('Employee Count:'))
                assert (emp_count > 0)
                break
            except AssertionError:
                print('number must be greater than zero')
        for i in range(emp_count):
            id = int(input("please Enter id:"))
            name = input("Please Enter name: ")
            age = int(input("Please Enter age: "))
            address = input("Please Enter address: ")
            emp = {'id': id, 'name': name, 'age': age, 'address': address}
            emp_details.append(emp)
        return emp_details



class SaveFiles:
    def save_files(self, emp_detailsjson):
        print("......file handling...")

        try:
            with open('outputfile.json', 'w') as fout:
                json.dump(emp_detailsjson, fout)
        except FileNotFoundError as err:
            print(err)
        except FileExistsError as err:
            print(err)
        except PermissionError:
            print('the permission for file has been denied..check the settings')
        else:
            f = open('outputfile.json', 'r')
            print(f.read(), end='\n')



class GetStack:
     def get_stack(self):
         try:
            with open('outputfile.json') as f:
                data = json.load(f)
                print("......file stack operation...")
                while data:
                 print(data.pop())
         except FileNotFoundError :
             print("file not found ...")

class GetQueue:
     def get_queue(self):
         print("......file queue operation...")
         try:
             with open('outputfile.json') as f:
                data = json.load(f)
                result = deque(data)
                while result:
                     print(result.popleft())
         except FileNotFoundError as err:
             print(err)




if __name__ == '__main__':

    emp_ob = GetDetails()
    # emp_ob.get_details()
    result = emp_ob.get_details()
    # new_list = result[:]
    emp_ob1 = SaveFiles()
    emp_ob1.save_files( emp_detailsjson = result)
    emp_ob2 =GetStack()
    emp_ob2.get_stack()
    emp_obj3 =GetQueue()
    emp_obj3.get_queue()

