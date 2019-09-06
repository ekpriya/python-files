import json
from collections import  deque

class GetQueue:
    def get_queue(self, dataqueue):
        try:
            print("......file queue operation...")
            result = deque(dataqueue)
            while result:
             print(result.popleft())
        except Exception as err:
            print("There is some problem",str(err))



