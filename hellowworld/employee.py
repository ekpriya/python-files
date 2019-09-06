from collections import deque
employee1=[]
employee2=[]
employee3=[]
employee1.append(({'id':'1','name':'aaa','age':22,'location':'chennai'}))
employee2.append(({'id':'2','name':'bbb','age':23,'location':'delhi'}))
employee3.append(({'id':'3','name':'ccc','age':'21','location':'madhurai'}))

details=deque([employee1,employee2,employee3])
employee3.append({'country:india'})
employee3.append({'state:tn'})
details.popleft()
# details.popleft()
# for e in details:
print(details)
# detailsreverse={v:k for k,v in employee4}
# reverse=details.reverse()
# print(reverse)
# employee1.reverse()
# print(employee1)