n=int(input())
l=list(map(int,input().split()))
m=0
c=0
f=0
d=1000
r=[]
for i in l:
    c=l.count(i)
    if(i==c):
        if(i not in r):
            r.append(i)
            f=1
            print(i,end=" ")
if(f==0):
    print("-1")