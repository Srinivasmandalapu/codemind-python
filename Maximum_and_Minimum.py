n=int(input())
l=list(map(int,input().split()))
m=0
c=0
p=0
q=0
r=[]
d=1000
for i in l:
    c=l.count(i)
    if(i==c):
        r.append(i)
        if(c>m):
            m=c
            p=i
        if(d>c):
            d=c
            q=i
if(p==0 and q==0):
    print('-1')
else:
    print(q,p)