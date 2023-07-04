x=int(input())
l=list(map(int,input().split()))
x=len(l)
t=0
j=0
for i in l:
    t+=i
    j=t//x
if j in l:
    print("True")
else:
    print("False")
    
    