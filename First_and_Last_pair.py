n=int(input())
l=list(map(int,input().split()))
o=[]
r=[]
for i in range(n//2+1):
    o.append(l[i])
for i in range(n-1,n//2,-1):
    r.append(l[i])
i=0
j=0
while(i<len(o) or j<len(r)):
    if(i<len(o)):
        print(o[i],end=" ")
        i+=1
    if(j<len(r)):
        print(r[j],end=' ')
        j+=1
if n%2!=0:
    print('0')