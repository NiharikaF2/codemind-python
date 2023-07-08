n=int(input())
l=list(map(int,input().split()))
x=int(input())
d=0
for i in l:
    if i<=x:
        d+=i
print(d)
        