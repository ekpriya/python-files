from collections import deque
queue=deque(['id:1','name:kavi','age:21','loc:chennai'])
emp2=['id:2','name:savi','age:20','loc:delhi']
details=[queue]
# queue.append('favcolor:black')
# queue.append('state:TN')
# queue.append('country:india')
queue.popleft()
# emp1.append('project:cloud')
for e in details:
    print(e)
