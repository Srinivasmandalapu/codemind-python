s=input()
z=s.split()
v="aeiouAEIOU"
for i in z:
    c=0
    for j in range(len(i)):
        if i[j] in v:
            c+=1
    print(c,end=" ")#print(c)