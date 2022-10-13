def fun(n):
    d=0
    while(n!=0):
        d=n%10
        n=n//10
        if(d==2 or d==3 or d==9):
            return True
        else:
            return False
n=int(input())
c=0
for i in range(n):
    c=0
    n,m=map(int,input().split())
    for i in range(n,m+1):
        if(fun(i)):
            c+=1
    print(c)