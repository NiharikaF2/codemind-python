n=input()
x=['a','e','i','o','u']
c=[]
d=[]
for i in n:
    if i in x:
        c.append(i)
for i in c:
    if i not in d:
        d.append(i)
if len(d)==len(x):
    print("True")
else:
    print("False")
        