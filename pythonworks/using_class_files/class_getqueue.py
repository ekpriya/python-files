from collections import deque
class GetQueue:
    def get_queue(self, emp_details):
        # get_detail_obj = GetDetails()
        # emp_details = get_detail_obj.get_details()
        new_list = emp_details[:]
        result = deque(new_list)
        print('queue operation')
        while result:
            print(result.popleft())
