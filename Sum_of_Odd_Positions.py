n=int(input())
l=list(map(int,input().split()))
x=len(l)
o=0
for i in range (x):
    if i%2!=0:
        o+=l[i]
print(o)
        