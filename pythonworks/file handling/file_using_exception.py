

def readOnly_file():
    f = None
    try:
        f = open('my_write_file','w')
        f.write('vb this is the new content .....')

    except ValueError:
        print('unsupported mode error')
    else:
       print('data updated .......')
    finally:
        if f != None:

            f.close()

def writeOnly_file():

    try:
        f = open('myfile.txt','r')
        f.write(' ....i am kavipriya ')

        # f = open('myfile.txt','r')
        # print(f.read())
    except FileNotFoundError:
        print('file not found')
    except:
        print('something is wrong')
    finally:
        f.close()

readOnly_file()
# writeOnly_file()