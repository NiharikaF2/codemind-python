import math
n=int(input())
l=list(map(int,input().split()))
m1=l[0]
m2=l[1]
lcm=math.lcm(m1,m2)
for i in range(2,len(l)):
    lcm=math.lcm(lcm,l[i])
print(lcm)