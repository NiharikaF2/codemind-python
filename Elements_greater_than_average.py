n=int(input())
l=list(map(int,input().split()))
x=len(l)
c=0
a=0
for i in l:
    c+=i
s=c//x
for i in l:
    if i>=s:
        a+=1
print(a)
        