n=int(input())
l=list(map(int,input().split()))
x=0
for i in l:
    if i==0 or i==1:
        x+=1
if x==len(l):
    print("True")
else:
    print("False")
        