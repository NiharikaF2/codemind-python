n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
for i in l:
    if i not in range(a,b+1):
        d.append(i)
if len(d)>0:
    print(min(d))
else:
    print(-1)