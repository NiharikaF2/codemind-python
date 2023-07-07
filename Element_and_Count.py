x=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for j in l:
      if j not in a:
          a.append(j)
for i in a:
    b.append(i)
    b.append(l.count(i))
    
    
print(*b)
       