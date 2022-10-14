n=input().lower()
p=input().lower()
n=n.split()
p=p.split()
c=0
s=0
q=0
for i in n:
    c=0
    q=n.count(i)
    for j in p:
        if(i==j and i!=" "):
            c+=1
    if(c==1 and q==1):
        s+=1
print(s)
