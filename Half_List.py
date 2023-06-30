n=int(input())
l=list(map(int,input().split()))
m=n//2-1
M=n//2
c=l[:m:-1]
b=l[:M:]
z=c+b
print(*z)