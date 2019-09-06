
class Add:
    def __init__(self, value1, value2):
         self.v1 = value1
         self.v2 = value2

x = Add(8 , 8)
print(x.v1 * x.v2)
x.counter = 1
while x.counter < 10:
 x.counter = x.counter * 2
print(x.counter)
