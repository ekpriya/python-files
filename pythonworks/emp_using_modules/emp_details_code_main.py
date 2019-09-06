import emp_using_modules.emp_details_code_part
import emp_using_modules. emp_details_code_stack_part
import emp_using_modules.emp_details_code_queue_part

emp_details = emp_using_modules.emp_details_code_part.get_details()
new_list = emp_details[:]
emp_using_modules.emp_details_code_stack_part.emp_stack_function(emp_details)
emp_using_modules.emp_details_code_queue_part.emp_queue_function(new_list)




# new_list = copy.copy(emp_details)
# new_list = emp_details.copy()
# emp_details.copy()