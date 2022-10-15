n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(n-1):
    if(l[i]>l[i+1]):
        c+=1
if(c==n-1):
    print("yes")
else:
    print("no")
        