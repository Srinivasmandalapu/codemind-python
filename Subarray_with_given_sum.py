t=int(input())
for i in range(t):
    n,se=map(int,input().split())
    arr=list(map(int,input().split()))
    x=y=count=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if(s==se):
                x=i
                y=j
                count=1
                break
        if(count==1):
            break
    if(count==1):
        print(x+1,end=" ")
        print(y+1)
    else:
        print(-1)