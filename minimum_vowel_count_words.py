n=input()
z=n.split()
q="aeiouAEIOU"
ma=x=0
for i in z:
    c=0
    for j in i:
        if j in q:
            c+=1
    if ma<c:
        ma=c
for i in z:
    c=0
    for j in i:
       if j in q:
        c+=1
    if ma==c:
       x+=1
print(x)