n=input()
f=list(n)
c=['1','2','3','4','5','6','7','8','9','0']
d=[]
for i in f:
    if i in c:
        d.append(int(i))
print(sum(d))