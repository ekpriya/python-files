from task_with_sep_class.emp_details import GetDetailsF
from task_with_sep_class.import_into_file import SaveFiles
from task_with_sep_class.file_stack import GetStack
from task_with_sep_class.file_queue import GetQueue
from task_with_sep_class.is_file_available import readFiles

if __name__ == "__main__":

    emp_details_obj = GetDetailsF()
    result = emp_details_obj.get_details()
    emp_details_obj1 = SaveFiles()
    emp_details_obj1.save_files(emp_detailsjson=result)
    emp_sobj =readFiles()
    data =emp_sobj.read_files()
    emp_details_obj2 = GetStack()
    emp_details_obj2.get_stack(data = data)
    data = emp_sobj.read_files()
    emp_details_obj3 = GetQueue()
    emp_details_obj3.get_queue(dataqueue = data)
