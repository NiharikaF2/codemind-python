m=input()
d=0
for j in m:
    if j.isdigit():
        d+=1
if d>0:
    print("Contains",d,"digit")
else:
    print("Doesn't contain digit")