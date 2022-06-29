s=input()
z=s.split()
ma=0
v="aeiouAEIOU"
for i in z:
    x=0
    for j in range(len(i)):
        if i[j] in v:
            x+=1
    break
for i in z:
    c=0 
    for j in range(len(i)):
        if i[j] in v:
            c+=1 
    if(c<=x):
        ma=c
print(ma)