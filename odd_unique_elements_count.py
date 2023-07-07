n=int(input())
l=list(map(int,input().split()))
c=[]
d=0
for i in l:
    if i not in c:
        c.append(i)
for i in c:
    if i%2!=0:
        d+=1
print(d)
            