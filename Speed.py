t=int(input())
for i in range(t):
    c=0
    n=int(input())
    a=list(map(int,input().split()))
    min=a[0]
    for i in range(len(a)):
        if(a[i]<=min):
            c+=1
            min=a[i]
    print(c)