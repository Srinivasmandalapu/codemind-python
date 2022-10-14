n=input().lower()
p=input().lower()
n=n.split()
p=p.split()
c=0
for i in n:
    for j in p:
        if(i==j and i!=" "):
            c+=1
            break
print(c)
