x=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
t=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
t=e+o
print(*t)