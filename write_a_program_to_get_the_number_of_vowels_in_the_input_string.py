n=input()
x=['a','e','i','o','u','A','E','I','O','U']
c=[]
d=0
for i in n:
    if i in x:
        c.append(i)
if len(c)>0:
    print(len(c))
else:
    print(0)