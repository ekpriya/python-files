# class Dog:
#     kind='canine'
#
#     def __init__(self,name):
#         self.n=name
#
# x = Dog('buddy')
# e = Dog('kitty')
# print(e.n)
# print(x.n)
# print(x.kind,x.n)
# print(e.n,e.kind)

# ................example to append to a list .................


class Dog:
    def __init__(self,name):
        self.name = name
        self.tricks = []

    def my_tricks(self,tricks):
        self.tricks.append(tricks)


a = Dog('kitty')
b = Dog('buddy')
print(a.name)
print(b.name)
a.my_tricks('roll ')
b.my_tricks('sleep')
print(a.tricks)
print(b.tricks)

#..........function with global...............

