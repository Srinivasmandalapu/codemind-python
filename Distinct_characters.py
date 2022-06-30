s=input()
x=len(s)
c=v=z=w=0
b=[]
for i in range(x):
    c=0
    if s[i]==" ":
        continue
    else:
        if s[i].upper() not in b and s[i].lower() not in b:
            if s[i].islower():
                b.append(s[i])
v=len(b)
b.sort()
for i in range(v):
    print(b[i],end="")