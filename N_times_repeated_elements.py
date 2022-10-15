n=int(input())
l=list(map(int,input().split()))
k=int(input())
p=[]
c=0
f=0
for i in l:
    c=l.count(i)
    if(i not in p and c==k):
        p.append(i)
        print(i,end=" ")
        f=1
if(f==0):
    print("-1")
