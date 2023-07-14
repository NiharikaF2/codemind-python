n=input().split()
l=("aeiouAEIOU")
b=[]
for i in n:
    c=0
    for j in i:
        if j in l:
            c+=1
    b.append(c)
print(max(b))