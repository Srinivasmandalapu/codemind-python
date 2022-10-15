n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(n//2+1):
    p.append(l[i])
q=[]
for i in range(n-1,n//2,-1):
    q.append(l[i])
i=0
j=0
while(i<len(p) or j<len(q)):
    if(i<len(p)):
        print(p[i],end=" ")
        i+=1
    if(j<len(q)):
        print(q[j],end=" ")
        j+=1
if(n%2!=0):
    print(0)