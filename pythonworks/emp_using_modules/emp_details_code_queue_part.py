
from collections import deque# import emp_details_code_stack_part
# print(emp_details_code_stack_part.result)
def emp_queue_function(emp_details):
    result = deque(emp_details)
    while result:
        print( result.popleft())