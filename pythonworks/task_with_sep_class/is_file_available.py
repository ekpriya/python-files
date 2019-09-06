
import json

class readFiles():
    def read_files(self):
        try:
            with open('data.json','r') as f:
                data =json.load(f)
                return data
        except FileNotFoundError:
            print("......file is not available.....")
        except PermissionError:
            print('.....permission is denied  :check file setting.... ')
        except Exception as error:
            print('....ERROR check the CODE...', repr(error))