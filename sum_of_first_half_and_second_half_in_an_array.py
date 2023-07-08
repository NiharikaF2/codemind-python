n=int(input())
l=list(map(int,input().split()))
d=n//2
f=0
b=0
for i in l:
    if i in range(l[0],d+1):
        f+=i
    else:
        b+=i
        
print(f)
print(b)