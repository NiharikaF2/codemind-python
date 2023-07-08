n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    i=str(i)
    i=list(i)
    i.reverse()
    i=''.join(i)
    i=int(i)
    d.append(i)
print(*d)