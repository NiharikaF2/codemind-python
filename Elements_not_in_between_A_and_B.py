a=int(input())
l=list(map(int,input().split()))
x,n=map(int,input().split())
c=[]
for i in l:
    if i not in range(x,n+1):
       c.append(i)
if len(c)>0:
    print(*c)
else:
    print("-1")
