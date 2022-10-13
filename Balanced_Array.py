n=int(input())
for _ in range(n):
    p=int(input())
    r=0
    l=list(map(int,input().split()))
    s=0
    c=0
    for j in range(p):
        s=sum(l[:j])
        c=sum(l[j+1:])
        if(c==s):
            r+=1
    if(r==0):
        print("NO")
    else:
        print("YES")