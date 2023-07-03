n=int(input())
l=list(map(int,input().split()))
x=len(l)
e=0
for i in range(x):
    if i%2==0:
        e+=l[i]
print(e)