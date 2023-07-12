n=input()
x=['a','e','i','o','u']
c=[]
d=[]
for i in n:
    if i in x:
        c.append(i)
for i in x:
    if i not in c:
        d.append(i)
if len(d)>0:
    print(*d)
else:
    print(0)