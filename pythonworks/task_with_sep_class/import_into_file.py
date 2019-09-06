import json
class SaveFiles:
    def save_files(self, emp_detailsjson):
        try:
            print("......file handling...")
            with open('data.json', 'w') as fout:
                json.dump(emp_detailsjson, fout)
        except FileNotFoundError as err:
            print(err)
        except FileExistsError as err:
            print(err)
        except PermissionError:
            print(".....permission has been denied...check file setting.... ")
        except Exception:
            print(' ....There is some problem with your code...')
        except IOError:
            print('input error ...check file ')
        else:
            f = open('data.json','r')
            print(f.readline(),end ='\n')