# try:
#     x = 2/0
# except ZeroDivisionError as err:
#     print(err)



# def division_operation(x,y):
#     try:
#         result = x / y
#         print('the result:',result)
#     except ZeroDivisionError as err:
#         print(err)

# division_operation(2,0)



# num = [1, 2, 3]
#
#
# def fun():
#     try:
#         for i in num:
#             print(num[i])
#     except IndexError as err:
#         print(err)
#
# fun()


# data = {'name': 'john', 'dept': 'cse' }
# print(data['name'])
# print(data['loc'])
# data['age'] = '22'
# print(data)



# try:
#     x = int(input("enter a number: "))
# except ValueError as err:
#     print(err)
#     print('try again.enter integer.')



# try:
#     print(x)
# except NameError:
#     print('variable not defined')
# except :
#     print('some other error')



# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")



# try:
#   f = open("demofile.txt")
#   f.write("Lorum Ipsum")
# except:
#   print("Something went wrong when writing to the file")
#
# else:
#     print('nnn')
# finally:
#   f.close()


# try:
#     raise NameError('Hi')
# except NameError:
#     print('An exception ')
    # raise