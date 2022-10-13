n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if(i not in d.keys()):
        d[i]=1
    else:
        d[i]+=1
l=[]
c=0
for i in d:
    if(d[i]>1):
        c+=1
for i in range(c):
    m=ele=0
    for i in d:
        if(d[i]>m):
            m=d[i]
            ele=i
    l.append(ele)
    d[ele]=0
a=[]
for i in d:
    if(d[i]>0):
        a.append(i)
a.sort()
for i in a:
    l.append(i)
print(*l)