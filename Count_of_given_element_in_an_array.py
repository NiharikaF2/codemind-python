x=int(input())
l=list(map(int,input().split()))
n=int(input())
for i in range (len(l)):
    t=l.count(n)
print(t)