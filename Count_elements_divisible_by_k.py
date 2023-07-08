n,k=map(int,input().split())
l=list(map(int,input().split()))
d=0
for i in l:
    if i%k==0:
        d+=1
print(d)