n=int(input())
c=0
d=0
l=list(map(int,input().split()))
for i in range(2,n):
    if(l[i-1]+l[i-2]==l[i]):
        c+=1
    else:
        d=1
        break
if(c>0 and d==0):
    print("yes")
else:
    print("no")
        