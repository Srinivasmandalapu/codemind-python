n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=0
p=[]
for i in l1:
    if(i not in l2 and i not in p):
        p.append(i)
        c+=1
q=[]
for i in l2:
    if(i not in l1 and i not in q):
        q.append(i)
        c+=1
print(c)