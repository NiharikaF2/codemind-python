n=int(input())
l=list(map(int,input().split()))
j=0
t=0
x=len(l)
for i in l:
    j+=i
    t=j/x
print("%.2f"%t)
    
    