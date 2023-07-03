n=int(input())
l=list(map(int,input().split()))
e=0
o=0
x=len(l)
for i in range (x):
    
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
print(e-o)