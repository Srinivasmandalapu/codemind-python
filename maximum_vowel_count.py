s=input()
z=s.split()
ma=0
v="aeiouAEIOU"
for i in z:
    c=0
    for j in range(len(i)):
        if i[j] in v:
            c+=1
    if(c>ma):
        ma=c
print(ma)