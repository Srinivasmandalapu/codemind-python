n=input()
l=[]
p=[]
c=0
m=1000
for i in n:
    if(i.isdigit()):
        l.append(i)
s=set(l)
p=list(sorted(s,reverse=True))
for i in p:
    if(int(i)%2!=0):
        c+=1
if(c==len(p)):
    print(-1)
else:
    for i in p:
        if(int(m)>int(i) and (int(i)%2==0)):
            m=i
    p.remove(m)
    p.append(m)
    print(*p,sep='')      