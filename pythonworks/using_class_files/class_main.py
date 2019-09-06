# import using_class_files.class_getdetails
# import using_class_files.class_getstack
# import using_class_files.class_getqueue


from .class_getdetails import GetDetails
from using_class_files.class_getqueue import GetQueue
from .class_getstack import GetStack

if __name__ == '__main__':
    # emp_details_obj = using_class_files.class_getdetails.GetDetails()
    emp_details_obj = GetDetails()
    # emp_details_obj.get_details()
    result = emp_details_obj.get_details()
    new_list = result[:]
    emp_stack_obj = GetStack()
    emp_stack_obj.get_stack(emp_details=result)
    emp_queue_obj = GetQueue()
    emp_queue_obj.get_queue(emp_details=new_list)
