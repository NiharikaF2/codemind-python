n=input()
l=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
d=0
for i in n:
    if i in l:
        d+=1
print(d)