n=int(input())
l=list(map(int,input().split()))
c=0
m=max(l)
for i in range (m):
    i=i*i
    if i in l:
        c=c+i
print(c)