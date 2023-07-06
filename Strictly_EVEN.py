n=int(input())
l=list(map(int,input().split()))
c=0
t=0
for i in range(n):
    if l[i]%2==0:
        c+=1
    if i%2==0 and l[i]%2==0:
        t+=1
if c==t:
    print("True")
else:
    print("False")
        