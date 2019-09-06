

class GetStack:
     def get_stack(self, data):
         try:
            print("....file stack operation...")
            while data:
             print(data.pop())
         except Exception:
             print('these is some problem ')


