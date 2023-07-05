a=int(input())
l=list(map(int,input().split()))
x,n=map(int,input().split())
sum=0
for i in l:
    if i not in range(x,n+1):
        sum+=i
print(sum)