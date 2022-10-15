n=int(input())
l=list(map(int,input().split()))
c=0
s=0
d=0
a=0
p=[]
for i in l:
    c=0
    c=l.count(i)
    if(c==i and i not in p):
        s=s+i
        p.append(i)
        d+=1
if(d==0):
    print("-1")
a=s/d
print("%.2f"%a)