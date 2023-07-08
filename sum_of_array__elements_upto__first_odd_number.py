n=int(input())
l=list(map(int,input().split()))
d=0
for i in l:
    if i%2==0:
        d+=i
    else:
        break
print(d)