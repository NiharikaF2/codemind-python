n=input().split()
c=[]
for i in n:
    s=list(i)
    s=str(i)
    s=i[::-1]
    c.append(s)
print(*c)