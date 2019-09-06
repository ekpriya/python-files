def create_file():
  f = open("myfile.txt", "x")


def delete_file():
  import os
  if os.path.exists("myfilee.txt"):
    os.remove("myfilee.txt")
  else:
    print("The file does not exist")

def just_read_file():
  f = open('myfile.txt','r')
  print(f.read())

def read_file():
  f = open('myfile.txt','r')
  print(f.read(10))

def readline_file():
  f = open('myfile.txt','r')
  print(f.readline())

def append_file():
  f = open("myfile.txt", "a")
  f.write(" more content into the file ")
  f.close()

  f = open("myfile.txt", "r")
  print(f.read())

def write_file():
  f = open('myfile.txt','w')
  f.write('this is the new overwrite into thr file')
  print(f.close())

  f = open('myfile.txt','r')
  print(f.read())
  f.close()

def simple():
  filename = input('id ')
# create_file()
# delete_file()
# read_file()
# just_read_file()
# readline_file()
# append_file()
# write_file()