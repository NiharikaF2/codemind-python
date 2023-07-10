n,k=map(int,input().split())
l=list(map(int,input().split()))
d=0
for i in l:
    if i<0:
        i=-i
    i=str(i)
    i=list(i)
    if len(i)==k:
        d+=1
print(d)
        