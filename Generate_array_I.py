n=int(input())
l=list(map(int,input().split()))
for i in range(0,n,2):
    while(l[i+1]):
        print(l[i],end=" ")
        l[i+1]-=1