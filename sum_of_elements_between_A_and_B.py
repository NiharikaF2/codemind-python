n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=0
for i in l:
    if i in range(a,b+1):
        d+=i
print(d)