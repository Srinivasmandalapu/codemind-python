import math
t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    c=0
    for j in p:
        for k in p:
            if j!=k:
                if j+k in p:
                    c+=1
    if(c>0):
        print(c//2)
    else :
        print(-1)