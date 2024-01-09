n=input()
x=['a','e','i','o','u']
l=[]
q=[]
for j in n:
    if j in x:
        l.append('V')
    else:
        l.append('C')
i=0
while i<len(l):
    c=l[i]
    q.append(c)
    while (i+1)<len(l) and l[i+1]==c:
        i+=1
    i+=1
print("".join(q),end="")

